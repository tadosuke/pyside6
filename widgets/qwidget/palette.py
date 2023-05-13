"""ウィジェットの背景色を設定/取得する."""

from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette
from PySide6.QtWidgets import QLabel

app = QtWidgets.QApplication()
window = QtWidgets.QWidget()
label = QLabel('テキスト', parent=window)

# パレットの設定
window_palette = window.palette()
window_palette.setColor(QPalette.ColorRole.Window, Qt.red)
label_palette = label.palette()
label_palette.setColor(QPalette.ColorRole.Window, Qt.blue)

# 子ウィジェットに設定
label.setPalette(label_palette)
label.setAutoFillBackground(True)  # 背景色を塗りつぶすオプション

# 親ウィンドウに設定
window.setPalette(window_palette)
# label.setAutoFillBackground(True)  # ウィンドウの場合は指定しなくても塗りつぶされる

# 取得
print(window_palette.color(QPalette.ColorRole.Window))
print(label_palette.color(QPalette.ColorRole.Window))

window.show()
app.exec()
