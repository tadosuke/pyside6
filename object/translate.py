"""翻訳テキストを表示するサンプル."""

from PySide6.QtCore import QObject, QTranslator
from PySide6.QtWidgets import QApplication


class MyObject(QObject):
    def __init__(self) -> None:
        super().__init__()
        print(self.tr("Hello!"))
        #  翻訳データを読み込んでいれば、翻訳テキストが代わりに表示される


if __name__ == "__main__":
    app = QApplication()

    # 翻訳データを読み込む
    translator = QTranslator()
    if translator.load("translation.qm"):
        app.installTranslator(translator)

    obj = MyObject()
