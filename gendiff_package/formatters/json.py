import json


class JsonFormat:
    """JSON module - apply JSON view to diff"""

    @classmethod
    def format_(cls, tree: list) -> json:
        return json.dumps(tree, indent=4)
