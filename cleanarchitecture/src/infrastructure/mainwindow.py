"""View モジュール."""
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow, QWidget

from adapter.controller import Controller
from adapter.presenter import Presenter, ViewModel
from infrastructure.parameterwidget import ParameterWidget


class MainWindow(QMainWindow):
    """メインウィンドウクラス.

    :param controller: コントローラ
    :param presenter: プレゼンター。親オブジェクトは MainWindow に設定される
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
        self._presenter.setParent(self)

        self.setWindowTitle('MainWindow')

        self._create_menu()
        self._create_children()

        self.setCentralWidget(self._parameter_widget)

        self._connect_signals()

    def _create_menu(self) -> None:
        """メニューを作成する."""
        self._create_file_menu()

    def _create_file_menu(self) -> None:
        """ファイルメニューを作成する."""
        menubar = self.menuBar()
        file_menu = menubar.addMenu("ファイル")

        # Save
        save_action = QAction("Save", self)
        save_action.triggered.connect(self._save)
        file_menu.addAction(save_action)

        # Load
        load_action = QAction("Load", self)
        load_action.triggered.connect(self._load)
        file_menu.addAction(load_action)

    def _create_children(self) -> None:
        """子ウィジェットを生成する."""
        self._parameter_widget = ParameterWidget(self._controller)

    def _connect_signals(self) -> None:
        """シグナルを接続する."""
        self._presenter.update_view.connect(self._update_view)

    def _update_view(self, view_model: ViewModel) -> None:
        """Presenter から渡された ViewModel を基にビューを更新する.

        :param view_model: 表示内容を表すビューモデル
        """
        self._parameter_widget.update_view(view_model)

    def _save(self) -> None:
        """Save が選択されたときの処理."""
        self._controller.save()

    def _load(self) -> None:
        """Load が選択されたときの処理."""
        self._controller.load()
