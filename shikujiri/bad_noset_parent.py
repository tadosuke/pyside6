"""オブジェクトに親を設定し忘れるサンプル：良い例."""

from PySide6.QtWidgets import QApplication, QWidget, QPushButton

app = QApplication([])
window = QWidget()

# 親を指定してボタンを生成
button = QPushButton("Click Me!", parent=window)
button.destroyed.connect(lambda _: print('destroyed'))

# window（親） の削除予約
window.deleteLater()

window.show()
app.exec()

#  destroyed が表示される：Button もう残っていない
