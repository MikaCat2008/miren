from __future__ import annotations


class E:
    def __init__(self, m: str, s: tuple[int, int], e: list[E]) -> None:
        self.m = m
        self.s = s
        self.e = e


def update(e: E, x: int = 0, y: int = 0, mx: int = 0, my: int = 0) -> tuple[int, int]:
    for _e in e.e:
        _mx, _my = update(_e, x, y, 0, 0)

        if e.m == "x":
            x += _mx + _e.s[0]
            my = max(my, _e.s[1])
        if e.m == "y":
            y += _my + _e.s[1]
            mx = max(mx, _e.s[0])

    return mx, my


update(
    E("y", (60, 60), [
        E("x", (60, 30), [
            E(None, (30, 30), []),
            E(None, (30, 30), [])
        ]),
        E("x", (60, 30), [
            E(None, (30, 30), []),
            E(None, (30, 30), [])
        ]),
    ])
)
