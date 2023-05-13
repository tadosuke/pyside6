"""マスクを設定/取得する."""
from PySide6.QtGui import QRegion
from PySide6.QtWidgets import QApplication, QWidget, QPushButton

app = QApplication()
window = QWidget()
button = QPushButton('Button', parent=window)

# 円形のマスクを定義
mask = QRegion(2, 2, 70, 20, QRegion.Ellipse)
# 設定
button.setMask(mask)
# 取得
print(button.mask())

window.show()
app.exec()
