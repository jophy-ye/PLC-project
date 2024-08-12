"""
To run this PLCdb linter, install `pytest` and `pyyaml`.
Run `pytest linter.py` in cmd line.
"""

import yaml


FILENAME = 'PLCdb/pump-control.yaml'


def test_yaml():
    with open(FILENAME, 'r') as stream:
        yaml.safe_load(stream)