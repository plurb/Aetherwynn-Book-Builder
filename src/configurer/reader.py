import yaml

from typing import TextIO


def load_build_config_file(config_file: TextIO) -> dict:
    data: dict = yaml.load(config_file, Loader=yaml.CLoader)

    if 'schema' not in data.keys():
        raise TypeError('No schema defined')

    return data
