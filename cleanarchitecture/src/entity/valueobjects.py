"""値オブジェクトモジュール."""

import typing as tp


class Hp:
    """HP.

    :param value: 値
    """

    #: 最小値
    MIN: tp.ClassVar[int] = 0
    #: 最大値
    MAX: tp.ClassVar[int] = 99999

    def __init__(self, value: int) -> None:
        if not self.MIN <= value <= self.MAX:
            raise ValueError(f"HP must be between {self.MIN} and {self.MAX}, got {value}.")
        self._value = value

    @property
    def value(self) -> int:
        return self._value

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Hp):
            return self._value == other._value
        raise TypeError

    def __lt__(self, other: object) -> bool:
        if isinstance(other, Hp):
            return self._value < other._value
        raise TypeError

    def __le__(self, other: object) -> bool:
        if isinstance(other, Hp):
            return self._value <= other._value
        raise TypeError

    def __gt__(self, other: object) -> bool:
        if isinstance(other, Hp):
            return self._value > other._value
        raise TypeError

    def __ge__(self, other: object) -> bool:
        if isinstance(other, Hp):
            return self._value >= other._value
        raise TypeError
