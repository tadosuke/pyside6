"""QLabel のサンプル."""

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QLineEdit, QGridLayout


class MainWindow(QWidget):
    """メインウィンドウ."""

    def __init__(self):
        super().__init__()

        self._setup_for_normal()
        # self._setup_for_buddy()

    def _setup_for_normal(self):
        """通常確認用にセットアップします."""

        # ラベルオブジェクトの生成
        label = QLabel()

        # テキストを設定
        label.setText('0123456789')

        # テキストを選択できるようにするために必要なフラグ
        label.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)
        # テキストを選択(開始位置, 長さ)
        label.setSelection(1, 3)
        # 選択中のテキストを取得
        print(f'Selected = {label.selectedText()}')

        # \n で改行も入れられる
        # label.setText('0123456789\n0123456789\n0123456789\n')

        # 画像を設定
        # label.setPixmap(QPixmap("statusicon_ok.png"))
        # label.setScaledContents(True)  # True にすると、ウィンドウの拡縮に合わせて画像も拡縮される

        # リンクを設定
        # label.setText('<a href="https://www.google.com/">Google</a>')  # リンクは<a>タグで指定する
        # label.setOpenExternalLinks(True)  # これを呼ばないと、クリックしても開かない

        # テキストを消去
        # label.clear()

        # テキストを取得
        print(label.text())

        # 右下寄せ
        # label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)

        # インデントを設定
        # label.setIndent(20)

        # マージンを設定
        # label.setMargin(30)

        layout = QVBoxLayout(self)
        layout.addWidget(label)
        self.setLayout(layout)

    def _setup_for_buddy(self):
        """setBuddy 確認用にセットアップします.

        &+1文字 のラベルは、対になるウィジェット（バディウィジェット）のショートカットキーとして利用されます。
        この例では、Alt+1～3 を押すと、それぞれ対応する LineEdit にフォーカスが移動します。
        """

        edit1 = QLineEdit()
        edit2 = QLineEdit()
        edit3 = QLineEdit()

        label1 = QLabel('(&1)名前')
        label2 = QLabel('(&2)住所')
        label3 = QLabel('(&3)電話')

        # バディウィジェットの設定
        label1.setBuddy(edit1)
        label2.setBuddy(edit2)
        label3.setBuddy(edit3)

        layout = QGridLayout(self)
        layout.addWidget(label1, 0, 0)
        layout.addWidget(edit1, 0, 1)
        layout.addWidget(label2, 1, 0)
        layout.addWidget(edit2, 1, 1)
        layout.addWidget(label3, 2, 0)
        layout.addWidget(edit3, 2, 1)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
