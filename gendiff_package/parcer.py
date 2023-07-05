"""Parser module"""
import json
import yaml


class Parser:

    @staticmethod
    def parce(file_name, file_ex):
        if file_ex == '.json':
            return json.load(open(file_name))
        if file_ex in ('.yaml', '.yml'):
            return yaml.safe_load(open(file_name))

        raise ValueError('Unknown file format')
