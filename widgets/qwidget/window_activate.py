"""ウィンドウを前面に持ってくる."""

from PySide6 import QtWidgets

app = QtWidgets.QApplication()

# ウィンドウを２つ作る

window1 = QtWidgets.QWidget()
window1.setWindowTitle('1')
window1.move(0, 0)
window1.show()

window2 = QtWidgets.QWidget()
window2.setWindowTitle('2')
window2.move(100, 100)
window2.show()

# 何もしなければ、後から作ったほう（2）が前面に表示される。

# 最前面&入力を受け付けるようにする
#window1.activateWindow()

# 最前面に持ってくるだけ（入力は有効にならない）
#window1.raise_()

app.exec()
