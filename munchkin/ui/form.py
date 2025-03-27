from tkinter import Frame, Misc
from tkinter.ttk import Entry, Label
from typing import Optional

from munchkin.base.validations import validate_exist, validate_text


class UIForm:
    @staticmethod
    def input(master: Misc, label: str, help: Optional[str] = None) -> Frame:
        validate_exist("master", master)
        validate_text("label", label)

        view = Frame(master)

        Label(view, text=label).pack(fill="x")
        entry = Entry(view)
        # in case some helping text is passed
        # it will place below the entry text input
        if help:
            entry.pack_configure(pady=2)
        entry.pack(fill="x")

        if help:
            Label(view, text=help, foreground="grey", font=("Helvetica", 8)).pack(
                fill="x"
            )

        view.pack(fill="x")

        return view
