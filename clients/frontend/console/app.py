import tkinter as tk
from typing import Optional

from munchkin.base.settings import Settings as Base
from munchkin.base.settings import build_settings as build_base


class Settings(Base):
    width: int
    height: int


def _build_settings() -> Settings:
    settings = build_base()

    settings["width"] = 600
    settings["height"] = 800

    return settings


class Application(tk.Tk):
    def __init__(self, settings: Optional[Settings] = _build_settings()):
        # Main window setup
        super().__init__()
        self.title(settings.get("package"))
        self.geometry(f"{settings.get('width')}x{settings.get('height')}")
        self.minsize(settings.get("width"), settings.get("height"))

    def run(self):
        self.mainloop()
