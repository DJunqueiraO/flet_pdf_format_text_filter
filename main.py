import os

import flet
import pdfplumber

from layout.book_text import BookText
from layout.filename_button import FilenameButton
from layout.filters_row import FiltersRow
from layout.get_text_button import GetTextButton
from layout.pdf_file_picker import PdfFilePicker
from scripts.book import Book


def main(page: flet.Page):
    page.title = "Aplicação Básica com Flet"

    book_text = BookText(expand=True)
    text_filters_row = FiltersRow(scroll=flet.ScrollMode.ALWAYS)
    file_picker = PdfFilePicker()
    get_text_button = GetTextButton(
        file_picker=file_picker,
        book_text=book_text,
        text="Gerar arquivo de texto"
    )
    filename = FilenameButton(
        text="Escolha o arquivo",
        filters_row=text_filters_row,
        file_picker=file_picker,
        page=page,
        book_text=book_text,
        autofocus=True
    )
    size = flet.TextField(label="Digite um filtro desejado", autofocus=True, expand=True)

    column = flet.Column(
        expand=True,
        controls=[
            flet.Row(controls=[filename, size]),
            text_filters_row,
            flet.Column(
                expand=True,
                scroll=flet.ScrollMode.ALWAYS,
                controls=[book_text]
            ),
            get_text_button,
            file_picker
        ]
    )

    page.add(column)

    if not os.path.exists(f"in/{filename}.pdf"):
        return
    with pdfplumber.open(f"in/{filename}.pdf") as file:
        book = Book(file.pages)
        book_text.value = book.get_text()


flet.app(target=main)