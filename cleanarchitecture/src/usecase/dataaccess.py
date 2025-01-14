"""データアクセスのインターフェース"""

from __future__ import annotations

from abc import ABCMeta, abstractmethod

from entity.enemyparameter import EnemyParameter


class DataAccessInterface(metaclass=ABCMeta):
    """データの出力用を行うインターフェース."""

    @abstractmethod
    def save(self, parameter: EnemyParameter) -> None:
        """エネミーのパラメータを保存する.

        :param parameter: 保存するパラメータ
        """
        ...

    @abstractmethod
    def load(self) -> EnemyParameter:
        """エネミーのパラメータを読み込む.

        :return: 読み込んだパラメータ
        """
        ...
