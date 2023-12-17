from typing import Callable
from ..element import Element
# from ..dispatcher import Listener

from .text_container import TextContainer


class InputFieldContainer(Element):
    text: str

    def __init__(
        self,
        text_container: TextContainer,
        class_list: list[str] = None, 
        attributes: dict[str, object] = None
    ) -> None:
        if class_list is None:
            class_list = []
            
        if "input_field_container" not in class_list:
            class_list = ["input_field_container"] + class_list

        if "input_container" not in class_list:
            class_list = ["input_container"] + class_list

        if "input_field_text_container" not in text_container.class_list:
            text_container.class_list = ["input_field_text_container"] + text_container.class_list

        if "input_text_container" not in text_container.class_list:
            text_container.class_list = ["input_text_container"] + text_container.class_list

        super().__init__(class_list, [text_container], attributes)

        self.text = text_container.text
        self.text_container = text_container

    def set_text(self, text: str) -> None:
        self.text = text

        self.text_container.text = text
