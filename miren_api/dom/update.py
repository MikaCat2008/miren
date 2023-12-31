from collections import defaultdict

import pygame
from pygame import mouse
from pygame.event import EventType

from .._types import DOMType

from ..draw import draw_layers
from ..update import update_element
from ..styles import get_styles
from ..builtin_containers import (
    InputFieldContainer, SurfaceContainer
)


def left_arrow(dom: DOMType) -> None:
    input_text = dom.selected_element.text
    
    if input_text:
        if dom.ctrl :
            splitted = input_text[:dom.input_index].split()
            
            if len(splitted) < 2:
                dom.input_index = 0

            else:
                *_, text = input_text[:dom.input_index].split()
                right_text = input_text[dom.input_index:]

                dom.input_index -= len(text)

                if right_text:
                    if right_text[0] != " ":
                        dom.input_index -= 1
                elif input_text[-1] == " ":
                    dom.input_index -= 1

        elif dom.input_index > 0:
            dom.input_index -= 1


def right_arrow(dom: DOMType) -> None:
    input_text = dom.selected_element.text
    
    if input_text:
        if dom.ctrl :
            splitted = input_text[dom.input_index:].split()
            
            if len(splitted) < 2:
                dom.input_index = len(input_text)

            else:
                text, *right_splitted_text = splitted
                left_text = input_text[:dom.input_index]

                dom.input_index += len(text)

                if left_text and left_text[-1] != " ":
                    dom.input_index += 1

        elif dom.input_index < len(input_text):
            dom.input_index += 1


def backslash(dom: DOMType) -> None:
    if not isinstance(dom.selected_element, InputFieldContainer):
        return 
    
    if not dom.input_text:
        return

    input_text = dom.selected_element.text

    if dom.ctrl:
        splitted = input_text[:dom.input_index].split()
        right_text = input_text[dom.input_index:]

        if len(splitted) < 2:
            text = right_text

            dom.input_index = 0
            
        else:
            *left_splitted_text, text = splitted
            
            dom.input_index -= len(text)

            if right_text:
                if right_text[0] != " ":
                    dom.input_index -= 1
            elif input_text[-1] == " ":
                dom.input_index -= 1

            text = " ".join(left_splitted_text) + " " + right_text

    elif dom.input_index > 0:
        text = input_text[:dom.input_index - 1] + input_text[dom.input_index:]

        dom.input_index -= 1

    else:
        text = input_text

    dom.input_text = text
    
    dom.selected_element.set_text(text)
    dom.selected_element.emit("input")



def delete(dom: DOMType) -> None:
    if not isinstance(dom.selected_element, InputFieldContainer):
        return

    if not dom.input_text:
        return
    
    input_text = dom.selected_element.text

    if dom.ctrl:
        splitted = input_text[dom.input_index:].split()
        left_text = input_text[:dom.input_index]

        if len(splitted) < 2:
            text = left_text

        else:
            text, *right_splitted_text = splitted
            left_text = input_text[:dom.input_index]

            text = left_text + " " + " ".join(right_splitted_text)

    else:
        text = input_text[:dom.input_index] + input_text[dom.input_index + 1:]

    dom.input_text = text
    
    dom.selected_element.set_text(text)
    dom.selected_element.emit("input")



def update(dom: DOMType, events: list[EventType]) -> None:
    layers = defaultdict(list[int])

    update_element(dom.container, layers)
    draw_layers(dom.screen, layers, dom.window.debug)

    mx, my = mouse.get_pos()
    m1, m2, m3 = mouse.get_pressed()

    hovered_element = None
    selected_element = None

    elements = dom.get_elements()

    for element in elements:
        styles = element.get_styles()

        if isinstance(element, SurfaceContainer):
            element.emit("update")

        ex, ey = element.position
        ew, eh = element.size

        is_mouse_in = element.styles.is_mouse_in
        is_clicked = element.styles.is_clicked

        if ex <= mx <= ex + ew and ey <= my <= ey + eh:
            if m1:
                if not is_clicked:
                    if selected_element is None and styles.selectable and not dom.is_clicked:
                        selected_element = element

                    element.styles.is_clicked = True
            elif is_clicked:
                element.styles.is_clicked = False

            if not is_mouse_in:
                if hovered_element is None and styles.selectable:
                    hovered_element = element

                element.styles.is_mouse_in = True
        elif is_mouse_in:
            element.styles.is_mouse_in = False

    if m1 and not dom.is_clicked:
        dom.is_clicked = True
    elif not m1 and dom.is_clicked:
        dom.is_clicked = False

    if hovered_element and hovered_element is not dom.hovered_element:
        if dom.hovered_element:
            dom.hovered_element.emit("mouse_out")
            dom.hovered_element.styles.is_hovered = False

        hovered_element.styles.is_hovered = True

        hovered_element.emit("mouse_in")

        dom.hovered_element = hovered_element

    if selected_element:
        if selected_element is not dom.selected_element:
            dom.unselect()

            dom.select(selected_element)

        ex, ey = selected_element.position

        selected_element.emit("click", **{
            "mx": mx,
            "my": my,
            "ex": mx - ex,
            "ey": my - ey
        })

    for event in events:
        if event.type == pygame.VIDEORESIZE:
            dom.window.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            dom.screen = dom.window.screen

        elif event.type == pygame.KEYDOWN:
            if not isinstance(dom.selected_element, InputFieldContainer):
                continue

            symbol = event.unicode

            if symbol == "\x1b":
                dom.unselect()

            elif event.key == 1073742048:
                dom.ctrl = True

            elif event.key == 1073741904:
                left_arrow(dom)

            elif event.key == 1073741903:
                right_arrow(dom)

            elif symbol == "\x08":
                backslash(dom)

            elif symbol == "\x7f":
                delete(dom)

            elif symbol == "\r":
                if not isinstance(dom.selected_element, InputFieldContainer):
                    continue
                
                dom.selected_element.emit("submit")

                dom.unselect()

            dom.pressed_time = 0
            dom.pressed_key = event.key
            dom.pressed_symbol = symbol

        if event.type == pygame.KEYUP:
            if event.key == 1073742048:
                dom.ctrl = False

            if (event.key == dom.pressed_key and dom.pressed_key) or \
                (event.unicode == dom.pressed_symbol and dom.pressed_symbol):
                dom.pressed_time = None
                dom.pressed_key = None
                dom.pressed_symbol = None

        if event.type == pygame.TEXTINPUT:
            symbol = event.text

            if not isinstance(dom.selected_element, InputFieldContainer):
                continue

            text = dom.selected_element.text
            text = text[:dom.input_index] + symbol + text[dom.input_index:]

            dom.input_text = text
            dom.input_index += 1

            dom.selected_element.set_text(text)
            dom.selected_element.emit("input")

            dom.is_input_line_show = True

    if dom.pressed_symbol or dom.pressed_key:
        dom.pressed_time += 1

        if max(1, dom.pressed_time - 1100) % 120 == 0:
            if isinstance(dom.selected_element, InputFieldContainer):
                key = dom.pressed_key
                symbol = dom.pressed_symbol

                if key == 1073741904:
                    left_arrow(dom)

                elif key == 1073741903:
                    right_arrow(dom)

                elif symbol == "\x08":
                    backslash(dom)

                elif symbol == "\x7f":
                    delete(dom)

                dom.is_input_line_show = True

    if dom.input_text is not None:
        dom.input_line_time += 1

        if dom.input_line_time % 1600 == 0:
            dom.is_input_line_show = not dom.is_input_line_show
