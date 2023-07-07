from gendiff_package.formatters.main_formatters import Formatter


class PlainFormat(Formatter):
    """Plain module - apply plain view to diff"""

    @classmethod
    def to_string(cls, value, depth=0):
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
    def iter_(cls, node: dict, path="", depth=0) -> str:
        children = node.get('children')
        key = cls.colored_string(node.get('key'), cls.WHITE)
        current_path = f"{path}{key}"
        removed = cls.colored_string('removed', cls.RED)
        added = cls.colored_string('added', cls.GREEN)
        changed = cls.colored_string('updated', cls.GREEN)
        unchanged = cls.colored_string('unchanged', cls.MAGENTA)
        property = cls.colored_string('Property', cls.WHITE)
        with_value = cls.colored_string('with value:', cls.WHITE)
        was = cls.colored_string('was', cls.WHITE)
        from_ = cls.colored_string('From', cls.WHITE)
        formatted_value = cls.colored_formated_str(node.get('value'))
        formatted_old_value = cls.colored_formated_str(node.get('old_value'), color=cls.RED)  # noqa: E501
        formatted_new_value = cls.colored_formated_str(node.get('new_value'), color=cls.GREEN)  # noqa: E501

        formatted_values = {
            'root': lambda: "\n".join(filter(bool, map(lambda child: cls.iter_(child, path), children))),  # noqa: E501
            'nested': lambda: "\n".join(
                filter(bool, map(lambda child: cls.iter_(child, f"{current_path}."), children))),  # noqa: E501
            'removed': lambda: f"{property} '{current_path}' {was} {removed}",  # noqa: E501
            'added': lambda: f"{property} '{current_path}' {was} {added} {with_value} {formatted_value}",  # noqa: E501
            'changed': lambda: f"{property} '{current_path}' {was} {changed}. {from_} {formatted_old_value} to {formatted_new_value}",  # noqa: E501
            'unchanged': lambda: f"{property} '{current_path}' {unchanged}."  # noqa: E501
        }

        return formatted_values[node['type']]()

    @classmethod
    def format_(cls, node: dict):
        return cls.iter_(node)
