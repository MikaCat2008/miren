from __future__ import annotations

from typing import Callable

from ._types import ElementType

from .styles import Styles
from .attributes import Attributes
from .dispatcher import Dispatcher


class Element(ElementType, Dispatcher):
    def __init__(
        self, 
        class_list: list[str] = None,
        elements: list[ElementType] = None,
        attributes: dict[str, object] = None
    ) -> None:
        super().__init__()

        self.class_list = class_list or []
        self.elements = elements or []
        self.attributes = Attributes(attributes)

        self.styles = self.attributes.styles

        for event, listeners in (self.static_listeners | (self.attributes.listeners or {})).items():
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
