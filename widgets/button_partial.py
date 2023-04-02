""" QPushButton のサンプル."""

from functools import partial

from PySide6 import QtWidgets
from PySide6.QtWidgets import QPushButton, QVBoxLayout


class MainWindow(QtWidgets.QWidget):
    """メインウィンドウ."""

    def __init__(self) -> None:
        super().__init__()

        button1 = QPushButton("Button 1", self)
        button2 = QPushButton("Button 2", self)

        # シグナルへの接続
        button1.clicked.connect(partial(self._on_clicked, 0))
        button2.clicked.connect(partial(self._on_clicked, 1))

        layout = QVBoxLayout(self)
        layout.addWidget(button1)
        layout.addWidget(button2)
        self.setLayout(layout)

    def _on_clicked(self, button_id: int) -> None:
        print(f'button {button_id} clicked.')


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = MainWindow()
    window.show()
    app.exec()
