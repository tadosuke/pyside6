"""ウィンドウアイコンを設定/取得する."""

from PySide6 import QtGui
from PySide6 import QtWidgets

app = QtWidgets.QApplication()
window = QtWidgets.QWidget()

# 設定
window.setWindowIcon(QtGui.QIcon("images/icon.png"))
# 取得
print(window.windowIcon())

window.show()
app.exec()
