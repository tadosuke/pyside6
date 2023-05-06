"""プロパティを設定/取得する."""

from PySide6 import QtWidgets

app = QtWidgets.QApplication()
window = QtWidgets.QWidget()

# 設定
window.setProperty("my_property", "Custom Property")

# 取得
print(window.property("my_property"))  # "Custom Property"

window.show()
app.exec()
