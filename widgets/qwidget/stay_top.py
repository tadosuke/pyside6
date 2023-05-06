"""ウィンドウを常に最前面に表示する."""

from PySide6 import QtWidgets
from PySide6.QtCore import Qt

app = QtWidgets.QApplication()
window = QtWidgets.QWidget()

window.setWindowFlags(window.windowFlags() | Qt.WindowStaysOnTopHint)

window.show()
app.exec()
