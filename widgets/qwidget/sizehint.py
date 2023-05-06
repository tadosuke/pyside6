"""サイズヒントをオーバーライト/取得する."""

from PySide6 import QtWidgets
from PySide6.QtCore import QSize


class MyWidget(QtWidgets.QPushButton):
    def sizeHint(self) -> QSize:
        """推奨サイズ."""
        return QSize(200, 100)

    def minimumSizeHint(self) -> QSize:
        """最小サイズ."""
        return QSize(100, 50)


app = QtWidgets.QApplication()
window = QtWidgets.QWidget()

widget = MyWidget()
print(widget.sizeHint())  # QSize
print(widget.minimumSizeHint())  # QSize

layout = QtWidgets.QVBoxLayout()
layout.addWidget(widget)
window.setLayout(layout)


window.show()
app.exec()
