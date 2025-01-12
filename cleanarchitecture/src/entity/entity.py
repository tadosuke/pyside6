"""エンティティモジュール."""


class Entity:

    def __init__(self) -> None:
        self._id = 0

    def set_id(self, value: int) -> None:
        self._id = value

    def get_id(self) -> int:
        return self._id
