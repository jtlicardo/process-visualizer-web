import configparser

import openai
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sse import sse

from coreference_resolution.coref import resolve_references
from create_bpmn_structure import create_bpmn_structure
from process_bpmn_data import (
    add_loops,
    add_process_end_events,
    add_task_ids,
    batch_classify_process_info,
    create_agent_task_pairs,
    create_sentence_data,
    extract_all_entities,
    extract_bpmn_data,
    find_sentences_with_loop_keywords,
    fix_bpmn_data,
    generate_graph_image,
    handle_text_with_conditions,
    handle_text_with_parallel_keywords,
    has_parallel_keywords,
    should_resolve_coreferences,
)

app = Flask(__name__)
app.config.from_object(__name__)
app.config["REDIS_URL"] = "redis://redis:6379"
app.register_blueprint(sse, url_prefix="/stream")

CORS(app, resources={r"/*": {"origins": "*"}})


def process_text(text: str) -> list[dict]:

    if should_resolve_coreferences(text):
        sse.publish({"message": "Resolving coreferences..."}, type="message")
        text = resolve_references(text)
    else:
        sse.publish({"message": "No coreferences to resolve"}, type="message")

    sse.publish({"message": "Extracting BPMN data..."}, type="message")

    data = extract_bpmn_data(text)

    if not data:
        return

    data = fix_bpmn_data(data)

    sse.publish({"message": "Extracting entities..."}, type="message")

    agents, tasks, conditions, process_info = extract_all_entities(data, 0.6)
    parallel_gateway_data = []
    exclusive_gateway_data = []

    sse.publish({"message": "Creating agent-task pairs..."}, type="message")

    sents_data = create_sentence_data(text)

    agent_task_pairs = create_agent_task_pairs(agents, tasks, sents_data)

    if has_parallel_keywords(text):
        sse.publish({"message": "Handling parallel gateways..."}, type="message")
        parallel_gateway_data = handle_text_with_parallel_keywords(
            text, agent_task_pairs, sents_data
        )

    if len(conditions) > 0:
        sse.publish({"message": "Handling exclusive gateways..."}, type="message")
        agent_task_pairs, exclusive_gateway_data = handle_text_with_conditions(
            agent_task_pairs, conditions, sents_data, text
        )

    if len(process_info) > 0:
        process_info = batch_classify_process_info(process_info)
        agent_task_pairs = add_process_end_events(
            agent_task_pairs, sents_data, process_info
        )

    sse.publish({"message": "Adding task IDs..."}, type="message")

    loop_sentences = find_sentences_with_loop_keywords(sents_data)
    agent_task_pairs = add_task_ids(agent_task_pairs, sents_data, loop_sentences)
    agent_task_pairs = add_loops(agent_task_pairs, sents_data, loop_sentences)

    sse.publish({"message": "Creating BPMN structure..."}, type="message")

    structure = create_bpmn_structure(
        agent_task_pairs, parallel_gateway_data, exclusive_gateway_data, process_info
    )

    return structure


@app.route("/key", methods=["POST"])
def receive_api_key():
    data = request.get_json()
    openai.api_key = data["key"]
    try:
        models = openai.Model.list()
    except openai.error.AuthenticationError:
        return jsonify({"message": "Invalid API key"}), 401
    available_models = [
        model["id"]
        for model in models["data"]
        if "gpt-3.5-turbo" in model["id"] or "gpt-4" in model["id"]
    ]
    with open(".env", "w+") as f:
        f.write(f"OPENAI_KEY={data['key']}")
    return (
        jsonify({"message": "API key received", "available_models": available_models}),
        200,
    )


def configure_openai_model(model):
    config = configparser.ConfigParser()
    config.read("src\config.ini")
    config["OPENAI"] = {}
    config["OPENAI"]["model"] = model
    with open("src\config.ini", "w") as configfile:
        config.write(configfile)
    sse.publish({"message": f"Using OpenAI model: {model}"}, type="message")


@app.route("/text", methods=["POST"])
def receive_text_input():
    data = request.get_json()
    text = data["text"]
    model = data["model"]
    configure_openai_model(model)
    output = process_text(text)
    sse.publish({"message": "Generating graph image..."}, type="message")
    generate_graph_image(output)
    return jsonify({"message": "success"}), 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
