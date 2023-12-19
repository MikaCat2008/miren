import miren_api as api
from miren_api import (
    container, input_field
)


def start(dom: api.DOMType) -> None:
    ...


def get_elements() -> list[api.ElementType]:
    return [
        input_field()
    ]
