import flet as ft

from views.FletRouter import Router


def main(page: ft.Page):
    page.route = "/"
    myRouter = Router(page, ft)

    page.on_route_change = myRouter.route_change()

    page.add(
        myRouter.body
    )


ft.app(target=main, assets_dir="assets")
