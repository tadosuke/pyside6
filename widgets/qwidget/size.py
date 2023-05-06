"""ウィンドウサイズを設定/取得する."""

from PySide6 import QtWidgets

app = QtWidgets.QApplication()
window = QtWidgets.QWidget()

# 設定
window.resize(150, 100)
# 取得
print(window.size())  # QSize(200, 300)

window.show()
app.exec()
