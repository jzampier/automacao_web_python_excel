import flet as ft
from flet import TextField, Checkbox, ElevatedButton, Text, Row, Column
from flet_core.control_event import ControlEvent


def main(page: ft.Page) -> None:
    # Page basic setup
    page.title = "Login Screen"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 600
    page.window_height = 400
    page.window_resizable = False

    # Setup fields and buttons
    text_username: TextField = TextField(label='Username', text_align=ft.TextAlign.LEFT, width=300)
    text_password: TextField = TextField(label='Password', text_align=ft.TextAlign.LEFT, width=300, password=True)
    checkbox_signup: Checkbox = Checkbox(value=False, label='I agree to the terms and conditions')
    btn_submit: ElevatedButton = ElevatedButton(text='Sign up', width=200, disabled=True)

    # functions and controls
    def validate(e: ControlEvent) -> None:
        if all([text_username.value, text_password.value, checkbox_signup.value]):
            btn_submit.disabled = False
        else:
            btn_submit.disabled = True
        page.update()

    def submit(e: ControlEvent) -> None:
        print('Username:', text_username.value)
        print('Password:', text_password.value)

        page.clean()
        page.add(
            Row(
                controls=[Text(value=f'Welcome: {text_username.value}!', size=20)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )

    # Link functions to our UI elements
    text_username.on_change = validate
    text_password.on_change = validate
    checkbox_signup.on_change = validate
    btn_submit.on_click = submit

    # Render the signup page
    page.add(
        Row(
            controls=[
                Column(
                    [text_username,
                     text_password,
                     checkbox_signup,
                     btn_submit
                     ]
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )


if __name__ == '__main__':
    ft.app(target=main)
