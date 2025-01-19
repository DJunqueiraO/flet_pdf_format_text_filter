import flet
from layout.pdf_filter_column.book_text_column.book_text import BookText


class BookTextColumn(flet.Column):
    def __init__(
            self,
            **cfg
    ):

        self.book_text = BookText()

        super().__init__(
            expand=True,
            scroll=flet.ScrollMode.ALWAYS,
            controls=[self.book_text],
            **cfg
        )