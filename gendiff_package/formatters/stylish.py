class Stylish:
    """Stylish module - apply stylish view to diff (by default)"""

    @classmethod
    def get_indent(cls, depth: int) -> str:
        return ' ' * (depth * 4 - 2)


    @classmethod
    def to_string(cls, value, depth: int) -> str:
        if isinstance(value, bool):
            return 'true' if value else 'false'

        if value is None:
            return 'null'

        if isinstance(value, dict):
            indent = cls.get_indent(depth)
            current_indent = indent + (" " * 6)
            lines = []
            for k, v in value.items():
                lines.append(f"{current_indent}{k}: {cls.to_string(v, depth + 1)}")
            result = "\n".join(lines)
            return f'{{\n{result}\n  {indent}}}'

        return value


    @classmethod
    def iter_(cls, node: dict, depth=0) -> str:
        children = node.get('children')
        indent = cls.get_indent(depth)
        formatted_value = cls.to_string(node.get('value'), depth)
        formatted_value1 = cls.to_string(node.get('old_value'), depth)
        formatted_value2 = cls.to_string(node.get('new_value'), depth)

        if node['type'] == 'root':
            lines = map(lambda child: cls.iter_(child, depth + 1), children)
            result = '\n'.join(lines)
            return f'{{\n{result}\n}}'

        if node['type'] == 'nested':
            lines = map(lambda child: cls.iter_(child, depth + 1), children)
            result = '\n'.join(lines)
            return f"{indent}  {node['key']}: {{\n{result}\n  {indent}}}"

        if node['type'] == 'changed':
            line1 = f"{indent}- {node['key']}: {formatted_value1}\n"
            line2 = f"{indent}+ {node['key']}: {formatted_value2}"
            result = line1 + line2
            return result

        if node['type'] == 'unchanged':
            return f"{indent}  {node['key']}: {formatted_value}"

        if node['type'] == 'removed':
            return f"{indent}- {node['key']}: {formatted_value}"

        if node['type'] == 'added':
            return f"{indent}+ {node['key']}: {formatted_value}"


    @classmethod
    def format_(cls, node: dict):
        return cls.iter_(node)
