from tkinter import Misc
from tkinter.ttk import Button, Frame, Notebook
from typing import Self

from munchkin.ui.container.grid import UIContainerGridHorizontal
from munchkin.ui.element.form import (
    UIElementFormInput,
    UIElementFormInputProps,
    UIElementFormSkill,
    UIElementFormSkillProps,
)
from munchkin.ui.element.image import UIViewImage


class ClassDoorTab(UIContainerGridHorizontal):
    def __init__(self, master: Misc):
        super().__init__(master)

    @staticmethod
    def create(name: UIElementFormInputProps, first_skill: UIElementFormSkillProps):
        print(name)
        print(first_skill)

    def view(self) -> Self:
        # Form container on the left
        form_container = Frame(self)
        name = UIElementFormInput(form_container, "Name").view()
        first_skill = UIElementFormSkill(form_container, "First Skill").view()
        second_skill = UIElementFormSkill(form_container, "First Skill").view()

        Button(
            form_container,
            text="Create Race Card",
            command=lambda: ClassDoorTab.create(name.props, first_skill.props),
        ).pack()
        # place the container within the tab
        form_container.grid(row=0, column=0, sticky="nsew")

        # Image container on the right
        image_container = Frame(self)
        # load treasure example card
        UIViewImage.base(image_container, "static/img/example_class_card.jpg")
        # place the container within the tab
        image_container.grid(row=0, column=1, sticky="nsew")

        return self


class RaceDoorTab(UIContainerGridHorizontal):
    def __init__(self, master: Misc):
        super().__init__(master)

        # Form container on the left
        form_container = Frame(self)
        name = UIElementFormInput(form_container, "Name").view()
        first_skill = UIElementFormSkill(form_container, "First Skill").view()
        second_skill = UIElementFormSkill(form_container, "First Skill").view()

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
        UIViewImage.base(image_container, "static/img/card.jpg")
        # place the container within the tab
        image_container.grid(row=0, column=1, sticky="nsew")


class MonsterDoorTab(UIContainerGridHorizontal):
    def __init__(self, master: Misc):
        super().__init__(master)

        # Form container on the left
        form_container = Frame(self)
        name = UIElementFormInput(form_container, "Name").view()
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
        UIViewImage.base(image_container, "static/img/example_door_card.jpg")
        # place the container within the tab
        image_container.grid(row=0, column=1, sticky="nsew")


class MonsterEnhancerDoorTab(UIContainerGridHorizontal):
    def __init__(self, master: Misc):
        super().__init__(master)

        # Form container on the left
        form_container = Frame(self)
        name = UIElementFormInput(form_container, "Name").view()
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
        UIViewImage.base(image_container, "static/img/card.jpg")
        # place the container within the tab
        image_container.grid(row=0, column=1, sticky="nsew")


class DoorTab(Notebook):
    def __init__(self, master: Misc):
        super().__init__(master)

    def view(self) -> Self:
        race_tab = RaceDoorTab(self)
        class_tab = ClassDoorTab(self).view()
        monster_tab = MonsterDoorTab(self)
        monster_enhancer_tab = MonsterEnhancerDoorTab(self)

        self.add(race_tab, text="Race")
        self.add(class_tab, text="Class")
        self.add(monster_tab, text="Monster")
        self.add(monster_enhancer_tab, text="Monster Enhancer")

        self.pack(expand=True, fill="both")

        return self


class TreasureTab(UIContainerGridHorizontal):
    def __init__(self, master: Misc):
        super().__init__(master)

    @staticmethod
    def create(name: str, description: str):
        print(name, description)

    def view(self) -> Self:
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
            command=lambda: TreasureTab.create(
                name.props.get("input"), description.props.get("input")
            ),
        ).pack()
        # place the container within the tab
        form_container.grid(row=0, column=0, sticky="nsew")

        # Image container on the right
        image_container = Frame(self)
        # load treasure example card
        UIViewImage.base(image_container, "static/img/example_treasure_card.jpg")
        # place the container within the tab
        image_container.grid(row=0, column=1, sticky="nsew")

        return self


class Cards(Notebook):
    def __init__(self, master: Misc):
        super().__init__(master)

        # door card type
        door_tab = DoorTab(self).view()
        treasure_tab = TreasureTab(self).view()

        # add both tabs
        self.add(door_tab, text="Door Cards")
        self.add(treasure_tab, text="Treasure Cards")

        # pack to fill the whole frame
        self.pack(expand=True, fill="both")
