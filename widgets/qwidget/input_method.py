"""IME に入力のヒントを与える."""

from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLineEdit, QVBoxLayout

app = QtWidgets.QApplication()
window = QtWidgets.QWidget()
edits = [QLineEdit() for _ in range(4)]

# 設定
edits[0].setInputMethodHints(Qt.ImhNone)  # 指定なし
edits[1].setInputMethodHints(Qt.ImhHiddenText)  # 非表示テキスト（パスワード）
edits[2].setInputMethodHints(Qt.ImhDigitsOnly)  # 数字のみ
edits[3].setInputMethodHints(Qt.ImhUppercaseOnly)  # 大文字のみ

layout = QVBoxLayout()
for e in edits:
    print(e.inputMethodHints())  # 取得
    layout.addWidget(e)
window.setLayout(layout)
window.show()
app.exec()
