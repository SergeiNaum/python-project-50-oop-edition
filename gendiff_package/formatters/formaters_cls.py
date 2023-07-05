from gendiff_package.formatters.stylish import Stylish
from gendiff_package.formatters.json import JsonFormat
from gendiff_package.formatters.plain import PlainFormat


class FormattersUnit:

    @staticmethod
    def format_stylish(tree):
        return Stylish.format_(tree)

    @staticmethod
    def format_json(tree):
        return JsonFormat.format_(tree)

    @staticmethod
    def format_plain(tree):
        return PlainFormat.format_(tree)
