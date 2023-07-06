

from gendiff_package.formatters.main_formatters import Formatter


class Stylish(Formatter):
    """Stylish module - apply stylish view to diff (by default)"""
    FORMAT_RENDER = None

    @classmethod
    def __get_indent(cls, depth: int) -> str:
        return ' ' * (depth * 4 - 2)

    @classmethod
    def to_string(cls, value, depth: int) -> str:
        if isinstance(value, bool):
            return 'true' if value else 'false'

        if value is None:
            return 'null'

        if isinstance(value, dict):
            indent = cls.__get_indent(depth)
            current_indent = indent + (" " * 6)
            lines = []
            for k, v in value.items():
                lines.append(
                    f"{current_indent}{k}: {cls.to_string(v, depth + 1)}"
                    )
            result = "\n".join(lines)
            return f'{{\n{result}\n  {indent}}}'

        return value



    @classmethod
    def iter_(cls, node: dict, depth=0) -> str:
        children = node.get('children')
        indent = cls.__get_indent(depth)
        MINUS = cls.colored_string('-', cls.RED)
        PLUS = cls.colored_string('+', cls.GREEN)
        key = cls.colored_string(node.get('key'), cls.WHITE)
        formatted_value = cls.colored_formated_str(node.get('value'), depth)
        formatted_value1 = cls.colored_formated_str(node.get('old_value'), depth)
        formatted_value2 = cls.colored_formated_str(node.get('new_value'), depth)


        formatted_values = {
            'root': lambda: f'{{\n{"".join(map(lambda child: cls.iter_(child, depth + 1), children))}\n}}',
            'nested': lambda: '{}  {}:  {{{}\n{}}}'.format(indent, key, "".join(map(lambda child: "\n{}".format(cls.iter_(child, depth + 1)).rstrip(), children)), indent),
            'changed': lambda: f'{indent}{MINUS} {key}: {formatted_value1}\n{indent}{PLUS} {key}:  {formatted_value2}',
            'unchanged': lambda: f'{indent}  {key}: {formatted_value}',
            'removed': lambda: f'{indent}{MINUS} {key}:  {formatted_value}',
            'added': lambda: f'{indent}{PLUS} {key}:  {formatted_value}',
        }
        return formatted_values[node['type']]()

    @classmethod
    def format_(cls, node: dict):
        cls.FORMAT_RENDER = cls.iter_(node)
        return cls.FORMAT_RENDER

    def __str__(cls):
        return f'{cls.FORMAT_RENDER}'
