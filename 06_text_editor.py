from icecream import ic
import flet as ft


# from flet import UserControl, TextField, InputBorder, Page, ControlEvent, app


class TextEditor(ft.UserControl):
    """
    Initializes a new instance of the class.

    Parameters:
        flet UserControl

    Returns:
        None
    """
    def __init__(self) -> None:
        super().__init__()
        self.textfield = ft.TextField(
            multiline=True,
            autofocus=True,
            border=ft.InputBorder.NONE,
            min_lines=40,
            on_change=self.save_text,
            content_padding=30,
            cursor_color='yellow'
        )

    def save_text(self, e: ft.ControlEvent) -> None:
        with open('save.txt', 'w') as f:
            f.write(self.textfield.value)

    def read_text(self) -> str | None:
        try:
            with open('save.txt', 'r') as f:
                return f.read()
        except FileNotFoundError:
            self.textfield.hint_text = 'Bem vindo ao editor de texto'

    def build(self) -> ft.TextField:
        self.textfield.value = self.read_text()
        return self.textfield


def main(page: ft.Page) -> None:
    page.title = 'Editor de Texto'
    page.scroll = True

    page.add(TextEditor())


if __name__ == '__main__':
    ft.app(target=main)
