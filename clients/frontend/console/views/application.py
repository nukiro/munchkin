from tkinter import Misc, Tk
from tkinter.ttk import Button, Frame, Label
from typing import List, Optional, Self, TypedDict

# from clients.frontend.console.views.cards import Cards
# from clients.frontend.console.views.menu import Menu
from munchkin.base.settings import Settings as Base
from munchkin.base.settings import build_settings as build_base


class Settings(Base):
    width: int
    height: int


def _build_settings() -> Settings:
    settings = build_base()

    settings["width"] = 1200
    settings["height"] = 800

    return settings


class TabScreenViewType(TypedDict):
    name: str
    key: str
    content: Frame


class TabScreenView(Frame):
    def __init__(self, master: Misc):
        super().__init__(master)
        self._screens: dict[str, Frame] = dict()

    def add(self, key: str, screen: Frame):
        self._screens[key] = screen

    def _hide_all(self):
        for screen in self._screens.values():
            screen.pack_forget()

    def show(self, key: str):
        self._hide_all()
        screen: Frame = self._screens.get(key)
        screen.pack(expand=True, fill="both")

    def view(self, key: str) -> Self:
        self.show(key)
        self.place(x=100, rely=0, relheight=1, relwidth=1)
        return self

    @property
    def screens(self) -> dict[str, Frame]:
        return self._screens


class TabMenuView(Frame):
    def __init__(self, master: Misc, screens: TabScreenView):
        super().__init__(master)
        self._screens = screens
        # self._buttons: List[Button] = [
        #     Button(
        #         self,
        #         text=screen.get("name"),
        #         command=lambda: screen_view.show(screen.get("key")),
        #     )
        #     for screen in screens
        # ]
        self._buttons: List[Button] = []

    def add(self, name: str, key: str):
        self._buttons.append(
            Button(self, text=name, command=lambda: self._screens.show(key))
        )

    def view(self) -> Self:
        for button in self._buttons:
            button.pack(fill="x")

        self.place(relx=0, rely=0, relheight=1, width=100)
        return self


class TabView:
    def __init__(self, master: Misc):
        self._screens = TabScreenView(master)
        self._menu = TabMenuView(master, self._screens)

    def add(self, screen: TabScreenViewType):
        self._screens.add(screen.get("key"), screen.get("content"))
        self._menu.add(screen.get("name"), screen.get("key"))

    def view(self) -> Self:
        self._menu.view()
        self._screens.view("account")
        return self

    @property
    def content_frame(self) -> Frame:
        return self._screens


class Application(Tk):
    def __init__(self, settings: Optional[Settings] = _build_settings()):
        # Window setup
        super().__init__()
        self.title(settings.get("package"))
        self.geometry(f"{settings.get('width')}x{settings.get('height')}")
        self.minsize(settings.get("width"), settings.get("height"))

        # # Main Window UI
        # self.configure(menu=Menu(self))
        # self.cards = Cards(self)

        window = TabView(self)

        account_view = Frame(window.content_frame)
        Label(account_view, background="green", text="This is account label").pack(
            expand=True, fill="both"
        )
        account: TabScreenViewType = dict(
            name="Account", key="account", content=account_view
        )
        window.add(account)

        cards_view = Frame(window.content_frame)
        Label(cards_view, background="red", text="This is cards label").pack(
            expand=True, fill="both"
        )
        cards: TabScreenViewType = dict(name="Cards", key="cards", content=cards_view)
        window.add(cards)

        games_view = Frame(window.content_frame)
        Label(games_view, background="yellow", text="This is games label").pack(
            expand=True, fill="both"
        )
        games: TabScreenViewType = dict(name="Games", key="games", content=games_view)
        window.add(games)

        window.view()

        # Menu Bar
        # menu = Frame(self)
        # Button(menu, text="Account", command=lambda: content.show("account")).pack(
        #     fill="x"
        # )
        # Button(menu, text="Cards", command=lambda: content.show("cards")).pack(fill="x")
        # Button(menu, text="Games", command=lambda: content.show("games")).pack(fill="x")
        # menu.place(relx=0, rely=0, relheight=1, width=100)

        # content = TabScreenView(self)

        # account = Frame(content)
        # Label(account, background="green", text="This is account label").pack(
        #     expand=True, fill="both"
        # )
        # content.add("account", account)

        # cards = Frame(content)
        # Label(cards, background="red", text="This is cards label").pack(expand=True)
        # content.add("cards", cards)

        # games = Frame(content)
        # Label(games, background="blue", text="This is games label").pack(fill="both")
        # content.add("games", games)

        # content.show("account")
        # content.place(x=100, rely=0, relheight=1, relwidth=1)

    def run(self):
        self.mainloop()
