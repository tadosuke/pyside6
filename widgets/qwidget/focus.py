"""ウィジェットのフォーカスを設定/取得する."""

from PySide6 import QtWidgets

app = QtWidgets.QApplication()

# 準備
window = QtWidgets.QWidget()
edit1 = QtWidgets.QLineEdit()
edit2 = QtWidgets.QLineEdit()
layout = QtWidgets.QVBoxLayout()
layout.addWidget(edit1)
layout.addWidget(edit2)
window.setLayout(layout)
window.show()

# 設定
# edit1.setFocus()
edit2.setFocus()

# 削除
# edit2.clearFocus()

# 取得
print(edit1.hasFocus())
print(edit2.hasFocus())

app.exec()
