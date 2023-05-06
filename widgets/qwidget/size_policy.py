"""サイズポリシーを設定/取得する."""

from PySide6 import QtWidgets
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QSizePolicy, QPushButton

app = QtWidgets.QApplication()

button1 = QPushButton('Minimum')
button2 = QPushButton('Maximum')
button3 = QPushButton('Fixed')
button4 = QPushButton('Expanding')
button5 = QPushButton('Ignored')

# 設定
button1.setMinimumSize(QSize(100, 50))
button1.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
button1.show()

button2.setMaximumSize(QSize(200, 100))
button2.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
button2.show()

button3.setFixedSize(QSize(100, 50))
button3.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
button3.show()

button4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
button4.show()

button5.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
button5.show()

# 取得
print(f'{button1.sizeHint()=}')
print(button1.sizePolicy())
print(button2.sizePolicy())
print(button3.sizePolicy())
print(button4.sizePolicy())
print(button5.sizePolicy())

app.exec()
