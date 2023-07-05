"""Generate Diff - main module"""


import pathlib
from gendiff_package.parcer import Parser
from gendiff_package.tree import Tree
from gendiff_package.formatter import Formatter


class GenerateDifference:

    @staticmethod
    def get_file_ex(file_path: str) -> str:
        """Get file extension from file path."""
        file = pathlib.Path(file_path)
        extension = file.suffix

        return extension

    @staticmethod
    def get_f_data(file_path: str) -> str:
        """Get data from file."""
        extension = GenerateDifference.get_file_ex(file_path)
        data = Parser.parce(file_path, extension)

        return data

    @staticmethod
    def generate_diff(file_path1: str,
                      file_path2: str,
                      format='stylish') -> str:

        dictionary1 = dict(GenerateDifference.get_f_data(file_path1))
        dictionary2 = dict(GenerateDifference.get_f_data(file_path2))
        tree = Tree.build_tree(dictionary1, dictionary2)
        diff = Formatter.formatting(tree, format)

        return diff
