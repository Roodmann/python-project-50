#!/usr/bin/env python
from gendiff import generate_diff, parse_args


def main():
    file_one, file_two, format_name = parse_args()
    print(generate_diff(file_one, file_two, format_name))


if __name__ == '__main__':
    main()
