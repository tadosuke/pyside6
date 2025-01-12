"""View モジュール."""

from PySide6.QtWidgets import QMainWindow, QWidget


class MainWindow(QMainWindow):
    """メインウィンドウクラス.

    :param parent: 親ウィジェット
    """

    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent=parent)

        self.setWindowTitle('MainWindow')
