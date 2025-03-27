from tkinter import Misc
from tkinter.ttk import Button, Entry, Frame, Label, Notebook
from typing import Optional

from munchkin.ui.container.grid import UIContainerGrid
from munchkin.ui.form import UIForm
from munchkin.ui.image import UIImage


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


class TreasureTab(UIContainerGrid):
    def __init__(self, master: Misc, rows: int, columns: int):
        super().__init__(master, rows, columns)

        # Form container on the left
        form_container = Frame(self)
        UIForm.input(form_container, "Name")
        UIForm.input(form_container, "Description", "Card longer text.")
        Button(
            form_container,
            text="Create Treasure Card",
            command=lambda: print("Create treasure Card"),
        ).pack()
        # place the container within the tab
        form_container.grid(row=0, column=0, sticky="nsew")

        # Image container on the right
        image_container = Frame(self)
        # load treasure example card
        UIImage.base(image_container, "card.jpg")
        # place the container within the tab
        image_container.grid(row=0, column=1, sticky="nsew")


class Cards(Frame):
    def __init__(self, parent: Misc):
        super().__init__(parent)

        # Window UI
        Label(self, text="Create Cards").pack()

        # it is composed by two tabs (one per basic card type): door and treasure.
        notebook = Notebook(self)
        # door card type
        door_tab = Frame(notebook)
        # create a grip in the door tab (two columns and one row)
        # door_tab.columnconfigure(0, weight=1)
        # door_tab.columnconfigure(1, weight=1)
        # door_tab.rowconfigure(0, weight=1)

        Form.input(door_tab, "Name")
        Button(
            door_tab, text="Create Card", command=lambda: print("Create Card")
        ).pack()

        # treasure card type tab
        treasure_tab = TreasureTab(notebook, 1, 2)

        # add both tabs and pack
        notebook.add(door_tab, text="Door Cards")
        notebook.add(treasure_tab, text="Treasure Cards")
        notebook.pack(expand=True, fill="both")

        self.pack(expand=True, fill="both")
