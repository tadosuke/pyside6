"""ウィンドウのサイズと位置を一度に設定/取得する."""

from PySide6 import QtWidgets

app = QtWidgets.QApplication()
window = QtWidgets.QWidget()

# 設定
window.setGeometry(150, 100, 400, 300)
# 取得
print(window.geometry())  # QRect(100, 100, 400, 300)

window.show()
app.exec()
