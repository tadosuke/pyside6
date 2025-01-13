"""アプリケーションのルールに基づき、entity 層を操作する."""

from __future__ import annotations

from entity.enemyparameter import EnemyParameter
from usecase.inputboundary import InputBoundary, InputData
from usecase.outputboundary import OutputBoundary


class UseCaseInteractor(InputBoundary):
    """アプリケーションのルールに基づき、entity 層を操作するクラス.

    :param output: adapter 層に渡す出力
    """

    def __init__(
            self,
            output: OutputBoundary = None) -> None:
        self._enemy_param_dict: dict[str, EnemyParameter] = {}
        self._output = output

    def input(self, input_data: InputData) -> None:
        """(override)コントローラからの入力を受け取る."""
        # input_data を使って Entity を操作する
        param = EnemyParameter()
        param.name = input_data.name
        param.hp = input_data.hp
        self._enemy_param_dict[input_data.name] = param
