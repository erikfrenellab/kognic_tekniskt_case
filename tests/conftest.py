import json
import pytest


@pytest.fixture
def kognic_annotation():
    path = "tests/data/kognic_1.json"
    with open(path, "r") as f:
        return json.load(f)


@pytest.fixture
def open_label_annotation():
    path = "tests/data/open_label_1.json"
    with open(path, "r") as f:
        return json.load(f)
