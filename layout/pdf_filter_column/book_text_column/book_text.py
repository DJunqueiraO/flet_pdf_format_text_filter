import os

import flet
import pdfplumber

from scripts.book import Book


class BookText(flet.TextField):
    def __init__(
            self,
            **cfg
    ):
        self.single_line_value = None
        self.book = None
        self.path = None
        super().__init__(
            multiline=True,
            expand=True,
            **cfg
        )

    def get(self) -> Book:
        return self.book

    def get_value(self):
        return self.value

    def load_pdf(self, path):
        if not os.path.exists(path):
            return
        with pdfplumber.open(path) as filename_on_blur_file:
            self.path = path
            self.book = Book(filename_on_blur_file.pages)
            filters = self.book.get_filters()

            self.value = self.book.get_text(filters)

            self.update()
        return filters