"""指定された座標にある子ウィジェットを取得する."""

from PySide6.QtWidgets import QApplication, QWidget, QPushButton

app = QApplication()
window = QWidget()

button = QPushButton('button', parent=window)
button.move(10, 10)

print(window.childAt(10, 10))  # button
print(window.childAt(9, 9))  # None

window.show()
app.exec()
