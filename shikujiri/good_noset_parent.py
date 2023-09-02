"""オブジェクトに親を設定し忘れるサンプル：悪い例."""

from PySide6.QtWidgets import QApplication, QWidget, QPushButton


app = QApplication([])
window = QWidget()

# 親を指定せずにボタンを生成
button = QPushButton("Click Me!")
button.destroyed.connect(lambda _: print('destroyed'))

# window の削除予約
window.deleteLater()

window.show()
app.exec()

#  destroyed は表示されない：Button はまだ残っている
