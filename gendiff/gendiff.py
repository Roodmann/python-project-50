from gendiff.create_diff import get_diff_key
from gendiff.formatters.plain import format_plain
from gendiff.formatters.json import format_json
from gendiff.formatters.stylish import format_stylish
from gendiff.file_parser import get_data_from_file


def generate_diff(data1, data2, format_name="stylish"):
    file1 = get_data_from_file(data1)
    file2 = get_data_from_file(data2)
    data = get_diff_key(file1, file2)

    if format_name == 'plain':
        return format_plain(data)

    elif format_name == 'json':
        return format_json(data)

    elif format_name == 'stylish':
        return format_stylish(data)
