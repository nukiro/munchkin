from tkinter import Tk
from typing import Optional

from clients.frontend.console.views.account import AccountView
from clients.frontend.console.views.cards import CardsView
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

        # UI
        window = TabView(self)

        window.add(AccountView("Account", window.screen))
        window.add(CardsView("Cards", window.screen))
        window.add(GamesView("Games", window.screen))

        window.view("Account")

    def run(self):
        self.mainloop()
