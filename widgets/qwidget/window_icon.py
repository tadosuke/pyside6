"""ウィジェットアイコンを設定/取得する."""

from PySide6 import QtGui
from PySide6 import QtWidgets

app = QtWidgets.QApplication()
window = QtWidgets.QWidget()

# アイコンの設定
window.setWindowIcon(QtGui.QIcon("images/icon.png"))
# アイコンの取得
print(window.windowIcon())

window.show()
app.exec()
