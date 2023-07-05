class PlainFormat:
    """Plain module - apply plain view to diff"""

    @classmethod
    def __to_string(cls, value):
        if isinstance(value, dict):
            return '[complex value]'
        if isinstance(value, bool):
            return "true" if value else "false"
        if isinstance(value, int):
            return value
        if value is None:
            return "null"
        return f"'{value}'"

    @classmethod
    def __iter_(cls, node: dict, path="") -> str:
        children = node.get('children')
        current_path = f"{path}{node.get('key')}"

        if node['type'] == 'root':
            lines = map(lambda child: cls.__iter_(child, path), children)
            result = "\n".join(filter(bool, lines))
            return result

        if node['type'] == 'nested':
            lines = map(lambda child: cls.__iter_(child, f"{current_path}."), children)
            result = "\n".join(filter(bool, lines))
            return result

        if node['type'] == 'removed':
            return f"Property '{current_path}' was removed"

        if node['type'] == 'added':
            formatted_value = cls.__to_string(node.get('value'))
            return f"Property '{current_path}' was added " \
                   f"with value: {formatted_value}"

        if node['type'] == 'changed':
            formatted_old_value = cls.__to_string(node.get('old_value'))
            formatted_new_value = cls.__to_string(node.get('new_value'))
            return f"Property '{current_path}' was updated. " \
                   f"From {formatted_old_value} to {formatted_new_value}"

    @classmethod
    def format_(cls, node: dict):
        return cls.__iter_(node)
