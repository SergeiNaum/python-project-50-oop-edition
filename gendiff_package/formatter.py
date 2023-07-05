"""Formatter module - formatting the tree with the selected formatter"""


from gendiff_package.formatters.formaters_cls import FormattersUnit


class Formatter:

    @staticmethod
    def formatting(tree: dict, format_name='stylish') -> str:
        formats = {
            'stylish': FormattersUnit.format_stylish,
            'json': FormattersUnit.format_json,
            'plain': FormattersUnit.format_plain,
        }
        if format_name in formats:
            return formats[format_name](tree)

        raise ValueError(f'Unknown format: {format_name}')
