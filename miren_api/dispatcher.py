from typing import Callable
from collections import defaultdict

from ._types import ListenerType, DispatcherType


class Listener(ListenerType):
    def __init__(self, listener: Callable) -> None:
        self.listener = listener


class Dispatcher(DispatcherType):
    def __init_subclass__(cls) -> None:
        cls.static_listeners = {
            k: v.listener 
            for k, v in cls.__dict__.items() if isinstance(v, Listener)
        }

    def __init__(self) -> None:
        self.listeners = defaultdict(list)

    def add_listener(self, event: str, listener: Callable) -> None:
        self.listeners[event].append(listener)

    def emit(self, event: str) -> None:
        listeners = self.listeners[event]

        for listener in listeners:
            listener(self)
