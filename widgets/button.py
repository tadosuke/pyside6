""" QPushButton のサンプル."""

from PySide6 import QtWidgets


class MainWindow(QtWidgets.QWidget):
    """メインウィンドウ."""

    def __init__(self) -> None:
        super().__init__()

        button = QtWidgets.QPushButton("Button 1", self)
        button.clicked.connect(self._clicked_button)
        button.pressed.connect(self._pressed_button)
        button.released.connect(self._released_button)

    def _clicked_button(self) -> None:
        """ボタンがクリックされた."""

        print("button1 clicked")

    def _pressed_button(self) -> None:
        """ボタンが押された."""

        print("button1 pressed")

    def _released_button(self) -> None:
        """ボタンが離された."""

        print("button1 released")


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = MainWindow()
    window.show()
    app.exec()
