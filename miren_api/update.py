from collections import defaultdict

from ._types import DOMType, ElementType


def update_xy(
    position: str, display: str,
    x: int, y: int, 
    max_x: int, max_y: int,
    child_max_x: int, child_max_y: int,
    width: int, height: int,
    offset_x: int, 
    offset_y: int
) -> tuple[int, int, int, int]:
    if position == "normal":
        if display == "x":
            x += max(child_max_x, width) + offset_x
            max_y = max(max_y, height)
        elif display == "y":
            y += max(child_max_y, height) + offset_y
            max_x = max(max_x, width)

    return x, y, max_x, max_y


def update_element(
    element: ElementType,
    layers: defaultdict[int, list[ElementType]],
    max_position: tuple[int, int] = (0, 0),
    parent_display: str = "y"
) -> tuple[int, int]:
    dom = element.dom
    x, y = element.position
    max_x, max_y = max_position

    for child_element in element.elements:
        styles = child_element.get_styles()

        display = styles.display
        position_type = styles.position

        width = styles.width
        height = styles.height

        left, up = styles.left, styles.up

        margin_left, margin_right = styles.margin_left, styles.margin_right
        margin_top, margin_bottom = styles.margin_top, styles.margin_bottom

        child_element.size = width, height
        child_element.position = x + left + margin_left, y + up + margin_top
        child_element.absolute_position = x + left, y + up

        layers[styles.z_index].append(child_element)

        child_max_x, child_max_y = update_element(
            child_element,
            layers, 
            (0, 0), 
            display
        )

        x, y, max_x, max_y = update_xy(
            position_type, parent_display,
            x, y,
            max_x, max_y,
            child_max_x, child_max_y,
            width, height,
            margin_right + margin_left,
            margin_bottom + margin_top
        )

    return max_x, max_y
