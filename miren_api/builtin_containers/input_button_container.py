from .text_container import TextContainer

from .._types import DOMType

from ..element import Element


class InputButtonContainer(Element):
    text: str

    def __init__(
        self,
        text_container: TextContainer,
        dom: DOMType,
        class_list: list[str] = None,
        attributes: dict[str, object] = None
    ) -> None:
        if class_list is None:
            class_list = []

        if "input_button_container" not in class_list:
            class_list = ["input_button_container"] + class_list

        if "input_container" not in class_list:
            class_list = ["input_container"] + class_list

        if "input_button_text_container" not in text_container.class_list:
            text_container.class_list = ["input_button_text_container"] + text_container.class_list

        if "input_text_container" not in text_container.class_list:
            text_container.class_list = ["input_text_container"] + text_container.class_list

        super().__init__(dom, class_list, [text_container], attributes)

        self.text = text_container.text
        self.text_container = text_container

    def set_text(self, text: str) -> None:
        self.text = text

        self.text_container.text = text
