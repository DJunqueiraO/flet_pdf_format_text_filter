import flet


class LoadingContainer(flet.Container):
    def __init__(self, **cfg):
        super().__init__(
            content=flet.Row(
                controls=[
                    flet.Column(
                        controls=[
                            flet.ProgressRing(
                                width=64,
                                height=64,
                                stroke_width=5
                            )
                        ],
                        alignment=flet.MainAxisAlignment.CENTER
                    )
                ],
                expand=True,
                alignment=flet.MainAxisAlignment.CENTER
            ),
            expand=True,
            bgcolor=flet.Colors.with_opacity(0.2, color=flet.Colors.BLACK),
            **cfg
        )