from tkinter import Menu as TkMenu


def _munchkin(parent: TkMenu):
    menu = TkMenu(parent, tearoff=False)
    menu.add_command(label="Connect", command=lambda: print("New connection"))
    menu.add_command(label="Exit", command=lambda: print("New Exit"))

    parent.add_cascade(label="Munchkin", menu=menu)


class Menu(TkMenu):
    def __init__(self, parent):
        super().__init__(parent)
        _munchkin(self)
