"""Test stylish formatter (for tree structure)"""

import pytest
from gendiff_package.gendiff import GenerateDifference

FORMATTER = 'stylish.py'


@pytest.mark.asyncio
async def test_json(file_tree1_json_path, file_tree2_json_path, result_render):
    assert result_render == GenerateDifference.generate_diff(
                                                        file_tree1_json_path,
                                                        file_tree2_json_path)


@pytest.mark.asyncio
async def test_yml(file_tree1_yml_path, file_tree2_yml_path, result_render):
    assert result_render == GenerateDifference.generate_diff(
                                                        file_tree1_yml_path,
                                                        file_tree2_yml_path)
