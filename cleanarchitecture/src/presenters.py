"""プレゼンターモジュール.

UseCase 層から受け取ったデータを View が表示しやすい形式に加工する.
"""

from dataclasses import dataclass

from PySide6.QtCore import QObject

from usecases import OutputBoundary, OutputData


class Presenter(QObject):
    """UseCase 層から受け取ったデータを View が表示しやすい形式に加工するクラス."""

    def __init__(self, output_boundary: OutputBoundary, parent: QObject = None) -> None:
        super().__init__(parent=parent)
        self._output_boundary = output_boundary


@dataclass
class ViewModel:
    """View の表示内容を保持するデータクラス."""
    pass
