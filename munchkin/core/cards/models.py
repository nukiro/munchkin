from munchkin.base.domain.service import Model


class Card(Model):
    def __init__(self, name: str):
        self.name = name
