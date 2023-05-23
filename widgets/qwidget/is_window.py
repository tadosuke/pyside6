"""ウィンドウかどうかを調べる."""

from PySide6 import QtWidgets
from PySide6.QtWidgets import QVBoxLayout, QPushButton

app = QtWidgets.QApplication()
window = QtWidgets.QWidget()
widget = QtWidgets.QPushButton('Button', parent=window)

# 取得
print(window.isWindow())  # True
print(widget.isWindow())  # False

window.show()
app.exec()
