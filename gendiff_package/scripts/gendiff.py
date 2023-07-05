#!/usr/bin/env python
"""Difference Generator."""

from gendiff_package.gendiff import GenerateDifference
from gendiff_package.cli import parsing_args


def main():
    first_file, second_file, output_format = parsing_args()
    print(
        GenerateDifference.generate_diff(first_file, second_file, output_format)
    )


if __name__ == '__main__':
    main()
