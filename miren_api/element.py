from __future__ import annotations

from ._types import DOMType, ElementType, StylesType

from .styles import get_styles as _get_styles
from .attributes import Attributes
from .dispatcher import Dispatcher


class Element(ElementType, Dispatcher):
    def __init__(
        self, 
        dom: DOMType,
        class_list: list[str] = None,
        elements: list[ElementType] = None,
        attributes: dict[str, object] = None
    ) -> None:
        super().__init__()

        self.dom = dom
        self.class_list = class_list or []
        self.elements = elements or []
        self.attributes = Attributes(attributes)

        self.styles = self.attributes.styles

        for event, listener in self.static_listeners.items():
            self.attributes.listeners[event].append(listener)

        for event, listeners in self.attributes.listeners.items():
            for listener in listeners:
                self.add_listener(event, listener)

        for attr, value in self.attributes.variables.items():
            setattr(self, attr, value)

        self.size = 0, 0
        self.position = 0, 0

        self.parent = None

    def add_element(self, element: ElementType) -> None:
        self.elements.append(element)

        element.parent = self

        return self
    
    def get_elements_by_class(self, _class: str) -> ElementType:
        elements = []

        for element in self.elements:
            elements += element.get_elements_by_class(_class)
        
        return elements

    def destroy(self) -> None:
        for element in self.elements:
            element.destroy()

        self.parent.elements.remove(self)
        self.dom.elements.remove(self)

    def get_styles(self) -> StylesType:
        return _get_styles(self)
