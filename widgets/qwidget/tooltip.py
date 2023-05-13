"""ホバー時の説明テキストを設定/取得する."""

from PySide6 import QtWidgets

app = QtWidgets.QApplication()
window = QtWidgets.QWidget()

# 設定
window.setToolTip('ツールチップ')
window.setToolTipDuration(1000)

# 取得
print(window.toolTip())  # ツールチップ
print(window.toolTipDuration())  # 1000

window.show()
app.exec()
