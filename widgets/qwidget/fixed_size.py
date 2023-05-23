"""ウィンドウサイズを変更できないようにする."""

from PySide6 import QtWidgets
from PySide6.QtCore import QSize

app = QtWidgets.QApplication()
window = QtWidgets.QWidget()

window.setFixedSize(QSize(200, 100))

window.show()
app.exec()
