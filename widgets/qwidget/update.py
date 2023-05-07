"""ウィジェットを明示的に再描画する."""

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPainter, QMouseEvent
from PySide6.QtWidgets import QApplication, QWidget


class RandomCircleWidget(QWidget):
    def __init__(self):
        super().__init__()

        # 円の座標と色を保存するためのリスト
        self.circles = []

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            # クリックされた座標に円を描画
            pos = event.position()
            x = int(pos.x())
            y = int(pos.y())
            self.circles.append((x, y, QColor(127, 127, 127)))

            # ウィジェットを再描画（これを呼ばないとクリック時に描画されない）
            self.update()

    def paintEvent(self, event):
        # 円を描画
        painter = QPainter(self)
        for x, y, color in self.circles:
            painter.setBrush(color)
            painter.drawEllipse(x - 25, y - 25, 20, 20)


app = QApplication()
random_circle_widget = RandomCircleWidget()
random_circle_widget.show()
app.exec()
