from miren_api import (
    Window, DOM, 
    Container, TextContainer, 
    InputFieldContainer, InputButtonContainer
)

number = 0
temp_number = 0
mode = ""
number_field: InputFieldContainer = None


def start(dom: DOM) -> None:
    global number_field

    number_field = dom.get_elements_by_class("calc_field")[0]


def input(field: InputFieldContainer) -> None:
    global number
    
    try:
        number = int(field.text)
    except:
        ...

    field.set_text(str(number))


def click(button: InputButtonContainer) -> None:
    global number, temp_number, mode

    symbol = button.text

    if symbol.isdigit():
        number = int(str(number) + symbol)

    if symbol in "+-":
        if symbol == "+":
            mode = "+"

        if symbol == "-":
            mode = "-"

        temp_number = number
        number = 0

    if symbol == "=":
        if mode == "+":
            number = temp_number + number
        elif mode == "-":
            number = temp_number - number

        temp_number = 0

    if symbol == "C":
        number = 0
        temp_number = 0

    update_number_field()


def update_number_field() -> None:
    number_field.set_text(str(number))


def calc_button(text: str) -> InputButtonContainer:
    return InputButtonContainer(
        TextContainer(text, ["calc_button_text"]), 
        ["calc_button"], {"click": click}
    )


def main() -> None:
    dom.styles |= {
        "main_container": {
            "position": "absolute",

            "width": 300,
            "height": 375
        },

        "calc_field": {
            "width": 100,
            "height": 80
        },
        "calc_field_text": {
            "width": 100,
            "height": 80,

            "font_size": 48,

            "margin_top": 10
        },

        "calc_button": {
            "width": 75,
            "height": 75
        },
        "calc_button_text": {
            "width": 75,
            "height": 75,

            "margin_left": 23,
            "margin_top": 9,

            "font_size": 52
        },

        "row": {
            "width": 300,
            "height": 75,

            "display": "x"
        }
    }

    dom.add_element(
        Container(["main_container"], [
            InputFieldContainer(
                TextContainer("", ["calc_field_text"]),
                ["calc_field"], 
                {"input": input}
            ),
            Container(["row"], [
                calc_button("7"),
                calc_button("8"),
                calc_button("9"),
                calc_button("C")
            ]),Container(["row"], [
                calc_button("4"),
                calc_button("5"),
                calc_button("6"),
                calc_button("+")
            ]),
            Container(["row"], [
                calc_button("1"),
                calc_button("2"),
                calc_button("3"),
                calc_button("-")
            ]),
            Container(["row"], [
                calc_button(""),
                calc_button("0"),
                calc_button(""),
                calc_button("=")
            ])
        ])
    )

    dom.add_listener("start", start)

    window.run()


if __name__ == "__main__":
    window = Window(300, 375, debug=True)
    dom = window.dom

    main()
