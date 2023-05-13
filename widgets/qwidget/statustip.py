"""ホバー時のステータスバーテキストを設定/取得する."""

from PySide6 import QtWidgets
from PySide6.QtWidgets import QStatusBar

app = QtWidgets.QApplication()
window = QtWidgets.QMainWindow()
window.setStatusBar(QStatusBar())

# 設定
window.setStatusTip('ステータスチップ')

# 取得
print(window.statusTip())  # ステータスチップ

window.show()
app.exec()
