import json
import yaml

from gendiff.create_diff import create_diff
from gendiff.formatters.plain import format_plain
from gendiff.formatters.json import format_json
from gendiff.formatters.stylish import format_stylish


def generate_diff(data1, data2, format_name="stylish"):
    file1 = get_data_from_file(data1)
    file2 = get_data_from_file(data2)
    data = create_diff(file1, file2)

    if format_name == 'plain':
        return format_plain(data)

    elif format_name == 'json':
        return format_json(data)

    elif format_name == 'stylish':
        return format_stylish(data)


def get_data_from_file(file_path):
    with open(file_path) as file:

        if file_path.endswith("json"):
            data = json.load(file)
        else:
            data = yaml.load(file, Loader=yaml.Loader)

    return data
