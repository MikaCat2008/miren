from miren_api import (
    DOMType, ElementType
)

from static.styles.styles import styles
from static.elements import elements


class Program:
    def start(self, dom: DOMType) -> None:
        elements.start(dom)

    def load_styles(self) -> dict[str, object]:
        return styles

    def load_elements(self) -> list[ElementType]:
        return elements.get_elements()
