from miren_api import Window

from program import Program


if __name__ == "__main__":
    window = Window(300, 375)
    dom = window.dom

    program = Program()

    dom.styles |= program.load_styles()
    for element in program.load_elements():
        dom.add_element(element)

    dom.listeners["start"].append(lambda dom: program.start(dom))

    window.run()
