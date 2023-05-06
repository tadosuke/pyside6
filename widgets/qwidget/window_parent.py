"""ウィジェットの親を設定/取得する."""

from PySide6 import QtWidgets

app = QtWidgets.QApplication()

# 設定
window1 = QtWidgets.QWidget()
window2 = QtWidgets.QPushButton('子ウィジェット', parent=window1)
window1.show()

# 取得
print(window1.parent())  # None
print(window2.parent())  # window1

app.exec()
