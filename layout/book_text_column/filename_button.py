import os

import flet

from layout.book_text_column.book_text import BookText
from layout.book_text_column.filter_button import FilterButton
from layout.book_text_column.filters_row import FiltersRow
from layout.loading_container.loading_container import LoadingContainer


class FilenameButton(flet.Button):
    def __init__(
        self,
        page: flet.Page,
        book_text: BookText,
        loading_container: LoadingContainer,
        filters_row: FiltersRow,
        file_picker: flet.FilePicker,
        **cfg
    ):

        self.filters_row = filters_row
        self.book_text = book_text
        self.page = page
        self.file_picker = file_picker
        self.loading_container = loading_container

        super().__init__(
            **cfg,
            on_click=self.filename_on_click
        )

    def filename_on_click(self, _: flet.ControlEvent):

        def file_picker_on_result(file_picker_on_result_event: flet.FilePickerResultEvent):
            files = file_picker_on_result_event.files

            if files is None:
                return
            path = files[0].path

            if not os.path.exists(path):
                return

            if '.pdf' not in path:
                return

            self.loading_container.visible = True
            self.loading_container.update()

            filters = self.book_text.load_pdf(path)

            self.filters_row.controls = list(map(
                lambda filename_on_blur_book_size: FilterButton(
                    book_text=self.book_text,
                    filters_row=self.filters_row,
                    loading_container=self.loading_container,
                    text=filename_on_blur_book_size
                ),
                sorted(filters)
            ))
            self.filters_row.update()
            self.loading_container.visible = False
            self.loading_container.update()
        self.file_picker.on_result = file_picker_on_result

        self.file_picker.pick_files()
