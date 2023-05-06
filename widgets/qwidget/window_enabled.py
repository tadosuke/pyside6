"""ウィジェットの有効/無効を設定/取得する."""

from PySide6 import QtWidgets

app = QtWidgets.QApplication()
button = QtWidgets.QPushButton('無効')

# 設定
button.setEnabled(False)
# 取得
print(button.isEnabled())  # False

button.show()
app.exec()
