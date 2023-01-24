"""QLabel のサンプル."""

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QLineEdit, QGridLayout


class MainWindow(QWidget):
    """メインウィンドウ."""

    def __init__(self):
        super().__init__()

        # 確認したい機能のコメントアウトを外してください
        self._setup_for_normal()
        # self._setup_for_format()
        # self._setup_for_pixmap()
        # self._setup_for_selection()
        # self._setup_for_buddy()

    def _setup_for_normal(self):
        """通常確認用にセットアップします."""

        # ラベルオブジェクトの生成
        label = QLabel()

        # テキストを設定
        label.setText('0123456789')
        # \n で改行も入れられる
        # label.setText('0123456789\n0123456789\n0123456789\n')
        print(f'text = {label.text()}')

        # 折り返し
        """
        label.setWordWrap(True)
        label.setMaximumWidth(50)  # 最大幅
        label.setText('This is a pen. That one is a cat.')  # 単語の切れ目で改行される
        """
        print(f'wordWrap = {label.wordWrap()}')

        # テキストを消去
        # label.clear()

        # アラインメント
        # label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)  # 右下寄せ
        print(f'alignment = {label.alignment()}')

        # インデント
        # label.setIndent(20)
        print(f'indent = {label.indent()}')

        # マージン
        # label.setMargin(30)
        print(f'margin = {label.margin()}')

        layout = QVBoxLayout(self)
        layout.addWidget(label)
        self.setLayout(layout)

    def _setup_for_pixmap(self):
        """setPixmap 確認用にセットアップします."""

        label = QLabel()

        label.setPixmap(QPixmap("statusicon_ok.png"))
        print(f'pixmap = {label.pixmap()}')
        label.setScaledContents(True)  # True にすると、ウィンドウの拡縮に合わせて画像も拡縮される
        print(f'hasScaledContents = {label.hasScaledContents()}')

        layout = QVBoxLayout(self)
        layout.addWidget(label)
        self.setLayout(layout)

    def _setup_for_format(self):
        """setTextFormat 確認用にセットアップします."""

        label = QLabel()

        # リッチテキスト
        label.setText('<a href="https://www.google.com/">Google</a>')
        label.setTextFormat(Qt.TextFormat.RichText)
        label.setOpenExternalLinks(True)  # これを呼ばないと、クリックしても開かない
        label.linkActivated.connect(lambda link: print(f'linkActivated(link={link})'))  # クリック時の処理
        label.linkHovered.connect(lambda link: print(f'linkHovered(link={link})'))  # ホバー時の処理
        print(f'openExternalLinks = {label.openExternalLinks()}')

        # マークダウン
        """
        label.setText(
            '# 見出し\n'
            '- リスト\n')
        label.setTextFormat(Qt.TextFormat.MarkdownText)
        """

        # プレーンテキスト
        """
        label.setText('<a href="https://www.google.com/">Google</a>')  # タグを指定しても無視される
        label.setTextFormat(Qt.TextFormat.PlainText)
        """

        print(f'textFormat = {label.textFormat()}')

        layout = QVBoxLayout(self)
        layout.addWidget(label)
        self.setLayout(layout)

    def _setup_for_selection(self):
        """setSelection 確認用にセットアップします."""

        label = QLabel('0123456789')

        # テキストを選択できるようにするために必要なフラグ
        label.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)
        print(f'textInteractionFlags = {label.textInteractionFlags()}')

        # テキストを選択(開始位置, 長さ)
        label.setSelection(1, 3)
        print(f'selectedText = {label.selectedText()}')
        print(f'hasSelectedText = {label.hasSelectedText()}')
        print(f'selectionStart = {label.selectionStart()}')

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

        print(f'Buddy1 = {label1.buddy()}')
        print(f'Buddy2 = {label2.buddy()}')
        print(f'Buddy3 = {label3.buddy()}')

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
