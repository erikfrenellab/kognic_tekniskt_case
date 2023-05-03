import json

from flask import Flask, request, jsonify
from annotation_converter.converter import convert

app = Flask(__name__)


@app.route("/api", methods=["GET"])
def get_payload():
    payload = request.args.get("payload")
    result = process_payload(payload)
    return jsonify(result)


def process_payload(payload):
    payload_dict = json.loads(payload)
    result = convert(payload_dict)
    return result


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
