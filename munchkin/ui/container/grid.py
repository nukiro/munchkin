from tkinter import Misc
from tkinter.ttk import Frame
from typing import Optional

from munchkin.base.validations import validate_exist, validate_positive_number


class UIContainerGrid(Frame):
    def __init__(self, master: Misc, rows: int, columns: int):
        validate_exist("master", master)
        validate_positive_number("rows", rows)
        validate_positive_number("columns", columns)

        super().__init__(master)

        # configure rows and columns
        self.rowconfigure(list(range(rows)), weight=1, uniform="a")
        self.columnconfigure(list(range(columns)), weight=1, uniform="a")


class UIContainerGridHorizontal(UIContainerGrid):
    def __init__(self, master, columns: Optional[int] = 2):
        super().__init__(master, 1, columns)
