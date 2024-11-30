import flet


class PdfFilePicker(flet.FilePicker):
    def __init__(self, **cfg):
        super().__init__(**cfg)