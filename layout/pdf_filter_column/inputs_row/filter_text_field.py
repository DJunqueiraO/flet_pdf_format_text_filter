import flet
from flet.core.control_event import ControlEvent

from layout.pdf_filter_column.book_text_column.book_text import BookText
from scripts.book import Book
from layout.pdf_filter_column.filters_row.filters_row import FiltersRow
from typing import Callable


class FilterTextField(flet.TextField):
    def __init__(
            self,
            filters_row: FiltersRow,
            book_text: BookText,
            on_set_value: Callable[[float], str],
            **cfg
    ):
        self.text_filters_row = filters_row
        self.book_text = book_text
        self.on_set_value = on_set_value

        super().__init__(
            autofocus=True,
            keyboard_type=flet.KeyboardType.NUMBER,
            expand=True,
            on_submit=self.filter_text_field_on_submit,
            **cfg
        )

    def filter_text_field_on_submit(self, _):
        try:
            value = float(self.value)
        except ValueError:
            return

        self.book_text.value = self.on_set_value(value)
        # self.book_text.value = self.book_text.get().get_text(
        #     self.text_filters_row.get_unselected_filters(),
        #     min_y0=value
        # )
        self.book_text.update()