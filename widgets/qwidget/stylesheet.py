"""スタイルシートを設定/取得する."""

from PySide6 import QtWidgets

app = QtWidgets.QApplication()
window = QtWidgets.QLabel('テキスト')

# 設定
window.setStyleSheet(
    "background-color: yellow;"
    "color: red;"
    "margin: 10px;"
)

# 取得
print(window.styleSheet())  # "background-color: yellow;"

window.show()
app.exec()
