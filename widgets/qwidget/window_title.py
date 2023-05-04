"""ウィンドウタイトルを設定/取得する."""

from PySide6 import QtWidgets

app = QtWidgets.QApplication()
window = QtWidgets.QWidget()

# 設定
window.setWindowTitle('タイトル')
# 取得
print(window.windowTitle())

window.show()
app.exec()
