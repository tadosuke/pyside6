"""ウィンドウのフレームをなくす."""

from PySide6 import QtWidgets
from PySide6.QtCore import Qt

app = QtWidgets.QApplication()

window = QtWidgets.QWidget()

# フレームレスフラグの設定
window.setWindowFlags(Qt.FramelessWindowHint)

window.show()
# 閉じるボタンも消えてしまうので、タスクバーから終了してください

app.exec()
