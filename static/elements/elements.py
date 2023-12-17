import miren_api as api
from miren_api import (
    container, input_field
)


def start(dom: api.DOMType) -> None:
    ...


def destroy(element: api.ElementType) -> None:
    element.destroy()


def get_elements() -> list[api.ElementType]:
    return [
        container(["red", "container"], [], {"click": destroy}),
        container(["green", "container"], [], {"click": destroy}),
        container(["red", "container"], [], {"click": destroy}),
        container(["green", "container"], [], {"click": destroy}),
        container(["red", "container"], [], {"click": destroy}),
        container(["green", "container"], [], {"click": destroy}),
        container(["red", "container"], [], {"click": destroy}),
        container(["green", "container"], [], {"click": destroy}),
        container(["red", "container"], [], {"click": destroy}),
        container(["green", "container"], [], {"click": destroy}),
        container(["red", "container"], [], {"click": destroy}),
        container(["green", "container"], [], {"click": destroy}),
        container(["red", "container"], [], {"click": destroy}),
        container(["green", "container"], [], {"click": destroy}),
        container(["red", "container"], [], {"click": destroy}),
        container(["green", "container"], [], {"click": destroy}),
        container(["red", "container"], [], {"click": destroy}),
        container(["green", "container"], [], {"click": destroy}),
        container(["red", "container"], [], {"click": destroy}),
        container(["green", "container"], [], {"click": destroy}),
        container(["red", "container"], [], {"click": destroy}),
        container(["green", "container"], [], {"click": destroy}),
        container(["red", "container"], [], {"click": destroy}),
        container(["green", "container"], [], {"click": destroy}),
        container(["red", "container"], [], {"click": destroy}),
        container(["green", "container"], [], {"click": destroy}),
        container(["red", "container"], [], {"click": destroy}),
        container(["green", "container"], [], {"click": destroy}),
        container(["red", "container"], [], {"click": destroy}),
        container(["green", "container"], [], {"click": destroy})
    ]
