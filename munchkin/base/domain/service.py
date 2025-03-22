from abc import ABC
from typing import List, Optional, Type

from munchkin.base.persistance.repository import UUID, IRepository, Schema


class Model:
    """Represent common model attributes. All models will inherence from it."""

    def __init__(self, row: Schema):
        # uuid as string type to make it is easier to work with
        self._uuid: Optional[UUID] = row.get("_uuid")


class IService[T: Model](ABC):
    def get(self) -> List[T]:
        pass


class ObjectService[T: Model](IService):
    def __init__(self, repository: IRepository, model: Type[T]):
        self._repository = repository
        self._model = model

    def get(self) -> List[T]:
        return [self._model(result) for result in self._repository.get()]
