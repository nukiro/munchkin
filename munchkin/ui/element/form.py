from tkinter import Frame, Misc, StringVar
from tkinter.ttk import Entry, Label
from typing import Optional, Self, TypedDict

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


class UIElementFormInputProps(TypedDict):
    input: str


class UIElementFormInput(Frame):
    def __init__(
        self,
        master: Misc,
        label: str,
        help: Optional[str] = None,
        space: Optional[int] = 10,
    ):
        super().__init__(master, pady=space)
        # Props
        self._props_entry = StringVar()

        # View
        self._label_text = label
        self._help_label_text = help

    def view(self) -> Self:
        # some text as a header indicating input variable
        Label(self, text=self._label_text).pack(fill="x")
        # input, props variable will be assigned
        entry = Entry(self, textvariable=self._props_entry)
        # in case some helping text is passed
        # it will place below the entry text input
        if self._help_label_text:
            entry.pack_configure(pady=2)
        entry.pack(fill="x")

        if self._help_label_text:
            Label(
                self,
                text=self._help_label_text,
                foreground="grey",
            ).pack(fill="x")

        self.pack(fill="x")

        return self

    @property
    def props(self) -> UIElementFormInputProps:
        return dict(input=self._props_entry.get())
