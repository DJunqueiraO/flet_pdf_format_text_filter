import os

import flet
import pdfplumber

from scripts.book import Book


class BookText(flet.TextField):
    def __init__(
            self,
            **cfg
    ):
        self.book = None
        super().__init__(
            multiline=True,
            **cfg
        )

    def get_book(self) -> Book:
        return self.book

    def load_pdf(self, path):
        if not os.path.exists(path):
            return
        with pdfplumber.open(path) as filename_on_blur_file:
            self.book = Book(filename_on_blur_file.pages)

            fonts = self.book.get_fonts()
            sizes = self.book.get_sizes()
            filters = fonts.union(sizes)

            self.value = self.book.get_text(filters)
            self.update()
        return filters