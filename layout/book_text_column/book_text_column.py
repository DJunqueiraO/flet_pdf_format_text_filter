import flet
from reportlab.lib.pdfencrypt import padding

from layout.book_text_column.filename_button import FilenameButton
from layout.book_text_column.filter_button import FilterButton
from layout.book_text_column.filters_row import FiltersRow
from layout.book_text_column.get_text_button import GetTextButton
from layout.book_text_column.pdf_file_picker import PdfFilePicker
from layout.loading_container.loading_container import LoadingContainer
from layout.book_text_column.book_text import BookText


class BookTextColumn(flet.Column):
    def __init__(
            self,
            page: flet.Page,
            loading_container: LoadingContainer,
            **cfg
    ):
        book_text = BookText(expand=True)
        text_filters_row = FiltersRow()
        pdf_file_picker = PdfFilePicker()
        get_text_button = GetTextButton(
            file_picker=pdf_file_picker,
            book_text=book_text,
            text="Gerar arquivo de texto"
        )
        filename_button = FilenameButton(
            text="Escolha o arquivo",
            filters_row=text_filters_row,
            loading_container=loading_container,
            file_picker=pdf_file_picker,
            page=page,
            book_text=book_text,
            autofocus=True
        )
        size_textfield = flet.TextField(
            label="Digite um filtro desejado",
            autofocus=True,
            expand=True
        )

        def on_submit(_):
            text_filters_row.controls.append(FilterButton(
                text=size_textfield.value,
                filters_row=text_filters_row,
                book_text=book_text,
                loading_container=loading_container
            ))
            size_textfield.value = ''
            size_textfield.update()
            text_filters_row.update()
        size_textfield.on_submit = on_submit

        super().__init__(
            controls=[
                flet.Row(controls=[filename_button, size_textfield]),
                text_filters_row,
                flet.Column(
                    expand=True,
                    scroll=flet.ScrollMode.ALWAYS,
                    controls=[book_text]
                ),
                get_text_button,
                pdf_file_picker
            ],
            expand=True,
            **cfg
        )