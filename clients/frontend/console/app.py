from tkinter import Tk
from typing import Optional

from clients.frontend.console.cards import Cards
from clients.frontend.console.menu import Menu
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


class Application(Tk):
    def __init__(self, settings: Optional[Settings] = _build_settings()):
        # Window setup
        super().__init__()
        self.title(settings.get("package"))
        self.geometry(f"{settings.get('width')}x{settings.get('height')}")
        self.minsize(settings.get("width"), settings.get("height"))

        # Main Window UI
        self.configure(menu=Menu(self))
        self.cards = Cards(self)

    def run(self):
        self.mainloop()
