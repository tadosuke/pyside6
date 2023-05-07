"""カーソルを設定/取得する."""

from PySide6 import QtWidgets
from PySide6.QtGui import Qt

app = QtWidgets.QApplication()

# 設定
window = QtWidgets.QWidget()
window.setCursor(Qt.CursorShape.PointingHandCursor)
window.show()

# 取得
print(window.cursor())

app.exec()
