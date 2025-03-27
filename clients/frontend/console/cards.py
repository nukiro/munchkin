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
        # create a grip in the door tab (two columns and one row)
        # door_tab.columnconfigure(0, weight=1)
        # door_tab.columnconfigure(1, weight=1)
        # door_tab.rowconfigure(0, weight=1)

        Form.input(door_tab, "Name")
        Button(
            door_tab, text="Create Card", command=lambda: print("Create Card")
        ).pack()

        # treasure card type
        treasure_tab = Frame(notebook)
        # treasure tab will have two columns (one for the from, another for the image hint)
        treasure_tab.columnconfigure((0, 1), weight=1, uniform="a")
        treasure_tab.rowconfigure(0, weight=1, uniform="a")

        title = Label(
            treasure_tab,
            text="HELLOOO",
            foreground="grey",
            background="red",
            font=("Helvetica", 8),
        )
        title.grid(row=0, column=0, sticky="new")

        # ti = Label(
        #     treasure_tab,
        #     text="HELLOOO",
        #     foreground="grey",
        #     background="blue",
        #     font=("Helvetica", 8),
        # )
        # ti.grid(row=0, column=1, sticky="new")

        # add both tabs and pack
        notebook.add(door_tab, text="Door Cards")
        notebook.add(treasure_tab, text="Treasure Cards")
        notebook.pack(expand=True, fill="both")

        self.pack(expand=True, fill="both")
