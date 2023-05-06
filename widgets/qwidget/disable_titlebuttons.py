"""ウィンドウの最小化ボタン、最大化ボタン、クローズボタンを無効化する."""

from PySide6 import QtWidgets
from PySide6.QtCore import Qt

app = QtWidgets.QApplication()

window = QtWidgets.QWidget()

# デフォルトのウィンドウ装飾を非表示にし、独自のウィンドウタイトルバーやボタンなどを実装するためのフラグ
window.setWindowFlags(window.windowFlags() | Qt.CustomizeWindowHint)
# 最小化ボタンを無効化
window.setWindowFlags(window.windowFlags() & ~Qt.WindowMinimizeButtonHint)
# 最大化ボタンを無効化
window.setWindowFlags(window.windowFlags() & ~Qt.WindowMaximizeButtonHint)
# 閉じるボタンを無効化
window.setWindowFlags(window.windowFlags() & ~Qt.WindowCloseButtonHint)

window.show()
# 閉じるボタンは使えないので、タスクバーから閉じてください

app.exec()
