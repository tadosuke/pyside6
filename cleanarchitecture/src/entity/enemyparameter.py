"""エネミーのパラメータを保持するモジュール."""

from dataclasses import dataclass
import typing as tp


@dataclass(frozen=True)
class EnemyParameter:
    """エネミーのパラメータ."""

    # 定数
    MAX_NAME_LENGTH: tp.ClassVar[int] = 8  # 名前の最大文字数
    MIN_HP: tp.ClassVar[int] = 0  # 最小HP
    MAX_HP: tp.ClassVar[int] = 99999  # 最大HP

    # メンバー
    name: str  # 名前
    hp: int = MIN_HP  # HP

    def __post_init__(self):
        if len(self.name) > self.MAX_NAME_LENGTH:
            raise ValueError(f"name must be {self.MAX_NAME_LENGTH} characters or less.")
        if not (self.MIN_HP <= self.hp <= self.MAX_HP):
            raise ValueError(f"hp must be between {self.MIN_HP} and {self.MAX_HP}.")
