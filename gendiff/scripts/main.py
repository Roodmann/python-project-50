#!/usr/bin/env python
from gendiff import generate_diff, arg_parser


def main():
    file_one, file_two, format_name = arg_parser()
    print(generate_diff(file_one, file_two, format_name))


if __name__ == '__main__':
    main()
