import flet

from layout.book_text import BookText
from layout.filters_row import FiltersRow
from functools import reduce


class FilterButton(flet.CupertinoButton):
    def __init__(
            self,
            book_text: BookText,
            filters_row: FiltersRow,
            **cfg
    ):
        self.book_text = book_text
        self.filters_row = filters_row
        super().__init__(
            **cfg,
            on_click=self.filter_on_click
        )

    def filter_on_click(self, _: flet.ControlEvent):
        if self.color is None or self.bgcolor is None:
            self.bgcolor = "white"
            self.color = "black"
        else:
            self.bgcolor = None
            self.color = None

        def on_map_filter(control: flet.Control):
            if not isinstance(control, FilterButton):
                return
            return control.text, control.bgcolor

        def on_reduce_filter(a, b):
            if b[1] is not None:
                return a
            return a + [b]

        filters = list(map(
            lambda x: x[0],
            reduce(on_reduce_filter, list(map(on_map_filter, self.filters_row.controls)), [])
        ))

        self.book_text.value = self.book_text.get_book().get_text(filters)
        self.book_text.update()

        self.update()