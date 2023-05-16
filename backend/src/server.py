import os

from flask import Flask, jsonify, request
from flask_cors import CORS

from process_bpmn_data import generate_graph_image, process_text

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/key", methods=["POST"])
def receive_api_key():
    data = request.get_json()
    key = data["key"]
    with open(".env", "w+") as f:
        f.write(f"OPENAI_KEY={key}")
    return jsonify({"status": "success"})


@app.route("/text", methods=["POST"])
def receive_text_input():
    data = request.get_json()
    text = data["text"]
    print(text)
    output = process_text(text)
    generate_graph_image(output)
    return jsonify({"status": "success"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
