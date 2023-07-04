"""fixtures"""


import pathlib
import asyncio
import aiofiles
import pytest


FIXTURES_FOLDER = 'fixtures'


@pytest.fixture(scope='module')
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope='session')
def file1_json_path():
    file_path = pathlib.Path(__file__).parent / FIXTURES_FOLDER / 'file1.json'
    return file_path


@pytest.fixture(scope='session')
def file2_json_path():
    file_path = pathlib.Path(__file__).parent / FIXTURES_FOLDER / 'file2.json'
    return file_path


@pytest.fixture(scope='session')
def file1_yml_path():
    file_path = pathlib.Path(__file__).parent / FIXTURES_FOLDER / 'file1.yml'
    return file_path


@pytest.fixture(scope='session')
def file2_yml_path():
    file_path = pathlib.Path(__file__).parent / FIXTURES_FOLDER / 'file2.yml'
    return file_path


@pytest.fixture(scope='session')
def file_tree1_json_path():
    file_path = pathlib.Path(__file__).parent / FIXTURES_FOLDER / 'file1_tree.json'
    return file_path



@pytest.fixture(scope='session')
def file_tree2_json_path():
    file_path = pathlib.Path(__file__).parent / FIXTURES_FOLDER / 'file2_tree.json'
    return file_path



@pytest.fixture(scope='session')
def file_tree1_yml_path():
    file_path = pathlib.Path(__file__).parent / FIXTURES_FOLDER / 'file1_tree.yml'
    return file_path



@pytest.fixture(scope='session')
def file_tree2_yml_path():
    file_path = pathlib.Path(__file__).parent / FIXTURES_FOLDER / 'file2_tree.yml'
    return file_path


@pytest.fixture(scope='function')
async def result_render(request):
    assert getattr(request.module, 'FORMATTER', None)
    result_path = pathlib.Path(__file__).parent / FIXTURES_FOLDER / request.module.FORMATTER

    async with aiofiles.open(result_path, mode='r') as file:
        content = await file.read()
    return content.replace('- wow:', '- wow: ')
