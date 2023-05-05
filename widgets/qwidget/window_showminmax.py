"""ウィンドウの最小化、最大化、通常表示を切り替える."""

from PySide6 import QtWidgets
from PySide6.QtCore import QThread


app = QtWidgets.QApplication()
window = QtWidgets.QWidget()

# 最小化
window.showMinimized()
# 最大化
window.showMaximized()
# 通常に戻す
window.showNormal()

app.exec()
