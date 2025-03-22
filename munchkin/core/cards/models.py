from munchkin.base.domain.service import Model
from munchkin.base.persistance.repository import Schema


class CardSchema(Schema):
    name: str


class CardModel(Model):
    def __init__(self, data: CardSchema):
        super().__init__(data)
        self.name = data.get("name")
