"""
To run this PLCdb linter, install `pytest` and `pyyaml`.
Run `pytest linter.py` in cmd line.
"""

import os
import logging

import pytest
import yaml


src_filenames = os.listdir(os.path.dirname(__file__))
src_filenames = list(filter(lambda name: name.endswith('.yaml'), src_filenames))


@pytest.fixture
def load_file(src_name):
    with open(src_name, 'r') as stream:
        return yaml.safe_load(stream)

@pytest.mark.parametrize("src_name", src_filenames)
def test_yaml(load_file):
    assert isinstance(load_file, dict)

@pytest.mark.parametrize("src_name", src_filenames)
def test_structure(load_file: dict):
    keys = load_file.keys()
    INCLUDES = ('Name', 'Update', 'Input', 'Variable', 'Output', 'Rungs')
    # TODO: add 'CNF'
    for include in INCLUDES:
        assert include in keys
    assert 'Annotator' in keys or 'Author' in keys

@pytest.mark.parametrize("src_name", src_filenames)
def test_variables(load_file: dict):
    pass