import json
import yaml


def get_data_from_file(file_path):
    with open(file_path) as file:
        if file_path.endswith(".json"):
            return json.load(file)
        elif file_path.endswith(".yml") or file_path.endswith(".yaml"):
            return yaml.load(file, Loader=yaml.Loader)
        else:
            raise ValueError("Unsupported file format: {file_path}")
