import os

from flask import Flask, jsonify, request
from flask_cors import CORS
import openai

from process_bpmn_data import generate_graph_image, process_text

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})


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


@app.route("/text", methods=["POST"])
def receive_text_input():
    data = request.get_json()
    text = data["text"]
    print(text)
    output = process_text(text)
    generate_graph_image(output)
    return jsonify({"message": "success"}), 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
