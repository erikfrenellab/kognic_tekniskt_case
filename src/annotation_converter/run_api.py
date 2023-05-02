import json

from flask import Flask, request, jsonify
from annotation_converter.converter import convert

app = Flask(__name__)

from flask_restful import Api
from flask_restful_swagger import swagger

app = Flask(__name__)
api = swagger.docs(Api(app), apiVersion='0.1')
@app.route('/api', methods=['GET'])
def get_payload():
    # Get payload from the request
    payload = request.args.get('payload')

    # Process payload and generate a result
    result = process_payload(payload)

    # Return the result as a response
    return jsonify(result)


def process_payload(payload):
    # Add your payload processing logic here
    # This is just an example
    payload_dict = json.loads(payload)
    print(payload_dict)
    result = convert(payload_dict)
    return result

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()