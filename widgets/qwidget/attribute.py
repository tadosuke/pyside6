"""ウィジェットの属性を設定/取得する."""

from PySide6 import QtWidgets
from PySide6.QtCore import Qt


app = QtWidgets.QApplication()
window = QtWidgets.QWidget()

# 設定
window.setAttribute(Qt.WidgetAttribute.WA_AcceptDrops)

# 取得
print(window.testAttribute(Qt.WidgetAttribute.WA_AcceptDrops))
print(window.acceptDrops())  # 同じ効果

window.show()
app.exec()
