"""レイアウトを設定/取得する."""

from PySide6 import QtWidgets
from PySide6.QtWidgets import QVBoxLayout, QPushButton

app = QtWidgets.QApplication()
window = QtWidgets.QWidget()

# レイアウトの作成
layout = QVBoxLayout()
layout.addWidget(QPushButton("Button 1"))
layout.addWidget(QPushButton("Button 2"))

# 設定
window.setLayout(layout)

# 取得
print(window.layout())  # QVBoxLayout

window.show()
app.exec()
