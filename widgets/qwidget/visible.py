"""ウィジェットの表示/非表示を設定/取得する."""

from PySide6 import QtWidgets

app = QtWidgets.QApplication()

# 設定
window1 = QtWidgets.QWidget()
window1.setWindowTitle('1')
window1.show()
window1.setVisible(True)

window2 = QtWidgets.QWidget()
window2.setWindowTitle('2')
window2.show()
window2.setVisible(False)

# 取得
print(window1.isVisible())
print(window2.isVisible())

app.exec()
