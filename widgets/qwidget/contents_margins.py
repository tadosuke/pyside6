"""ウィジェットの縁と中身との間のスペースを設定/取得する."""

from PySide6 import QtWidgets

app = QtWidgets.QApplication()
window = QtWidgets.QWidget()

layout = QtWidgets.QVBoxLayout()
layout.addWidget(QtWidgets.QPushButton('button'))
window.setLayout(layout)

# 設定
left = 10
top = 20
right = 30
bottom = 40
window.setContentsMargins(left, top, right, bottom)

# 取得
print(window.contentsMargins())

window.show()
app.exec()
