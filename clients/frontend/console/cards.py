from tkinter import Misc
from tkinter.ttk import Button, Frame, Notebook

from munchkin.ui.container.grid import UIContainerGrid, UIContainerGridHorizontal
from munchkin.ui.view.form import UIViewForm
from munchkin.ui.view.image import UIViewImage


class DoorTab(UIContainerGridHorizontal):
    def __init__(self, master: Misc):
        super().__init__(master)

        # Form container on the left
        form_container = Frame(self)
        UIViewForm.input(form_container, "Name")
        UIViewForm.input(form_container, "Description", "Card longer text.")
        Button(
            form_container,
            text="Create Door Card",
            command=lambda: print("Create door Card"),
        ).pack()
        # place the container within the tab
        form_container.grid(row=0, column=0, sticky="nsew")

        # Image container on the right
        image_container = Frame(self)
        # load treasure example card
        UIViewImage.base(image_container, "example_door_card.jpg")
        # place the container within the tab
        image_container.grid(row=0, column=1, sticky="nsew")


class TreasureTab(UIContainerGrid):
    def __init__(self, master: Misc, rows: int, columns: int):
        super().__init__(master, rows, columns)

        # Form container on the left
        form_container = Frame(self)
        UIViewForm.input(form_container, "Name")
        UIViewForm.input(form_container, "Description", "Card longer text.")
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
        UIViewImage.base(image_container, "example_treasure_card.jpg")
        # place the container within the tab
        image_container.grid(row=0, column=1, sticky="nsew")


class Cards(Notebook):
    def __init__(self, parent: Misc):
        super().__init__(parent)

        # door card type
        door_tab = DoorTab(self)
        treasure_tab = TreasureTab(self, 1, 2)

        # add both tabs
        self.add(door_tab, text="Door Cards")
        self.add(treasure_tab, text="Treasure Cards")

        # pack to fill the whole frame
        self.pack(expand=True, fill="both")
