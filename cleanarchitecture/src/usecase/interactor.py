"""アプリケーションのルールに基づき、entity 層を操作する."""

from __future__ import annotations

from entity.enemyparameter import EnemyParameter
from usecase.dataaccess import DataAccessInterface
from usecase.inputboundary import InputBoundary
from usecase.outputboundary import OutputBoundary, OutputData


class UseCaseInteractor(InputBoundary):
    """アプリケーションのルールに基づき、entity 層を操作するクラス.

    :param data_access: 読込/保存用のインターフェース
    :param output: adapter 層に渡す出力
    """

    def __init__(
            self,
            data_access: DataAccessInterface,
            output: OutputBoundary = None) -> None:
        self._data_access = data_access
        self._output = output
        self._enemy_param = EnemyParameter()

    def set_name(self, name: str) -> None:
        """(override)名前を設定する.

        :param name: 名前
        """
        self._enemy_param.name = name
        self._output_parameter()

    def set_hp(self, hp: int) -> None:
        """(override)HP を設定する.

        :param hp: HP
        """
        self._enemy_param.hp = hp
        self._output_parameter()

    def save(self) -> None:
        """(override)パラメータを保存する."""
        self._data_access.save(self._enemy_param)

    def load(self) -> None:
        """(override)パラメータを読み込む."""
        self._enemy_param = self._data_access.load()
        self._output_parameter()

    def _output_parameter(self) -> None:
        if self._output is None:
            return

        data = OutputData(self._enemy_param)
        self._output.output(data)
