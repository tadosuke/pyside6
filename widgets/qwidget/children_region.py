"""全ての子ウィジェットを含む領域を取得する."""

from PySide6 import QtWidgets

app = QtWidgets.QApplication()
window = QtWidgets.QWidget()

button1 = QtWidgets.QPushButton('1', parent=window)
button1.move(10, 10)
button2 = QtWidgets.QPushButton('2', parent=window)
button2.move(80, 50)

# 取得
print(f'{window.childrenRegion()=}')  # QRegion(size=2, bounds=(10,10 170x70) - [(10,10 100x30), (80,50 100x30)]
print(f'{window.childrenRect()=}')  # QRect(10, 10, 170, 70)

window.show()
app.exec()
