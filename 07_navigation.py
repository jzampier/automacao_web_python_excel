import flet as ft


def main(page: ft.Page) -> None:
    page.title = 'Minha Loja'

    def route_change(e: ft.RouteChangeEvent) -> None:
        page.views.clear()

        # Home
        page.views.append(
            ft.View(
                route='/',
                controls=[
                    ft.AppBar(title=ft.Text('Home'), bgcolor='green'),
                    ft.Text(value='Home', size=30),
                    ft.ElevatedButton(text='Ir para Loja', on_click=lambda _: page.go('/loja'))
                ],
                vertical_alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=26

            )
        )

        # Loja
        if page.route == '/loja':
            page.views.append(
                ft.View(
                    route='/loja',
                    controls=[
                        ft.AppBar(title=ft.Text('Loja'), bgcolor='Blue'),
                        ft.Text(value='Loja', size=30),
                        ft.ElevatedButton(text='Voltar', on_click=lambda _: page.go('/'))
                    ],
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=26

                )
            )
        page.update()

    def view_pop(e: ft.ViewPopEvent) -> None:
        page.views.pop()
        top_view: ft.View = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


if __name__ == '__main__':
    ft.app(target=main)
