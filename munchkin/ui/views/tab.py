from tkinter import Misc
from tkinter.ttk import Button, Frame
from typing import Callable, List, Self, TypedDict

from munchkin.ui.views.view import View


class TabScreenView(TypedDict):
    label: str
    key: str
    content: Frame


class _TabScreenView(Frame):
    def __init__(self, master: Misc):
        super().__init__(master)
        # screen will be within the screen frame
        # and will be shown and hiden when menu buttons are clicked
        self._screen: dict[str, View] = dict()

    def add(self, view: View):
        self._screen[view.key] = view

    def _hide_all(self):
        # get all frames store in screen dictionary
        for screen in self._screen.values():
            screen.hide_view()

    def view(self, key: str) -> Self:
        # initialy pack/grid/place all views
        for screen in self._screen.values():
            screen.build_view()

        # then show which initial screen was indicated
        # initial screen which will be shown as launch
        self.show(key)

        # screen frame main window position
        self.place(x=100, rely=0, relheight=1, relwidth=1)

        return self

    def show(self, key: str):
        self._hide_all()
        # get screen which will be shown and pack
        screen = self._screen.get(key)
        screen.show_view()


class _TabMenuView(Frame):
    def __init__(self, master: Misc, show_method: Callable):
        super().__init__(master)
        self._screen_show_method = show_method
        self._buttons: List[Button] = []

    def add(
        self,
        key: str,
    ):
        # create button with show/hide handle from screen
        self._buttons.append(
            Button(self, text=key, command=lambda: self._screen_show_method(key))
        )

    def view(self) -> Self:
        # pack all buttons (one per screen)
        for option in self._buttons:
            option.pack(fill="x")

        # place button list from the main window
        self.place(relx=0, rely=0, relheight=1, width=100)

        return self


class TabView:
    def __init__(self, master: Misc):
        # holds all frame will be shown
        # screen view must be created first as it is injected into the menu
        # button within the options menu attribute needs
        # it reference to use show/hide methods.
        self._screen = _TabScreenView(master)
        # holds buttons to switch between frames
        # the screen method which handle how screens are shown or hiden
        # is injected to hold its reference
        self._menu = _TabMenuView(master, self._screen.show)

    @property
    def screen(self) -> Frame:
        return self._screen

    @property
    def menu(self) -> Frame:
        return self._menu

    def add(self, view: View):
        """
        Add a new screen to the tab view.
        """
        # view title will be set as key
        # update both views the menu and the screen
        self._screen.add(view)
        self._menu.add(view.key)

    def view(self, key: str) -> Self:
        self._menu.view()
        # indicated key will be the screen shown at launch
        self._screen.view(key)

        return self
