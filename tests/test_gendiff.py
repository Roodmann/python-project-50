import pytest
from gendiff import generate_diff


@pytest.mark.parametrize(
    "file_1, file_2, format, result",
    [
        #  test plain nested
        (
            "tests/fixtures/file_nested1.json",
            "tests/fixtures/file_nested2.json",
            'plain',
            "tests/fixtures/plain_result",
        ),

        #  test plain flat
        (
            "tests/fixtures/file1.json",
            "tests/fixtures/file2.json",
            "plain",
            "tests/fixtures/flat_plain_result",
        ),

        #  test stylish nested
        (
            "tests/fixtures/file_nested1.json",
            "tests/fixtures/file_nested2.json",
            "stylish",
            "tests/fixtures/stylish_result",
        ),
        #  test stylish flat
        (
            "tests/fixtures/file1.json",
            "tests/fixtures/file2.json",
            "stylish",
            "tests/fixtures/result",
        ),
    ]
)
def test_generate_diff(file_1, file_2, format, result):
    with open(result) as file:
        expected = file.read()
        assert generate_diff(file_1, file_2, format) == expected
