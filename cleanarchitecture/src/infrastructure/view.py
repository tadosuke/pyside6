"""View モジュール."""

from PySide6.QtWidgets import QMainWindow, QWidget

from adapter.controller import Controller
from adapter.presenter import Presenter, ViewModel


class MainWindow(QMainWindow):
    """メインウィンドウクラス.

    :param controller: View の入力を usecase 層に伝えるためのコントローラ
    :param presenter: usecase 層の出力を View に伝えるためのプレゼンター
    :param parent: 親ウィジェット
    """

    def __init__(
            self,
            controller: Controller,
            presenter: Presenter,
            parent: QWidget = None) -> None:
        super().__init__(parent=parent)

        self._controller = controller
        self._presenter = presenter

        self.setWindowTitle('MainWindow')
        self._presenter.update_view.connect(self._update_view)

    def _update_view(self, view_model: ViewModel) -> None:
        """ビューを更新する.

        :param view_model: 表示内容を表すビューモデル
        """
        pass
