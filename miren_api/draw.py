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
    dom: DOMType,
    screen: SurfaceType,
    element: ElementType,
    styles: StylesType,
    debug: bool = False
) -> None:
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
        overflow = get_styles(dom, element.parent).overflow

        element_x, element_y = element.position

        if overflow == "normal":
            screen.blit(rendered, element.position)
        
        elif overflow == "hidden":
            parent_width, parent_height = parent.size
            parent_x, parent_y = parent.position

            screen.blit(
                rendered, 
                (element_x, element_y), 
                (0, 0, parent_width - element_x + parent_x, parent_height - element_y + parent_y)
            )
        

        if isinstance(parent, InputFieldContainer) and parent.styles.is_selected:
            input_rendered = _font.render(element.text[:dom.input_index], 1, color)
            input_rendered_x, _ = input_rendered.get_size()

            draw.line(
                screen, 
                (0, 0, 0), 
                (element_x + input_rendered_x, element_y), 
                (element_x + input_rendered_x, element_y + font_size)
            )    


    elif isinstance(element, SurfaceContainer):
        screen.blit(element.surface, element.position)

    if debug:
        if element.styles.is_hovered:
            draw.rect(screen, (0, 255, 0), (*element.position, width, height), 1)
        elif element.styles.is_selected:
            draw.rect(screen, (255, 0, 0), (*element.position, width, height), 1)


def draw_layer(
    dom: DOMType,
    screen: SurfaceType,
    layer: list[ElementType],
    debug: bool = False
) -> None:
    for element in layer:
        styles = get_styles(dom, element)

        draw_element(dom, screen, element, styles, debug)


def draw_layers(
    dom: DOMType,
    screen: SurfaceType, 
    layers: defaultdict[int, list[ElementType]],
    debug: bool = False
) -> None:
    sorted_layers = sorted(layers.items(), key=lambda x: x[0])

    for _, layer in sorted_layers:
        draw_layer(dom, screen, layer, debug)
