from pygame.event import EventType

from .._types import DOMType, WindowType

from .update import update as update_dom

from ..element import Element
from ..default_styles import default_styles
from ..builtin_containers import Container


class DOM(DOMType, Element):
    def __init__(self, window: WindowType) -> None:
        super().__init__()

        self.window = window
        self.screen = window.screen

        self.elements = []
        self.styles = default_styles
        self.container = Container()

        self.ctrl = False
        
        self.input_text = ""
        self.input_index = 0

        self.hovered_element = None
        self.selected_element = None

        self.container.styles.width = self.screen.get_width()
        self.container.styles.height = self.screen.get_height()

    def add_element(self, element: Element, child_add = False) -> Element:
        self.elements.append(element)

        element.parent = self

        if element.elements:
            for _element in element.elements:
                self.add_element(_element, True)

                _element.parent = element
        
        if not child_add:
            return self.container.add_element(element)
        return self

    def get_elements_by_class(self, _class: str) -> Element:
        return [element for element in self.elements if _class in element.class_list]

    def get_elements(self, element: Element = None) -> list[Element]:
        elements = []

        if element is None:
            element = self.container
        
        for _element in element.elements:
            if _element.elements:
                elements += self.get_elements(_element)
            elements.append(_element)

        return elements

    def update(self, events: list[EventType]) -> None:
        update_dom(self, events)
