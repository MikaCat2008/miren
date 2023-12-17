from ..element import Element


def container_to_str(element: Element, deep: int = 1) -> str:
    name = element.__class__.__name__
    class_list = " class=\"" + " ".join(element.class_list) + "\"" if element.class_list else ""
    _styles = element.styles.get_styles()
    styles = f" styles=\"{" ".join(
        f"{k}={v};" 
        for k, v in _styles.items()
    )}\"" if _styles else ""
    inner = (f"\n{"    " * deep}" + f"\n{"    " * deep}".join(
        container_to_str(_element, deep + 1) if isinstance(_element, Container) else repr(_element)
        for _element in element.elements
    ) + f"\n{"    " * (deep - 1)}") if element.elements else ""

    return f"<{name}{class_list}{styles}>{inner}</{name}>"


class Container(Element):
    def __repr__(self) -> str:
        return container_to_str(self)
