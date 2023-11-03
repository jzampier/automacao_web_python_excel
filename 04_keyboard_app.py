import flet as ft
from flet import Page, Row, Text, KeyboardEvent
from icecream import ic


def main(page: Page) -> None:
    page.title = "KB App"
    page.spacing = 30
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'

    # Criar os elementos de visualização de texto
    key: Text = Text('Key', size=30)
    shift: Text = Text('Shift', size=30, color='red')
    ctrl: Text = Text('Control', size=30, color='blue')
    alt: Text = Text('Alt', size=30, color='green')
    meta: Text = Text('Meta', size=30, color='yellow')

    # Lidar com os eventos de teclado
    def on_keyboard(e: KeyboardEvent) -> None:
        key.value = e.key
        shift.visible = e.shift
        ctrl.visible = e.ctrl
        alt.visible = e.alt
        meta.visible = e.meta
        ic(e.data)
        page.update()

    # Linkar os eventos de teclado com a página
    page.on_keyboard_event = on_keyboard

    # Adicionar os elementos a página
    page.add(
        Text('Pressione qualquer combinação de teclas...'),
        Row(controls=[shift, ctrl, alt, meta, key],
            alignment=ft.MainAxisAlignment.CENTER)
    )


if __name__ == '__main__':
    ft.app(target=main)
