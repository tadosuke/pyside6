"""ウィンドウ位置を設定/取得する."""

from PySide6 import QtWidgets

app = QtWidgets.QApplication()
window = QtWidgets.QWidget()

# 設定
window.move(100, 150)
# 取得
print(window.pos())  # QPoint(100, 150)

window.show()
app.exec()
