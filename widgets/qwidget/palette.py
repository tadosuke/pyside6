"""ウィジェットの背景色を設定/取得する."""

from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette

app = QtWidgets.QApplication()
window = QtWidgets.QWidget()

# 設定
palette = window.palette()
palette.setColor(QPalette.ColorRole.Window, Qt.red)  # ウィンドウ色を赤に
window.setPalette(palette)

# 取得
print(window.palette().color(QPalette.ColorRole.Window))

window.show()
app.exec()
