import json
import yaml


def get_data_from_file(file_path):
    with open(file_path) as file:

        if file_path.endswith("json"):
            data = json.load(file)
        else:
            data = yaml.load(file, Loader=yaml.Loader)

    return data
