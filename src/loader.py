from pathlib import Path

import yaml


def load_yaml(path: str | Path) -> dict:
    with open(path) as file:
        data = yaml.safe_load(file)
    return data or {}
