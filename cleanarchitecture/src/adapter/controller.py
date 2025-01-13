"""コントローラモジュール.

ユーザーからの入力を受け取り、UseCase 層の機能を呼び出す.
"""

from usecase.inputboundary import InputBoundary


class Controller:
    """ユーザーからの入力を受け取り、UseCase 層の機能を呼び出すクラス.

    :param input_boundary: 入力を渡すユースケース層のインターフェース
    """

    def __init__(self, input_boundary: InputBoundary) -> None:
        self._input_boundary = input_boundary

    def set_name(self, name: str) -> None:
        """名前を設定する."""
        self._input_boundary.set_name(name)

    def set_hp(self, hp: int) -> None:
        """HP を設定する."""
        self._input_boundary.set_hp(hp)
