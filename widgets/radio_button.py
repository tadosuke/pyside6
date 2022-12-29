"""QRadioButton のサンプル"""

from PySide6 import QtWidgets


class MainWindow(QtWidgets.QWidget):
    """メインウィンドウ."""

    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 300, 300)

        # ラジオボタンのグループ登録用オブジェクト
        self.radioGroup = QtWidgets.QButtonGroup()

        # ラジオボタンオブジェクトの生成
        radioButton1 = QtWidgets.QRadioButton("Radio Button 1", self)
        radioButton2 = QtWidgets.QRadioButton("Radio Button 2", self)
        radioButton3 = QtWidgets.QRadioButton("Radio Button 3", self)

        # ラジオボタンオブジェクトのグループ登録
        self.radioGroup.addButton(radioButton1, 1)
        self.radioGroup.addButton(radioButton2, 2)
        self.radioGroup.addButton(radioButton3, 3)

        # 2番目のラジオボタンを初期入力として設定
        radioButton2.setChecked(True)

        # ラジオボタンの配置設定
        radioButton1.move(10, 0)
        radioButton2.move(10, 30)
        radioButton3.move(10, 60)

        # 選択中のラジオボタンのIDを取得するボタン
        button = QtWidgets.QPushButton("IDを取得", self)
        button.clicked.connect(self._print_radiobutton_id)
        button.move(10, 90)

    def _print_radiobutton_id(self):
        """ラジオボタンの ID を表示する."""

        button_id = self.radioGroup.checkedId()  # 選択中のラジオボタンID
        print("Radio Button ID:", button_id)     # ID表示


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = MainWindow()
    window.show()
    app.exec()
