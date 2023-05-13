"""座標系の変換/逆変換を行う."""

from PySide6.QtCore import Qt
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget


class MyLabel(QLabel):
    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            pos_in_self = event.position().toPoint()
            pos_in_parent = self.mapToParent(pos_in_self)
            pos_in_global = self.mapToGlobal(pos_in_self)
            print(f'自身 {pos_in_self.toTuple()}')
            print(f'  親 {pos_in_parent.toTuple()}')
            print(f'  グローバル {pos_in_global.toTuple()}')

            # 逆変換
            print(self.mapFromParent(pos_in_parent).toTuple())  # pos_in_self
            print(self.mapFromGlobal(pos_in_global).toTuple())  # pos_in_self


app = QApplication()
window = QWidget()

label1 = MyLabel("Label1", parent=window)
label2 = MyLabel("Label2", parent=window)

layout = QVBoxLayout()
layout.addWidget(label1)
layout.addWidget(label2)
window.setLayout(layout)

window.show()
app.exec()
