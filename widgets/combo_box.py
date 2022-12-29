"""QComboBox のサンプル."""

from PySide6 import QtWidgets, QtGui


def _combobox_changed():
    """コンボボックスの選択項目が変更された."""

    print("Changed!!")


class MainWindow(QtWidgets.QWidget):
    """メインウィンドウ."""

    def __init__(self):
        super().__init__()

        combobox1 = self._create_from_data()

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(combobox1)
        self.setLayout(layout)

    def _create_from_data(self, parent: QtWidgets.QWidget = None) -> QtWidgets.QComboBox:
        """データから生成."""

        # コンボボックスオブジェクトの生成
        combobox = QtWidgets.QComboBox(parent)
        # コンボボックスの選択肢を追加
        combobox.addItems(["One", "Two", "Three"])
        # コンボボックスの選択数を取得
        print(f'ItemNum={combobox.count()}')
        # 選択中の文字列を取得
        print(f'CurrentText={combobox.currentText()}')
        # IDを取得
        print(f'CurrentIndex={combobox.currentIndex()}')
        # 真ん中の選択肢 "Two" を削除 (コンボボックスのIDで指定)
        combobox.removeItem(1)
        # コンボボックス欄の入力を有効
        combobox.setEditable(True)
        # コンボボックスの選択肢が変更されたら呼び出す関数
        combobox.currentIndexChanged.connect(_combobox_changed)

        return combobox


if __name__ == '__main__':
    # アプリの実行と終了
    app = QtWidgets.QApplication()
    window = MainWindow()
    window.show()
    app.exec()
