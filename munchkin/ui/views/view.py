from abc import ABC, abstractmethod
from typing import Self


class View(ABC):
    @property
    @abstractmethod
    def title(self) -> str:
        pass

    @abstractmethod
    def build_view(self) -> Self:
        pass

    @abstractmethod
    def show_view(self) -> Self:
        """It defines how the widget will be shown: pack, grid or place"""
        pass

    @abstractmethod
    def hide_view(self) -> Self:
        """It defines how the widget will be hidden regarding the method it was shown"""
        pass
