"""ウィンドウの最小サイズと最大サイズを設定/取得する."""

from PySide6 import QtGui
from PySide6 import QtWidgets

app = QtWidgets.QApplication()
window = QtWidgets.QWidget()

# 設定
window.setMinimumSize(300, 200)
window.setMaximumSize(400, 300)

# 取得
print(window.minimumSize())
print(window.maximumSize())

window.show()
app.exec()
