from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Callable
from collections import defaultdict

from pygame.surface import SurfaceType


class ListenerType:
    listener: Callable


class DispatcherType(ABC):
    listeners: defaultdict[str, list[Callable]]

    @abstractmethod
    def add_listener(self, event: str, listener: Callable) -> None: ...

    @abstractmethod
    def emit(self, event: str) -> None: ...


class AttributesType(ABC):
    styles: StylesType
    listeners: defaultdict[list]
    variables: dict[str, object]


class StylesType(ABC):
    display: str
    position: str
    overflow: str

    width: int
    height: int

    margin_top: int
    margin_right: int
    margin_bottom: int
    margin_left: int

    left: int
    up: int

    font_size: int

    color: tuple[int, int, int]
    background_color: tuple[int, int, int]

    border: int
    border_color: tuple[int, int, int]

    z_index: int

    selectable: bool

    is_hovered: bool
    is_clicked: bool
    is_selected: bool
    is_mouse_in: bool

    @abstractmethod
    def add_styles(self, styles: dict[str, object]) -> None: ...

    @abstractmethod
    def get_styles(self) -> dict[str, object]: ...

    @abstractmethod
    def copy(self) -> StylesType: ...


class ElementType(DispatcherType, ABC):
    class_list: list[str]
    elements: list[ElementType]
    attribute: AttributesType

    styles: StylesType
    static_listeners: dict[str, Callable]

    size: tuple[int, int]
    position: tuple[int, int]
    absolute_position: tuple[int, int]
    parent: ElementType


class DOMType(ElementType, ABC):
    window: WindowType
    screen: SurfaceType

    ctrl: bool

    input_text: str
    input_index: int

    hovered_element: ElementType
    selected_element: ElementType


class WindowType(ABC):
    width: int
    height: int
    debug: bool

    screen: SurfaceType
    dom: DOMType

    @abstractmethod
    def run(self) -> None: ...
