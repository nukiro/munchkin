from tkinter import Misc
from tkinter.ttk import Button, Entry, Frame, Label, Notebook
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
        Label(self, text="Create Cards").pack()

        # it is composed by two tabs (one per basic card type): door and treasure.
        notebook = Notebook(self)
        # door card type
        door_tab = Frame(notebook)

        Form.input(door_tab, "Name")
        Button(
            door_tab, text="Create Card", command=lambda: print("Create Card")
        ).pack()

        # treasure card type
        treasure_tab = Frame(notebook)
        Label(
            treasure_tab, text="HELLOOO", foreground="grey", font=("Helvetica", 8)
        ).pack(fill="x")

        # add both tabs and pack
        notebook.add(door_tab, text="Door Cards")
        notebook.add(treasure_tab, text="Treasure Cards")
        notebook.pack(expand=True, fill="both")

        self.pack(expand=True, fill="both")
