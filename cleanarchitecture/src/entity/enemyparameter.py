"""エネミーのパラメータを保持するモジュール."""

import typing as tp


class EnemyParameter:
    """エネミーのパラメータ."""

    HP_MIN: tp.ClassVar[int] = 0
    HP_MAX: tp.ClassVar[int] = 99999
    NAME_LENGTH_MAX: tp.ClassVar[int] = 8

    def __init__(self) -> None:
        self._name = ''
        self._hp = 0

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if len(value) > self.NAME_LENGTH_MAX:
            raise ValueError(f"名前の長さは最大 {self.NAME_LENGTH_MAX} 文字までです。")
        self._name = value

    @property
    def hp(self) -> int:
        return self._hp

    @hp.setter
    def hp(self, value: int) -> None:
        if value < self.HP_MIN or value > self.HP_MAX:
            raise ValueError(f"HP は {self.HP_MIN} から {self.HP_MAX} の範囲で設定してください。")
        self._hp = value
