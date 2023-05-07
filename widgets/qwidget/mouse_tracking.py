"""マウスカーソルの動きを監視する."""

from PySide6 import QtGui
from PySide6 import QtWidgets
from PySide6.QtCore import Qt


class MyWidget(QtWidgets.QWidget):
    """マウスカーソルイベントを受け取るウィジェット."""

    def __init__(self):
        super().__init__()

        # マウス追跡を有効化
        self.setMouseTracking(True)
        print(f'{self.hasMouseTracking()=}')

        self.label = QtWidgets.QLabel('pos(0, 0)')
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignTop)
        layout.addSpacing(100)
        self.setLayout(layout)

    def mouseMoveEvent(self, event: QtGui.QMouseEvent):
        """マウス移動時に呼ばれる."""
        if event.type() == QtGui.QMouseEvent.Type.MouseMove:
            pos = event.position()
            self.label.setText(f'pos({int(pos.x())}, {int(pos.y())})')


app = QtWidgets.QApplication()
window = MyWidget()
window.show()
app.exec()
