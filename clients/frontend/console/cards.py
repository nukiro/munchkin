from tkinter import Misc
from tkinter.ttk import Button, Frame, Notebook

from munchkin.ui.container.grid import UIContainerGrid, UIContainerGridHorizontal
from munchkin.ui.element.form import UIElementFormInput, UIViewForm
from munchkin.ui.element.image import UIViewImage


class ClassDoorTab(UIContainerGridHorizontal):
    def __init__(self, master: Misc):
        super().__init__(master)

        # Form container on the left
        form_container = Frame(self)
        UIViewForm.input(form_container, "Name")
        UIViewForm.skill(form_container)
        UIViewForm.skill(form_container)

        Button(
            form_container,
            text="Create Race Card",
            command=lambda: print("Create class door Card"),
        ).pack()
        # place the container within the tab
        form_container.grid(row=0, column=0, sticky="nsew")

        # Image container on the right
        image_container = Frame(self)
        # load treasure example card
        UIViewImage.base(image_container, "example_class_card.jpg")
        # place the container within the tab
        image_container.grid(row=0, column=1, sticky="nsew")


class RaceDoorTab(UIContainerGridHorizontal):
    def __init__(self, master: Misc):
        super().__init__(master)

        # Form container on the left
        form_container = Frame(self)
        UIViewForm.input(form_container, "Name")
        UIViewForm.skill(form_container)
        UIViewForm.skill(form_container)

        Button(
            form_container,
            text="Create Race Card",
            command=lambda: print("Create race Card"),
        ).pack()
        # place the container within the tab
        form_container.grid(row=0, column=0, sticky="nsew")

        # Image container on the right
        image_container = Frame(self)
        # load treasure example card
        UIViewImage.base(image_container, "card.jpg")
        # place the container within the tab
        image_container.grid(row=0, column=1, sticky="nsew")


class MonsterDoorTab(UIContainerGridHorizontal):
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


class MonsterEnhancerDoorTab(UIContainerGridHorizontal):
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
        UIViewImage.base(image_container, "card.jpg")
        # place the container within the tab
        image_container.grid(row=0, column=1, sticky="nsew")


class DoorTab(Notebook):
    def __init__(self, master: Misc):
        super().__init__(master)

        race_tab = RaceDoorTab(self)
        class_tab = ClassDoorTab(self)
        monster_tab = MonsterDoorTab(self)
        monster_enhancer_tab = MonsterEnhancerDoorTab(self)

        self.add(race_tab, text="Race")
        self.add(class_tab, text="Class")
        self.add(monster_tab, text="Monster")
        self.add(monster_enhancer_tab, text="Monster Enhancer")

        self.pack(expand=True, fill="both")


class TreasureTab(UIContainerGrid):
    def __init__(self, master: Misc, rows: int, columns: int):
        super().__init__(master, rows, columns)

        # Form container on the left
        form_container = Frame(self)
        name = UIElementFormInput(form_container, "Name").view()
        description = UIElementFormInput(
            form_container,
            "Description",
            "Card longer text where some indications about the card and its use is written.",
        ).view()
        Button(
            form_container,
            text="Create Treasure Card",
            command=lambda: print(name.props.get("input"), description.props),
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
    def __init__(self, master: Misc):
        super().__init__(master)

        # door card type
        door_tab = DoorTab(self)
        treasure_tab = TreasureTab(self, 1, 2)

        # add both tabs
        self.add(door_tab, text="Door Cards")
        self.add(treasure_tab, text="Treasure Cards")

        # pack to fill the whole frame
        self.pack(expand=True, fill="both")
