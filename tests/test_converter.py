import json
import pprint

from annotation_converter import convert
from annotation_converter.run_api import app


def test_converter(kognic_annotation, open_label_annotation):
    converted_annotation = convert(kognic_annotation)

    # compare dict versions, not string versions
    error_str = json.dumps(kognic_annotation, indent=2) + "\n\n" + json.dumps(open_label_annotation, indent=2)
    assert converted_annotation == open_label_annotation, error_str

def test_rest_api(kognic_annotation, open_label_annotation):
    payload = json.dumps(kognic_annotation)
    with app.test_client() as client:
        # Send a GET request with payload = "hello world"

        response = client.get(f'/api?payload={payload}')

        # Check if response status code is 200 OK
        assert response.status_code == 200

        # Check if response payload is {"result": "HELLO WORLD"}
        expected_payload = open_label_annotation
        actual_payload = json.loads(response.data)
        assert actual_payload == expected_payload
