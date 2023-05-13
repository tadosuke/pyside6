"""ウィジェットの背景色を設定/取得する."""

from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette
from PySide6.QtWidgets import QVBoxLayout, QPushButton, QLabel, QSlider, QLineEdit

app = QtWidgets.QApplication()
window = QtWidgets.QWidget()

# 準備
button = QPushButton('Button')
label = QLabel('Label')
slider = QSlider(Qt.Orientation.Horizontal)
edit = QLineEdit()

layout = QVBoxLayout()
layout.addWidget(button)
layout.addWidget(label)
layout.addWidget(slider)
layout.addWidget(edit)
window.setLayout(layout)

# 設定
color_role = QPalette.ColorRole.Highlight
button.setBackgroundRole(color_role)
label.setBackgroundRole(color_role)
slider.setBackgroundRole(color_role)
edit.setBackgroundRole(color_role)

# 取得
print(button.backgroundRole())
print(label.backgroundRole())
print(slider.backgroundRole())
print(edit.backgroundRole())

window.show()
app.exec()
