from .._types import DOMType

from ..element import Element


class TextContainer(Element):
    text: str

    def __init__(
        self, 
        text: str,
        dom: DOMType,
        class_list: list[str] = None, 
        attributes: dict[str, object] = None
    ) -> None:
        super().__init__(dom, class_list, None, attributes)

        self.text = text
