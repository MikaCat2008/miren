from collections import defaultdict

from pygame import font, draw
from pygame.surface import SurfaceType

from ._types import DOMType, ElementType, StylesType

from .styles import get_styles
from .builtin_containers import (
    TextContainer, SurfaceContainer, InputFieldContainer
)

font.init()

loaded_fonts = {}


def get_font(size: int) -> font.FontType:
    if size in loaded_fonts:
        return loaded_fonts[size]

    _font = font.SysFont("arial", size)
    loaded_fonts[size] = _font
    return _font


def draw_element(
    element: ElementType,
    screen: SurfaceType,
    debug: bool = False
) -> None:
    dom = element.dom
    styles = element.get_styles()
    width, height = element.size

    background_color = styles.background_color

    border = styles.border
    border_color = styles.border_color

    if background_color:
        draw.rect(screen, background_color, (*element.position, width, height), 0)
    if border:
        draw.rect(screen, border_color, (*element.position, width, height), border)

    if isinstance(element, TextContainer):
        font_size = styles.font_size
        color = styles.color

        _font = get_font(font_size)
        rendered = _font.render(element.text, 1, color)

        parent = element.parent
        overflow = parent.get_styles().overflow

        element_x, element_y = element.position

        input_rendered = _font.render(element.text[:dom.input_index], 1, color)
        line_x, _ = input_rendered.get_size()  

        if overflow == "normal":
            screen.blit(rendered, element.position)
        
        elif overflow == "hidden":
            element_width, element_height = element.size
            parent_width, parent_height = parent.size
            parent_x, parent_y = parent.position

            width = min(parent_width, element_width)

            screen.blit(
                rendered, 
                (element_x, element_y), 
                (max(0, line_x - width + styles.margin_right), 0, width - element_x + parent_x, parent_height - element_y + parent_y)
            ) 

        if dom.is_input_line_show and isinstance(parent, InputFieldContainer) and parent.styles.is_selected:
            draw.line(
                screen, 
                (0, 0, 0), 
                (element_x - max(0, line_x - width + styles.margin_right) + line_x, element_y), 
                (element_x - max(0, line_x - width + styles.margin_right) + line_x, element_y + font_size)
            )


    elif isinstance(element, SurfaceContainer):
        screen.blit(element.surface, element.position)

    if debug:
        if element.styles.is_hovered:
            draw.rect(screen, (0, 255, 0), (*element.position, width, height), 1)
        elif element.styles.is_selected:
            draw.rect(screen, (255, 0, 0), (*element.position, width, height), 1)


def draw_layer(
    screen: SurfaceType,
    layer: list[ElementType],
    debug: bool = False
) -> None:
    for element in layer:
        draw_element(element, screen, debug)


def draw_layers(
    screen: SurfaceType, 
    layers: defaultdict[int, list[ElementType]],
    debug: bool = False
) -> None:
    sorted_layers = sorted(layers.items(), key=lambda x: x[0])

    for _, layer in sorted_layers:
        draw_layer(screen, layer, debug)
