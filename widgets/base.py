"""ウィンドウを表示するだけのサンプル."""

from PySide6 import QtWidgets


class MainWindow(QtWidgets.QWidget):
    """メインウィンドウ."""

    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = MainWindow()
    window.show()
    app.exec()
