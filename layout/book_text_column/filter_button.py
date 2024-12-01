import flet

from layout.book_text_column.book_text import BookText
from layout.book_text_column.filters_row import FiltersRow

from layout.loading_container.loading_container import LoadingContainer


class FilterButton(flet.Button):
    def __init__(
            self,
            book_text: BookText,
            filters_row: FiltersRow,
            loading_container: LoadingContainer,
            **cfg
    ):
        self.book_text = book_text
        self.filters_row = filters_row
        self.loading_container = loading_container

        super().__init__(
            **cfg,
            on_click=self.filter_on_click
        )

    def toggle_color(self, selected: bool=None):
        if selected or self.color is None or self.bgcolor is None:
            self.bgcolor = "white"
            self.color = "black"
        else:
            self.bgcolor = None
            self.color = None

    def filter_on_click(self, _: flet.ControlEvent):
        self.loading_container.visible = True
        self.loading_container.update()
        self.toggle_color()

        filters = self.filters_row.get_unselected_filters()

        self.book_text.value = self.book_text.get().get_text(filters)
        self.loading_container.visible = False

        self.loading_container.update()
        self.book_text.update()
        self.update()