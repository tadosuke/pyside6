"""コントローラモジュール.

ユーザーからの入力を受け取り、UseCase 層の機能を呼び出す.
"""

from PySide6.QtCore import QObject

from usecases import InputBoundary, InputData


class Controller(QObject):
    """ユーザーからの入力を受け取り、UseCase 層の機能を呼び出すクラス.

    :param input: 入力を渡すユースケース層のインターフェース
    """

    def __init__(self, input: InputBoundary, parent: QObject = None) -> None:
        super().__init__(parent=parent)

        self._input_boundary = input
