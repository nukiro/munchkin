from tkinter import Frame, Misc
from tkinter.ttk import Entry, Label
from typing import Optional

from munchkin.base.validations import validate_exist, validate_text


class UIViewForm:
    @staticmethod
    def input(
        master: Misc, label: str, help: Optional[str] = None, space: Optional[int] = 10
    ) -> Frame:
        validate_exist("master", master)
        validate_text("label", label)

        view = Frame(master, pady=space)

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

    @staticmethod
    def skill(master: Misc, space: Optional[int] = 10) -> Frame:
        validate_exist("master", master)

        view = Frame(master, pady=space)
        Label(view, text="Skill").pack(fill="x")

        UIViewForm.input(view, "Header", None, 0)
        UIViewForm.input(view, "Description", None, 0)
        UIViewForm.input(view, "Action", "From the catalog.", 0)

        view.pack(fill="x")

        return view
