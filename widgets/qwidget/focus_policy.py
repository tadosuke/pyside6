"""フォーカスポリシーを設定/取得する."""

from PySide6 import QtWidgets
from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt

app = QtWidgets.QApplication()
window = QtWidgets.QWidget()

edits = [QLineEdit() for _ in range(5)]

# フォーカスポリシーの設定
edits[0].setFocusPolicy(Qt.NoFocus)  # フォーカスを受け取らない
edits[1].setFocusPolicy(Qt.TabFocus)  # タブキーを使ってフォーカスを受け取る
edits[2].setFocusPolicy(Qt.ClickFocus)  # マウスクリックでフォーカスを受け取る
edits[3].setFocusPolicy(Qt.StrongFocus)  # タブキーとマウスクリックの両方でフォーカスを受け取る
edits[4].setFocusPolicy(Qt.WheelFocus)  # タブキー、マウスクリック、およびマウスホイールでフォーカスを受け取る

# フォーカスポリシーの取得
for e in edits:
    print(f'{e.focusPolicy()=}')

layout = QtWidgets.QVBoxLayout()
for e in edits:
    layout.addWidget(e)
window.setLayout(layout)
window.show()

app.exec()
