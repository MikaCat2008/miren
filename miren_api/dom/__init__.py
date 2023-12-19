from pygame.event import EventType

from .._types import DOMType, WindowType, ElementType

from .update import update as update_dom

from ..element import Element
from ..default_styles import default_styles
from ..builtin_containers import Container, InputFieldContainer

dom: DOMType = None


def get_dom() -> DOMType:
    return dom


class DOM(DOMType, Element):
    def __init__(self, window: WindowType) -> None:
        global dom

        super().__init__(None)

        dom = self

        self.window = window
        self.screen = window.screen

        self.elements = []
        self.styles = default_styles
        self.container = Container(self)

        self.ctrl = False
        self.is_clicked = False

        self.pressed_time = None
        self.pressed_key = None
        self.pressed_symbol = None
        
        self.input_text = None
        self.input_index = 0

        self.hovered_element = None
        self.selected_element = None

        self.container.styles.width = self.screen.get_width()
        self.container.styles.height = self.screen.get_height()

    def add_element(self, element: ElementType, child_add = False) -> ElementType:
        self.elements.append(element)

        element.parent = self

        if element.elements:
            for _element in element.elements:
                self.add_element(_element, True)

                _element.parent = element
        
        if not child_add:
            return self.container.add_element(element)
        return self

    def get_elements_by_class(self, _class: str) -> ElementType:
        return [element for element in self.elements if _class in element.class_list]

    def get_elements(self, element: ElementType = None) -> list[ElementType]:
        elements = []

        if element is None:
            element = self.container
        
        for _element in element.elements:
            if _element.elements:
                elements += self.get_elements(_element)
            elements.append(_element)

        return elements
    
    def select(self, element: ElementType) -> None:
        if isinstance(element, InputFieldContainer):
            self.input_text = element.text
            self.input_index = 0

        element.styles.is_selected = True

        element.emit("select")
        element.emit("click")

        self.selected_element = element

    def unselect(self) -> None:
        self.input_text = None
        self.input_index = 0

        selected_element = self.selected_element

        if selected_element:
            selected_element.styles.is_selected = False
            self.selected_element = None

            selected_element.emit("unselect")

    def update(self, events: list[EventType]) -> None:
        update_dom(self, events)
