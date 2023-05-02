import json
from collections import defaultdict

TYPE_MAP = {
    bool: "boolean",
    str: "text",
}

def _convert_to_objects(kognic_annotation):
    kognic_objects = kognic_annotation["shapeProperties"]
    open_label_objects = {}
    for name, properties in kognic_objects.items():
        type_ = properties["@all"]["class"]
        open_label_objects[name] = {
            "name": name,
            "type": type_,
        }
    return open_label_objects


def _convert_kognic_feature_to_open_label_frame(kognic_feature, kognic_object):
    key = kognic_feature["id"]
    bbox_name = "bbox-" + key.split("-")[0]
    x, y, w, h = _convert_bbox_from_extreme_points(kognic_feature["geometry"]["coordinates"])
    bbox = {
            "name": bbox_name,
            "stream": "CAM",
            "val": [x, y, w, h],
        }
    object_data = defaultdict(list)
    object_data["bbox"].append(bbox)
    kognic_object = kognic_object.copy()
    kognic_object.pop("class")
    for name, val in kognic_object.items():
        type_name = TYPE_MAP[type(val)]
        object_data[type_name].append({
            "name": name,
            "val": val,
        })

    # convert to regular dict
    od = {k: v for k, v in object_data.items()}

    return {"object_data": od}

def _convert_bbox_from_extreme_points(extreme_points):
    """
    Convert from extreme point bounding box to x,y, width and height, where (x,y) is the center of the box
    :param extreme_points: Coordinates of the four corners of the bounding box
    :return: the four values x, y, width, height
    """
    min_x = extreme_points["minX"]["coordinates"][0]
    max_x = extreme_points["maxX"]["coordinates"][0]
    min_y = extreme_points["minY"]["coordinates"][1]
    max_y = extreme_points["maxY"]["coordinates"][1]

    center_x = (min_x + max_x) / 2
    center_y = (min_y + max_y) / 2
    width = max_x - min_x
    height = max_y - min_y

    return center_x, center_y, width, height


def _convert_to_frames(kognic_annotation):
    kognic_features = kognic_annotation["shapes"]["CAM"]["features"]
    open_label_frames = {}
    for kognic_feature in kognic_features:
        key = kognic_feature["id"]
        kognic_object = kognic_annotation["shapeProperties"][key]["@all"]
        value = _convert_kognic_feature_to_open_label_frame(kognic_feature, kognic_object)
        open_label_frames[key] = value
    return {
        "0": {
            "objects": open_label_frames
        }
    }


def convert(kognic_annotation: str) -> str:
    """
    :param kognic_annotation: Annotations in the Kognic format, as a JSON string
    :return: Annotations converted to OpenLABEL format, as a JSON string
    """
    open_label_objects = _convert_to_objects(kognic_annotation)
    open_label_frames = _convert_to_frames(kognic_annotation)
    open_label_annotation = {
        "data": {
            "openlabel": {
                "objects": open_label_objects,
                "frames": open_label_frames,
            }
        }
    }
    return open_label_annotation