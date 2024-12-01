import json

from pdfplumber.page import Page

from scripts.extracting_char import ExtractingChar


class Book:
    def __init__(self, pages: list[Page]):
        self.pages = pages
        self.min_y0 = None
        self.filters: set[str] | None = None

    def get_filters(self):
        if self.filters is None:
            self.filters = set()
            for page in self.pages:
                for char in page.chars:
                    extracting_char = ExtractingChar(char)
                    self.filters.add(extracting_char.get_rounded_size())
                    # self.filters.add(extracting_char.get_fontname())
        return self.filters

    def get_text(
            self,
            filters: list[str]=None,
            min_y0: float=None
    ):
        if min_y0 is not None:
            self.min_y0 = min_y0
        text = ''
        for extracting_page in self.pages:
            for char in extracting_page.chars:
                extracting_char = ExtractingChar(char)
                size = extracting_char.get_rounded_size()
                y0 = extracting_char.get_y0()

                if (
                        self.min_y0 is not None and
                        y0 < self.min_y0
                ):
                    continue

                if (
                        filters is not None and
                        size in filters
                ):
                    continue
                text += extracting_char.get_text()
        return text

