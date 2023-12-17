from typing import Callable
from ..element import Element

from pygame.surface import Surface, SurfaceType


class SurfaceContainer(Element):
    surface: SurfaceType

    def __init__(
        self, 
        class_list: list[str] = None, 
        elements: list[Element] = None,
        attributes: dict[str, object] = None
    ) -> None:
        super().__init__(class_list, elements, attributes)

        width, height = self.attributes.width or 0, self.attribute.height or 0

        self.surface = Surface((width, height))
