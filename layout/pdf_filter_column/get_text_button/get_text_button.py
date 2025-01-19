import flet

from layout.pdf_filter_column.book_text_column.book_text import BookText


class GetTextButton(flet.Button):
    def __init__(
            self,
            book_text: BookText,
            file_picker: flet.FilePicker,
            **cfg
    ):
        self.file_picker = file_picker
        self.book_text = book_text

        super().__init__(
            **cfg,
            text="Gerar arquivo de texto",
            on_click=self.save_txt
        )


    def save_txt(self, _: flet.ControlEvent):

        def file_picker_on_result(file_picker_on_result_event: flet.FilePickerResultEvent):

            path = file_picker_on_result_event.path

            with open(path, "w", encoding="utf-8") as file:
                file.write(self.book_text.value)

        self.file_picker.on_result = file_picker_on_result
        self.file_picker.save_file()