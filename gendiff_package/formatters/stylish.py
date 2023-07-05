from colorama import Fore, Style


class Stylish:
    """Stylish module - apply stylish view to diff (by default)"""
    FORMAT_RENDER = None
    MINUS = f'{Fore.RED}\033[1m-\033[0m{Style.RESET_ALL}'
    PLUS = f'{Fore.GREEN}\033[1m+\033[0m{Style.RESET_ALL}'
    RED = Fore.LIGHTRED_EX
    WHITE = Fore.LIGHTWHITE_EX
    RESET = Style.RESET_ALL


    @classmethod
    def __get_indent(cls, depth: int) -> str:
        return ' ' * (depth * 4 - 2)

    @classmethod
    def __to_string(cls, value, depth: int) -> str:
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
                    f"{current_indent}{k}: {cls.__to_string(v, depth + 1)}"
                    )
            result = "\n".join(lines)
            return f'{{\n{result}\n  {indent}}}'

        return value

    @classmethod
    def __iter_(cls, node: dict, depth=0) -> str:
        children = node.get('children')
        indent = cls.__get_indent(depth)
        formatted_value = f"{cls.WHITE}{cls.__to_string(node.get('value'), depth)}{cls.RESET}"
        formatted_value1 = f"{cls.WHITE}{cls.__to_string(node.get('old_value'), depth)}{cls.RESET}"
        formatted_value2 = f"{cls.WHITE}{cls.__to_string(node.get('new_value'), depth)}{cls.RESET}"

        if node['type'] == 'root':
            lines = map(lambda child: cls.__iter_(child, depth + 1), children)
            result = '\n'.join(lines)
            return f'{{\n{result}\n}}'

        if node['type'] == 'nested':
            lines = map(lambda child: cls.__iter_(child, depth + 1), children)
            result = '\n'.join(lines)
            return f"{indent}  {cls.WHITE}{node['key']}{cls.RESET}: : {{\n{result}\n  {indent}}}"

        if node['type'] == 'changed':
            line1 = f"{indent}{cls.MINUS} {cls.WHITE}{node['key']}{cls.RESET}: {formatted_value1}\n"
            line2 = f"{indent}{cls.PLUS} {cls.WHITE}{node['key']}{cls.RESET}: : {formatted_value2}"
            result = line1 + line2
            return result

        if node['type'] == 'unchanged':
            return f"{indent}  {cls.WHITE}{node['key']}{cls.RESET}: {formatted_value}"

        if node['type'] == 'removed':
            return f"{indent}{cls.MINUS} {cls.WHITE}{node['key']}{cls.RESET}: : {formatted_value}"

        if node['type'] == 'added':
            return f"{indent}{cls.PLUS} {cls.WHITE}{node['key']}{cls.RESET}: : {formatted_value}"

    @classmethod
    def format_(cls, node: dict):
        cls.FORMAT_RENDER = cls.__iter_(node)
        return cls.FORMAT_RENDER

    def __str__(self):
        return f'{self.FORMAT_RENDER}'
