import flet as ft
from flet import UserControl, Text, Row, Page, ControlEvent, MainAxisAlignment, ElevatedButton


class IncrementCounter(UserControl):
    def __init__(self, text: str, start_number: int = 0) -> None:
        super().__init__()
        self.text = text
        self.counter = start_number
        self.text_number: Text = Text(value=str(start_number), size=40)

    def increment(self, e: ControlEvent) -> None:
        self.counter += 1
        self.text_number.value = str(self.counter)
        self.update()

    def build(self) -> Row:
        return Row(controls=[ElevatedButton(self.text, on_click=self.increment), self.text_number],
                   alignment=MainAxisAlignment.SPACE_BETWEEN, width=300)


def main(page: Page) -> None:
    page.title = 'Reusable App'
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'

    page.add(IncrementCounter('People'))
    page.add(IncrementCounter('Animals', start_number=5))
    page.add(IncrementCounter('Items', start_number=1000))


if __name__ == '__main__':
    ft.app(target=main)
