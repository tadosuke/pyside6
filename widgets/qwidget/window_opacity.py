"""ウィジェットの透明度を設定/取得する."""

from PySide6 import QtWidgets

app = QtWidgets.QApplication()
window = QtWidgets.QWidget()

# 設定
window.setWindowOpacity(0.5)
# 取得
print(window.windowOpacity())

window.show()
app.exec()
