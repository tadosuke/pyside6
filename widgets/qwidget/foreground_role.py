"""ウィジェットの前景色を設定/取得する."""

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
button.setForegroundRole(color_role)
label.setForegroundRole(color_role)
slider.setForegroundRole(color_role)
edit.setForegroundRole(color_role)

# 取得
print(button.foregroundRole())
print(label.foregroundRole())
print(slider.foregroundRole())
print(edit.foregroundRole())

window.show()
app.exec()
