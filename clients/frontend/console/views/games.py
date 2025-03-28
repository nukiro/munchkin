from tkinter import Frame, Label, Misc
from typing import Self

from munchkin.ui.views.view import View


class GamesView(View, Frame):
    def __init__(self, master: Misc):
        super().__init__(master)

        self._label = Label(self, text="Games Section")

    def build_view(self) -> Self:
        self._label.pack(expand=True, fill="both")

        return self

    def show_view(self) -> Self:
        self.pack(expand=True, fill="both")

        return self

    def hide_view(self) -> Self:
        self.pack_forget()

        return self
