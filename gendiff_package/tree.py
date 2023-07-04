"""Build internal tree view"""

class Tree:


    @classmethod
    def make_tree(cls, dictionary1: dict, dictionary2: dict) -> list:
        result = []
        all_keys = dictionary1.keys() | dictionary2.keys()

        for key in sorted(all_keys):
            child_1 = dictionary1.get(key)
            child_2 = dictionary2.get(key)

            if key not in dictionary1:
                result.append(
                    {
                        'key': key,
                        'type': 'added',
                        'value': child_2
                    }
                )
            elif key not in dictionary2:
                result.append(
                    {
                        'key': key,
                        'type': 'removed',
                        'value': child_1
                    }
                )
            elif isinstance(child_1, dict) and isinstance(child_2, dict):
                result.append({
                    'key': key,
                    'type': 'nested',
                    'children': cls.make_tree(child_1, child_2)})

            elif child_1 == child_2:
                result.append({
                    'key': key,
                    'type': 'unchanged',
                    'value': child_1})
            else:
                result.append({
                        'key': key,
                        'type': 'changed',
                        'old_value': child_1,
                        'new_value': child_2})
        return result


    @classmethod
    def build_tree(cls, dictionary1: dict, dictionary2: dict) -> dict:

        return \
            {
                'type': 'root',
                'children': cls.make_tree(dictionary1, dictionary2)
            }
