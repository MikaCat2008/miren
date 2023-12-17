from typing import Callable
from collections import defaultdict

from ._types import AttributesType

from .styles import Styles


class Attributes(AttributesType):
    def __init__(self, attributes: dict[str, object]) -> None:
        self.styles = Styles()
        self.listeners = defaultdict(list)
        self.variables = {}
        
        for attr, value in (attributes or {}).items():
            if attr == "styles":
                self.styles.add_styles(value)
            elif isinstance(value, Callable):
                self.listeners[attr].append(value)
            else:
                self.variables[attr] = value

    def __getattr__(self, _: str) -> None:
        return None
