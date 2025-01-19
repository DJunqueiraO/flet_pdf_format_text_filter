import flet

from layout.pdf_filter_column.book_text_column.book_text import BookText
from layout.pdf_filter_column.filters_row.filters_row import FiltersRow
from layout.pdf_filter_column.inputs_row.all_filters_checkbox import AllFiltersCheckbox
from layout.pdf_filter_column.inputs_row.filename_button import FilenameButton
from layout.pdf_filter_column.inputs_row.filter_text_field import FilterTextField
from layout.loading_container.loading_container import LoadingContainer


class InputsRow(flet.Row):
    def __init__(
            self,
            filters_row: FiltersRow,
            loading_container: LoadingContainer,
            file_picker: flet.FilePicker,
            page: flet.Page,
            book_text: BookText,
            **cfg
    ):
        self.book_text = book_text
        self.filters_row = filters_row

        filename_button = FilenameButton(
            text="Escolha o arquivo",
            filters_row=filters_row,
            loading_container=loading_container,
            file_picker=file_picker,
            page=page,
            book_text=book_text,
            autofocus=True
        )
        cabecalho_textfield = FilterTextField(
            label="Digite um valor para filtragem do cabeçalho desejado",
            filters_row=filters_row,
            on_set_value=lambda value: (
                book_text.get().get_text(
                    filters_row.get_unselected_filters(),
                    min_y0=value
                )
            ),
            book_text=book_text
        )
        rodape_textfield = FilterTextField(
            label="Digite um valor para filtragem do rodape desejado",
            filters_row=filters_row,
            on_set_value=lambda value: (
                book_text.get().get_text(
                    filters_row.get_unselected_filters(),
                    min_y1=value
                )
            ),
            book_text=book_text
        )
        all_filters_checkbox = AllFiltersCheckbox(
            filters_row=filters_row,
            book_text=book_text
        )

        super().__init__(
            controls=[
                filename_button,
                cabecalho_textfield,
                rodape_textfield,
                all_filters_checkbox
            ],
            **cfg
        )