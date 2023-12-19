from __future__ import annotations

from ._types import DOMType, StylesType, ElementType


def get_default_styles(dom: DOMType, _class: str) -> dict[str, object]:
    return dom.styles.get(_class, {})


def get_styles(element: ElementType) -> StylesType:
    dom = element.dom
    styles = Styles()

    for _class in element.class_list:
        default_styles = get_default_styles(dom, _class)
        
        modification = ""
        modification_styles = {}

        if element.styles.is_hovered:
            modification = _class + ":hover"
        elif element.styles.is_selected:
            modification = _class + ":select"
        
        if modification:
            modification_styles = get_default_styles(dom, modification)

        styles.add_styles(default_styles | modification_styles)

    styles.add_styles(element.styles.copy().get_styles())

    return styles


class Styles(StylesType):
    display = "y"
    position = "normal"
    overflow = "normal"

    width = 0
    height = 0

    margin_top = 0
    margin_right = 0
    margin_bottom = 0
    margin_left = 0

    left = 0
    up = 0

    font_size = 16

    color = 0, 0, 0
    background_color = None

    border = 0
    border_color = 0, 0, 0

    z_index = 0

    selectable = True

    is_hovered = False
    is_clicked = False
    is_selected = False
    is_mouse_in = False

    def __init__(self, styles: dict[str, object] = None) -> None:
        if styles is None:
            return

        for style, value in styles.items():
            setattr(self, style, value)

    def add_styles(self, styles: dict[str, object]) -> None:
        for style, value in styles.items():
            setattr(self, style, value)

    def get_styles(self) -> dict[str, object]:
        return self.__dict__

    def copy(self) -> StylesType:
        return Styles(self.get_styles())

    def __repr__(self) -> str:
        return str(self.get_styles())
