from typing import Callable
from ..element import Element


class TextContainer(Element):
    text: str

    def __init__(
        self, 
        text: str = "",
        class_list: list[str] = None, 
        attributes: dict[str, object] = None
    ) -> None:
        super().__init__(class_list, None, attributes)

        self.text = text
