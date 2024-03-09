"""QWindow を表示するサンプル."""

from PySide6.QtGui import QWindow
from PySide6.QtWidgets import QApplication

app = QApplication()

window = QWindow()
window.show()

app.exec()