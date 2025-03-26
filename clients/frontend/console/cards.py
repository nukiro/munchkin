from tkinter import Misc
from tkinter.ttk import Button, Entry, Frame, Label
from typing import Optional


class Form:
    @staticmethod
    def input(parent, label: str, help: Optional[str] = None) -> Frame:
        frame = Frame(parent, padding=2)

        Label(frame, text=label).pack(fill="x")
        entry = Entry(frame)
        if help:
            entry.pack_configure(pady=2)
        entry.pack(fill="x")
        Label(frame, text=help, foreground="grey", font=("Helvetica", 8)).pack(fill="x")

        frame.pack(fill="x")

        return frame


class Cards(Frame):
    def __init__(self, parent: Misc):
        super().__init__(parent)

        # Window UI
        Form.input(self, "Name")

        Button(self, text="Create Card", command=lambda: print("Create Card")).pack()

        self.pack(fill="x")
