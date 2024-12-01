import json

from pdfplumber.page import Page

from scripts.extracting_char import ExtractingChar


class Book:
    def __init__(self, pages: list[Page]):
        self.pages = pages
        self.filters: set[str] | None = None

    def get_filters(self):
        if self.filters is None:
            self.filters = set()
            for page in self.pages:
                for char in page.chars:
                    extracting_char = ExtractingChar(char)
                    self.filters.add(extracting_char.get_rounded_size())
                    self.filters.add(extracting_char.get_fontname())
        return self.filters

    def get_text(self, filters: list[str]=None):
        text = ''
        for extracting_page in self.pages:
            for char in extracting_page.chars:
                extracting_char = ExtractingChar(char)
                size = extracting_char.get_rounded_size()
                fontname = extracting_char.get_fontname()
                if (
                        filters is not None and
                        size in filters and
                        fontname in filters
                ):
                    continue
                text += extracting_char.get_text()
        return text

