"""スタイルシートを設定/取得する."""

from PySide6 import QtWidgets

app = QtWidgets.QApplication()
window = QtWidgets.QWidget()

# 設定
window.setStyleSheet("background-color: yellow;")

# 取得
print(window.styleSheet())  # "background-color: yellow;"

window.show()
app.exec()
