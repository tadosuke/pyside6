"""指定された座標にある子ウィジェットを取得する（レイアウト使用時）."""

from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

app = QApplication()
window = QWidget()

layout = QVBoxLayout()
layout.addWidget(QPushButton('button'))
window.setLayout(layout)

print(window.childAt(0, 0))  # button

window.show()
app.exec()
