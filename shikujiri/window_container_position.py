"""QWindow をウィンドウコンテナに埋め込んだ状態での座標取得."""
from PySide6.QtCore import QPoint
from PySide6.QtGui import QWindow
from PySide6.QtWidgets import QApplication, QWidget


def _print_point(point: QPoint):
    print(f'({point.x()}, {point.y()})')


app = QApplication()

# QWindow を生成
window = QWindow()
window.setPosition(10, 20)
_print_point(window.position())  # (10, 20)

# ウィンドウを埋め込んだウィンドウコンテナ（QWidget）を生成
widget = QWidget().createWindowContainer(window)
widget.move(100, 200)
widget.show()

_print_point(widget.pos())  # (100, 200)
_print_point(window.position())  # (0, 0)

app.exec()

