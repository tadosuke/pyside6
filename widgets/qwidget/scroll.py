"""子ウィジェットの位置をまとめて移動する."""

from PySide6.QtWidgets import QApplication, QWidget, QPushButton

app = QApplication()
window = QWidget()
window.setFixedSize(150, 100)

button1 = QPushButton('1', parent=window)
button1.move(0, 0)
button2 = QPushButton('2', parent=window)
button2.move(0, 30)

window.show()
window.scroll(20, 20)  # 右下に 20 px ずつスクロール
print(window.childAt(0, 0))  # 実際にウィジェットが移動するので、元の位置からは取得できない

app.exec()
