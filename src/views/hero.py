import flet as ft

def main(page: ft.Page):
    page.title = "Joey Renderer"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window.resizable = True
    page.expand = True
    page.update()

    # topbar = ft.Container(
    #     ft.Row(
    #         controls = [
    #             ft.Text("Welcome!")
    #         ]
    #     )
    # )

    def page_resized(e):
        print("New page size:", page.window.width, page.window.height)
        page.window.width = page.window.width
        page.window.height = page.window.height
        page.update()

    page.on_resized = page_resized

    eli5_card = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Image(
                            src="/wiki_func.png",
                            width=250,
                            height=200,
                            fit=ft.ImageFit.CONTAIN,
                            repeat=ft.ImageRepeat.NO_REPEAT,
                            border_radius=ft.border_radius.all(10),
                        ),
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.ListTile(
                                        leading=ft.Icon(ft.icons.ONDEMAND_VIDEO),
                                        title=ft.Text("!eli5"),
                                        subtitle=ft.Text(
                                            "Make a topic sisuper simple to learn and explain."
                                        ),
                                    ),
                                    ft.Row(
                                        [ft.TextButton("Start course"), ft.TextButton("More info")],
                                        alignment=ft.MainAxisAlignment.END,
                                    ),
                                ]
                            )
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                width=page.window.width/4-50,
                height=500,
                padding=10,
                alignment=ft.alignment.center
            )
        )
    
    wiki_card = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Image(
                            src="/wiki_func.png",
                            width=250,
                            height=200,
                            fit=ft.ImageFit.CONTAIN,
                            repeat=ft.ImageRepeat.NO_REPEAT,
                            border_radius=ft.border_radius.all(10),
                        ),
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.ListTile(
                                        leading=ft.Icon(ft.icons.ONDEMAND_VIDEO),
                                        title=ft.Text("!wiki"),
                                        subtitle=ft.Text(
                                            "Get a wikipedia summary for any subject."
                                        ),
                                    ),
                                    ft.Row(
                                        [ft.TextButton("Start course"), ft.TextButton("More info")],
                                        alignment=ft.MainAxisAlignment.END,
                                    ),
                                ]
                            )
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                width=page.window.width/4-50,
                height=500,
                padding=10,
                alignment=ft.alignment.center
            )
        )
    
    rel_card = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Image(
                            src="/rel_func.png",
                            width=250,
                            height=200,
                            fit=ft.ImageFit.CONTAIN,
                            repeat=ft.ImageRepeat.NO_REPEAT,
                            border_radius=ft.border_radius.all(10),
                        ),
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.ListTile(
                                        leading=ft.Icon(ft.icons.ONDEMAND_VIDEO),
                                        title=ft.Text("!rel"),
                                        subtitle=ft.Text(
                                            "Find topics & people related to your subject/guest."
                                        ),
                                    ),
                                    ft.Row(
                                        [ft.TextButton("Start course"), ft.TextButton("More info")],
                                        alignment=ft.MainAxisAlignment.END,
                                    ),
                                ]
                            )
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                width=page.window.width/4-50,
                height=500,
                padding=10,
                alignment=ft.alignment.center
            )
    )

    desc_card = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Image(
                            src="/desc_func.png",
                            width=250,
                            height=200,
                            fit=ft.ImageFit.CONTAIN,
                            repeat=ft.ImageRepeat.NO_REPEAT,
                            border_radius=ft.border_radius.all(10),
                        ),
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.ListTile(
                                        leading=ft.Icon(ft.icons.ONDEMAND_VIDEO),
                                        title=ft.Text("!desc"),
                                        subtitle=ft.Text(
                                            "Get a detailed look into anytime you wish."
                                        ),
                                    ),
                                    ft.Row(
                                        [ft.TextButton("Start course"), ft.TextButton("More info")],
                                        alignment=ft.MainAxisAlignment.END,
                                    ),
                                ]
                            )
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                width=page.window.width/4-50,
                height=500,
                padding=10,
                alignment=ft.alignment.center
            )
    )
    
    topbar = ft.Container(
        content=ft.Markdown("# **Podchat.ai**\nThe premiere podcasting suite",),
        alignment=ft.alignment.center,
        width=page.window.width-50,
        # height=100,
        height=page.window.height/8,
        # bgcolor=ft.Colors.AMBER,
        border_radius=ft.border_radius.all(5),
    )
    midbar = ft.Row(
        controls=[eli5_card, wiki_card, rel_card, desc_card],
        # alignment=ft.alignment.center,
        # width=page.window.width-50,
        width=page.window.width,
        alignment=ft.MainAxisAlignment.SPACE_AROUND,
        
        # spacing
        # height=100,
        # height=page.window.height/2,
        # bgcolor=ft.Colors.AMBER,
        # border_radius=ft.border_radius.all(5),
    )
    botbar = ft.Container(
        content=ft.TextButton("Start!", icon="Icons.RECORD_VOICE_OVER_OUTLINED"),
        alignment=ft.alignment.center,
        width=page.window.width-50,
        # height=100,
        height=page.window.height/6,
        # bgcolor=ft.Colors.AMBER,
        border_radius=ft.border_radius.all(5),
    )

    page.add(
        ft.Column(
            [topbar, midbar, botbar],
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            height=page.window.height - 50,
            width=page.window.width - 50,
            # max_width
            # padding
        )
    )


ft.app(main, assets_dir="assets")
