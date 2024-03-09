"""QWindow を QWidget に埋め込むサンプル."""

from PySide6.QtGui import QWindow
from PySide6.QtWidgets import QApplication, QWidget

app = QApplication()

window = QWindow()
widget = QWidget().createWindowContainer(window)
widget.show()

app.exec()