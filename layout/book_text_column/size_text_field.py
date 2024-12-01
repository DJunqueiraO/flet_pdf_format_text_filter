import flet

from layout.book_text_column.book_text import BookText
from layout.book_text_column.filters_row import FiltersRow


class SizeTextField(flet.TextField):
    def __init__(
            self,
            text_filters_row: FiltersRow,
            book_text: BookText,
            **cfg
    ):
        self.text_filters_row = text_filters_row
        self.book_text = book_text

        super().__init__(
            label="Digite um valor para filtragem do cabeçalho desejado",
            autofocus=True,
            keyboard_type=flet.KeyboardType.NUMBER,
            expand=True,
            on_submit=self.size_text_field_on_submit,
            **cfg
        )

    def size_text_field_on_submit(self, _):
        try:
            min_y0 = float(self.value)
        except ValueError:
            return

        self.book_text.value = self.book_text.get().get_text(
            self.text_filters_row.get_unselected_filters(),
            min_y0=min_y0
        )
        self.book_text.update()