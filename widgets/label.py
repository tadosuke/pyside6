"""QLabel のサンプル."""

from PySide6 import QtWidgets, QtGui


class MainWindow(QtWidgets.QWidget):
    """メインウィンドウ."""

    def __init__(self):
        super().__init__()

        # ウィンドウのサイズを設定
        self.setGeometry(100, 100, 300, 300)

        # ラベルオブジェクトの生成
        label = QtWidgets.QLabel(self)

        # 画像を表示
        label.setPixmap(QtGui.QPixmap("statusicon_ok.png"))

        # テキストを表示
        # label.setText("Hello!")


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = MainWindow()
    window.show()
    app.exec()
