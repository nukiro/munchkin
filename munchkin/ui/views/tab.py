from tkinter import Misc
from tkinter.ttk import Button, Frame
from typing import Callable, List, Self, TypedDict


class TabScreenView(TypedDict):
    label: str
    key: str
    content: Frame


class _TabScreenView(Frame):
    def __init__(self, master: Misc):
        super().__init__(master)
        self._screen: dict[str, Frame] = dict()

    def add(self, key: str, screen: Frame):
        self._screen[key] = screen

    def _hide_all(self):
        # get all frames store in screen dictionary
        for screen in self._screen.values():
            screen.pack_forget()

    def show(self, key: str):
        self._hide_all()
        # get screen which will be shown and pack
        screen = self._screen.get(key)
        screen.pack(expand=True, fill="both")

    def view(self, key: str) -> Self:
        # initial screen which will be shown as launch
        self.show(key)

        # screen frame main window position
        self.place(x=100, rely=0, relheight=1, relwidth=1)

        return self


class _TabMenuView(Frame):
    def __init__(self, master: Misc, show_method: Callable):
        super().__init__(master)
        self._screen_show_method = show_method
        self._buttons: List[Button] = []

    def add(
        self,
        key: str,
        label: str,
    ):
        # create button with show/hide handle from screen
        self._buttons.append(
            Button(self, text=label, command=lambda: self._screen_show_method(key))
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

    def add(self, screen: TabScreenView):
        """
        Add a new screen to the tab view.
        """
        # update both views the menu and the screen
        self._screen.add(screen.get("key"), screen.get("content"))
        self._menu.add(screen.get("key"), screen.get("label"))

    def view(self, key: str) -> Self:
        self._menu.view()
        # indicated key will be the screen shown at launch
        self._screen.view(key)

        return self
