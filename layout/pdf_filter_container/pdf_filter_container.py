import flet

from layout.loading_container.loading_container import LoadingContainer
from layout.pdf_filter_column.book_text_column.book_text_column import BookTextColumn
from layout.pdf_filter_column.filters_row.filters_row import FiltersRow
from layout.pdf_filter_column.get_text_button.get_text_button import GetTextButton
from layout.pdf_filter_column.inputs_row.inputs_row import InputsRow


class PdfFilterColumn(flet.Container):
    def __init__(
            self,
            page: flet.Page,
            loading_container: LoadingContainer,
            **cfg
    ):

        text_filters_row = FiltersRow()
        pdf_file_picker = flet.FilePicker()
        book_text_column = BookTextColumn()
        get_text_button = GetTextButton(
            file_picker=pdf_file_picker,
            book_text=book_text_column.book_text
        )
        inputs_row = InputsRow(
            filters_row=text_filters_row,
            loading_container=loading_container,
            file_picker=pdf_file_picker,
            page=page,
            book_text=book_text_column.book_text
        )

        super().__init__(
            content=flet.Column(
                controls=[
                    inputs_row,
                    text_filters_row,
                    book_text_column,
                    get_text_button,
                    pdf_file_picker
                ],
                expand=True
            ),
            **cfg
        )