from pygame import event
from pygame.display import flip, set_mode

from ._types import WindowType

from .dom import DOM


class Window(WindowType):
    def __init__(self, width: int, height: int, debug: bool = False) -> None:
        self.width = width
        self.height = height
        self.debug = debug

        self.screen = set_mode((self.width, self.height))
        self.dom = DOM(self)

    def run(self) -> None:
        self.dom.emit("start")

        while 1:
            self.screen.fill((255, 255, 255))

            events = event.get()

            self.dom.update(events)

            flip()
