#!/usr/bin/env python

import argparse
from gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration'
                    'files and shows a difference.'
                    )
    # Positional arguments
    parser.add_argument("first_file", type=str,
                        help="Absolute path to your file"
                        )
    parser.add_argument("second_file", type=str,
                        help="Absolute path to your file"
                        )

    # Optional arguments
    parser.add_argument('-f', '--format',
                        help='set format of output',
                        default="stylish"
                        )
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
