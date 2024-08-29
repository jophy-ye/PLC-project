"""
To run this PLCdb linter, install `pytest` and `pyyaml`.

Run `pytest linter.py` in cmd line.
The following packages are needed: `pyyaml`, `pytest`.
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
    INCLUDES = ('Name', 'Update', 'Input', 'Variable', 'Output', 'Rungs', 'VocabMap')
    # TODO: add 'CNF'
    for include in INCLUDES:
        assert include in keys
    assert 'Annotator' in keys or 'Author' in keys

@pytest.mark.parametrize("src_name", src_filenames)
def test_variables(load_file: dict):
    pass

@pytest.mark.parametrize("src_name", src_filenames)
def test_vocab_map(load_file: dict):
    with open('vocab.txt', 'r') as v:
        vocab_list = v.read().split()
    for vocab in vocab_list:
        assert type(vocab) is str and ' ' not in vocab
    for key, value in load_file['VocabMap'].items():
        assert value in vocab_list
