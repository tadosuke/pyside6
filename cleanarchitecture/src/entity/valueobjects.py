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
