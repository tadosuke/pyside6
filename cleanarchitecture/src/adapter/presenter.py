"""プレゼンターモジュール.

UseCase 層から受け取ったデータを View が表示しやすい形式に加工する.
"""

from dataclasses import dataclass

from PySide6.QtCore import QObject, Signal

from usecase.outputboundary import OutputData


class Presenter(QObject):
    """UseCase 層から受け取ったデータを View が表示しやすい形式に加工するクラス.

    :param parent: 親オブジェクト
    """

    #: View の更新を要求するシグナル
    update_view = Signal(object)

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent=parent)

    def output(self, data: OutputData) -> None:
        """(OutputBoundary)UseCase 層からの出力を受け取る."""
        # データを加工
        view_model = ViewModel()

        # View に通知
        self.update_view.emit(view_model)


@dataclass
class ViewModel:
    """View の表示内容を保持するデータクラス."""
    pass
