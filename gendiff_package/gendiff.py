"""Generate Diff - main module"""


import pathlib
from gendiff_package.parcer import Parser
from gendiff_package.tree import Tree
from gendiff_package.formatter import Formatter


class GenerateDifference:


    @classmethod
    def get_file_ex(self, file_path: str) -> str:
        """Get file extension from file path."""
        file = pathlib.Path(file_path)
        extension = file.suffix

        return extension


    @classmethod
    def get_f_data(self, file_path: str) -> str:
        """Get data from file."""
        extension = self.get_file_ex(file_path)
        data = Parser.parce(file_path, extension)

        return data


    def generate_diff(self, file_path1: str,
                      file_path2: str,
                      format='stylish') -> str:

        dictionary1 = dict(self.get_f_data(file_path1))
        dictionary2 = dict(self.get_f_data(file_path2))
        tree = Tree.build_tree(dictionary1, dictionary2)
        diff = Formatter.formatting(tree, format)

        return diff
