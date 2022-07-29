import os
import logging

from server.common.definitions import SERVICE_NAME

def get_spec_dir() -> str:
    return os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..', 'openapi'))


def get_spec_file() -> str:
    return f"{SERVICE_NAME}.yaml"


def get_spec_path() -> str:
    return os.path.join(get_spec_dir(), get_spec_file())


def append_headers(location: str) -> dict[str: str]:
    return {
        "Location": location
    }
