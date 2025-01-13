"""エネミーのパラメータを保持するモジュール."""

from valueobjects import Hp


class EnemyParameter:

    def __init__(self) -> None:
        self._name = ''
        self._hp = Hp(0)
