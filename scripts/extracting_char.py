class ExtractingChar(dict):
    def __init__(self, dict_: dict):
        super().__init__(dict_)

    def get_size(self):
        return self["size"]

    def get_rounded_size(self, ndigits=1):
        return round(self["size"], ndigits)

    def get_fontname(self):
        return self["fontname"]

    def get_text(self):
        return self["text"]

    def add_text(self, text: str):
        self["text"] += text
        return self

    def get_y0(self):
        return self["y0"]

    def get_y1(self):
        return self["y1"]

    def get_x0(self):
        return self["x0"]