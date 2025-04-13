import flet as ft

def main(page: ft.Page):
    page.title = "Flet - Build beautiful interactive UIs with Python"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def learn_more(e):
        page.launch_url("https://flet.dev")


    podchat_title = "Podchat.ai"
    podchat_tagline = "The premiere podcasting suite."
    topbar = ft.Container(
        content= ft.Row(
            controls= [ft.Container(),
            ft.Column(
                    controls = [podchat_tagline,
                         # ft.Text(value="The Koala Renderer", color = "#A4A4A4", text_align = ft.TextAlign.CENTER, size=15, weight = ft.FontWeight.BOLD, italic = True)], 
                         ft.Text(value=podchat_title, color = "#A4A4A4",  size=15, weight = ft.FontWeight.BOLD, italic = True, text_align= ft.TextAlign.CENTER)], 
                    # controls = [ft.Text(value="The Koala Renderer", color = "#A4A4A4", text_align = ft.TextAlign.CENTER, size=20, weight = ft.FontWeight.BOLD, italic = True) ],
                    # alignment = ft.alignment.center,
                    alignment = ft.MainAxisAlignment.CENTER,
                    
                ),
            ],
            alignment = ft.MainAxisAlignment.SPACE_BETWEEN
        ),
    padding = 5)

    cards = bottombar = ft.Container()
    # page.add(
    #     # controls=[topbar, cards, bottombar]
    #     # ft.Column(
    #     #     controls=[topbar,],
    #     #     height=page.window.height-50,
    #     #     width=page.window.width-50,
    #     #     alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    #     #     expand=True
    #     # )
    #     topbar,
    # )

    page.add(ft.Container(
            content=[ft.Text("Hello World!")]
        )
    )
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
                            # padding=ft.padding.symmetric(horizontal=30, vertical=15),
