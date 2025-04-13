import flet as ft

from views.chat import chat
from views.hero import hero

class Router:

    def __init__(self, page, ft):
        self.ft = ft
        self.page = page
        self.routes = {
            "/": hero(page),
            "/chat": chat(page)
        }
        self.body = ft.Container(content=self.routes['/'])

        def route_change(self, route):
            self.body.content = self.routes[route.route]
            self.body.update()
