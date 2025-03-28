from tkinter import Tk
from typing import Optional

# from clients.frontend.console.views.cards import Cards
# from clients.frontend.console.views.menu import Menu
from clients.frontend.console.views.account import AccountView
from clients.frontend.console.views.cards import Cards
from clients.frontend.console.views.games import GamesView
from munchkin.base.settings import Settings as Base
from munchkin.base.settings import build_settings as build_base
from munchkin.ui.views.tab import TabView


class Settings(Base):
    width: int
    height: int


def _build_settings() -> Settings:
    settings = build_base()

    settings["width"] = 1200
    settings["height"] = 800

    return settings


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

        window.add(
            dict(label="Account", key="account", content=AccountView(window.screen))
        )

        window.add(dict(label="Cards", key="cards", content=Cards(window.screen)))

        window.add(dict(label="Games", key="games", content=GamesView(window.screen)))

        # cards_view = Frame(window.screen)
        # Label(cards_view, background="red", text="This is cards label").pack(
        #     expand=True, fill="both"
        # )
        # cards: TabScreenView = dict(label="Cards", key="cards", content=cards_view)
        # window.add(cards)

        # games_view = Frame(window.screen)
        # Label(games_view, background="yellow", text="This is games label").pack(
        #     expand=True, fill="both"
        # )
        # games: TabScreenView = dict(label="Games", key="games", content=games_view)
        # window.add(games)

        window.view("account")

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
