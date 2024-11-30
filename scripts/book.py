from pdfplumber.page import Page

class Book:
    def __init__(self, pages: list[Page]):
        self.pages = pages
        self.sizes: set[str] | None = None
        self.fonts: set[str] | None = None

    def get_fonts(self):
        if self.fonts is None:
            self.fonts = set()
            for page in self.pages:
                for char in page.chars:
                    self.fonts.add(char.get("fontname"))
        return self.fonts

    def get_sizes(self):
        if self.sizes is None:
            self.sizes = set()
            for page in self.pages:
                for char in page.chars:
                    self.sizes.add(char.get("size"))
        return self.sizes

    def get_text(self, filters: list[str]=None):
        text = ''
        for extracting_page in self.pages:
            for extracting_char in extracting_page.chars:
                size = extracting_char.get("size")
                font = extracting_char.get("fontname")
                if (
                        filters is not None and
                        size in filters and
                        font in filters
                ):
                    continue
                text += extracting_char.get("text")
        return text

