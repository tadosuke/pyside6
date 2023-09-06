"""オブジェクトの削除を予約するサンプル."""

from PySide6.QtWidgets import QApplication, QPushButton, QWidget


def _on_destroy():
    print('destroyed')
    if widget is not None:  # 破棄されても None にはならないので注意！
        # 既に破棄されているのでエラーになる
        print(widget)


def _on_clicked():
    print('deleteLater')
    widget.deleteLater()  # 削除を予約する
    # このタイミングではまだ生きている
    print(widget)


app = QApplication()

button = QPushButton('Button')
button.clicked.connect(_on_clicked)

widget = QWidget()
widget.destroyed.connect(_on_destroy)  # 削除されたときのシグナル

button.show()
app.exec()
