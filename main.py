import flet

from layout.pdf_filter_column.pdf_filter_column import PdfFilterColumn
from layout.loading_container.loading_container import LoadingContainer


def main(page: flet.Page):
    page.title = "Filtro de texto PDF"

    loading_container = LoadingContainer(visible=False)

    page.padding = 0
    page.spacing = 0

    page.add(
        flet.Stack(
            controls=[
                PdfFilterColumn(page=page, loading_container=loading_container),
                loading_container
            ],
            expand=True
        )
    )


flet.app(target=main)