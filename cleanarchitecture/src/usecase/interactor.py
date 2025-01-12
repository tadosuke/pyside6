"""アプリケーションのルールに基づき、entity 層を操作する."""

from __future__ import annotations

from entity.entity import Entity
from usecase.inputboundary import InputBoundary, InputData
from usecase.outputboundary import OutputBoundary, OutputData


class UseCaseInteractor(InputBoundary):
    """アプリケーションのルールに基づき、entity 層を操作するクラス.

    :param output: adapter 層に渡す出力
    """

    def __init__(
            self,
            output: OutputBoundary) -> None:
        self._output = output
        self._entity = Entity()

    def input(self, input_data: InputData) -> None:
        """(override)コントローラからの入力を受け取る."""
        # input_data を使って Entity を操作する
        self._entity.set_id(input_data.id)

        # adapter 層に出力
        id = self._entity.get_id()
        output_data = OutputData(id=id)
        self._output.output(output_data)
