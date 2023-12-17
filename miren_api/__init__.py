from __future__ import annotations

from pygame import init

from ._types import DOMType, ElementType

from .dom import get_dom, DOM
from .window import Window
from .builtin_containers import *


def container(
    class_list: list[str] = None, 
    elements: list[ElementType] = None, 
    attributes: dict[str, object] = None
) -> Container:
    return Container(
        get_dom(), class_list, elements, attributes
    )    


def text_container(
    text: str = "",
    class_list: list[str] = None, 
    attributes: dict[str, object] = None
) -> TextContainer:
    return TextContainer(
        text, get_dom(), class_list, attributes
    )    


def input_field_container(
    text_container: TextContainer = None,
    class_list: list[str] = None, 
    attributes: dict[str, object] = None
) -> InputFieldContainer:
    return InputFieldContainer(
        text_container, get_dom(), class_list, attributes
    )


def input_field(
    class_list: list[str] = None,
    attributes: dict[str, object] = None
) -> None:
    return input_field_container(
        text_container(), class_list, attributes
    )


def input_button_container(
    text_container: TextContainer = None,
    class_list: list[str] = None, 
    attributes: dict[str, object] = None
) -> InputButtonContainer:
    return InputButtonContainer(
        text_container, get_dom(), class_list, attributes
    )


init()
