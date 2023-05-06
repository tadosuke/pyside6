"""ウィンドウが配置されているスクリーンの情報を取得する."""

from PySide6 import QtWidgets

app = QtWidgets.QApplication()
window = QtWidgets.QWidget()
window.move(0, 0)

# スクリーン情報を取得
screen = window.screen()
screen_geometry = screen.geometry()

# ウィンドウをスクリーン中央に移動する
x = (screen_geometry.width() - window.width()) // 2
y = (screen_geometry.height() - window.height()) // 2
window.move(x, y)

window.show()
app.exec()
