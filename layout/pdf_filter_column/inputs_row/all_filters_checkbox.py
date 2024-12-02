import flet

from layout.pdf_filter_column.book_text_column.book_text import BookText
from layout.pdf_filter_column.filters_row.filter_button import FilterButton
from layout.pdf_filter_column.filters_row.filters_row import FiltersRow


class AllFiltersCheckbox(flet.Checkbox):
    def __init__(
            self,
            filters_row: FiltersRow,
            book_text: BookText,
            **cfg
    ):

        self.text_filters_row = filters_row
        self.book_text = book_text

        super().__init__(
            'Selecionar todos',
            on_change=self.all_checkbox_on_change,
            **cfg
        )

    def all_checkbox_on_change(self, _):

        def on_map_control(control: flet.Control):
            if not isinstance(control, FilterButton):
                return
            if control is not None:
                control.toggle_color(self.value)
            return control

        self.text_filters_row.controls = list(map(
            on_map_control, self.text_filters_row.controls
        ))
        self.text_filters_row.update()

        book = self.book_text.get()
        if book is None:
            return

        self.book_text.value = book.get_text(self.text_filters_row.get_unselected_filters())
        self.book_text.update()