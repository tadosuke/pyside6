""" QPushButton のサンプル."""

from PySide6 import QtWidgets
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMenu, QPushButton


class MainWindow(QtWidgets.QWidget):
    """メインウィンドウ."""

    def __init__(self) -> None:
        super().__init__()

        button = QPushButton("Button 1", self)

        # テキストを設定する
        # button.setText('Changed')

        # シグナルへの接続
        button.clicked.connect(self._clicked_button)
        button.pressed.connect(self._pressed_button)
        button.released.connect(self._released_button)

        # クリックしたことにする
        # button.click()

        # ボタンを押し続けている間、一定間隔でシグナルを発火させる
        # button.setAutoRepeat(True)
        # リピートするまでの時間（ミリ秒）
        # button.setAutoRepeatDelay(1000)
        # リピート間隔
        # button.setAutoRepeatInterval(500)

        # ウィジェット上で Enter キーを押したとき、このボタンを押したことにする
        # button.setDefault(True)

        # フラットスタイルにする
        # button.setFlat(True)

        # ボタンを押したときにメニューを出すようにする
        self._add_menu(button)

    def _add_menu(self, button: QPushButton) -> None:
        """ボタンにメニューを追加する."""

        menu = QMenu(parent=self)

        action = QAction('menu', self)
        action.triggered.connect(self._menu_selected)
        menu.addAction(action)

        button.setMenu(menu)

    def _menu_selected(self) -> None:
        """メニューが選択された."""

        print('menu selected')

    def _clicked_button(self) -> None:
        """ボタンがクリックされた."""

        print("button1 clicked")

    def _pressed_button(self) -> None:
        """ボタンが押された."""

        print("button1 pressed")

    def _released_button(self) -> None:
        """ボタンが離された."""

        print("button1 released")

    def _toggled_button(self) -> None:
        """ボタンのトグル状態が切り替わった."""

        print("button1 toggled")


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = MainWindow()
    window.show()
    app.exec()
