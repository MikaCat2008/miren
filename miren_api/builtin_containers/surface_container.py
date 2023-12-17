from typing import Callable

from pygame.surface import Surface, SurfaceType

from .._types import DOMType

from ..element import Element


class SurfaceContainer(Element):
    surface: SurfaceType

    def __init__(
        self, 
        dom: DOMType,
        class_list: list[str] = None, 
        elements: list[Element] = None,
        attributes: dict[str, object] = None
    ) -> None:
        super().__init__(dom, class_list, elements, attributes)

        width, height = self.attributes.width or 0, self.attribute.height or 0

        self.surface = Surface((width, height))
