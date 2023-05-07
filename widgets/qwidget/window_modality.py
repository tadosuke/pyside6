"""ウィンドウのモーダル状態をアイコンを設定/取得する."""

from PySide6 import QtWidgets
from PySide6.QtCore import Qt

app = QtWidgets.QApplication()

# 準備
window1 = QtWidgets.QDialog()
window1.setWindowTitle('NonModal(parent)')
window1.setGeometry(100, 100, 200, 100)
window2 = QtWidgets.QDialog(parent=window1)
window2.setWindowTitle('WindowModal(child)')
window2.setGeometry(150, 150, 200, 100)
window3 = QtWidgets.QDialog()
window3.setWindowTitle('NonModal')
window3.setGeometry(200, 200, 200, 100)
window4 = QtWidgets.QDialog()
window4.setWindowTitle('ApplicationModal')
window4.setGeometry(250, 250, 200, 100)

# 設定
window2.setWindowModality(Qt.WindowModality.WindowModal)  # 親に対してのみモーダル
window4.setWindowModality(Qt.WindowModality.ApplicationModal)  # アプリケーション全体に対してモーダル

# 取得
print(f'{window1.windowModality()=}')
print(f'{window2.windowModality()=}')
print(f'{window3.windowModality()=}')
print(f'{window4.windowModality()=}')

window1.show()
window2.show()
window3.show()
# window4.show()
app.exec()
