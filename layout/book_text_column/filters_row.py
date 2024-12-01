import flet
from functools import reduce


class FiltersRow(flet.Row):
    def __init__(self, **cfg):
        super().__init__(
            scroll=flet.ScrollMode.HIDDEN,
            **cfg
        )

    def get_unselected_filters(self):
        def on_map_filter(control: flet.Control):
            if not isinstance(control, flet.Button):
                return
            return control.text, control.bgcolor

        def on_reduce_filter(a, b):
            if b[1] is not None:
                return a
            return a + [b]

        return list(map(
            lambda x: x[0],
            reduce(on_reduce_filter, list(map(on_map_filter, self.controls)), [])
        ))