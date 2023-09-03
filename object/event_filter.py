"""イベントフィルターを設定するサンプル."""

from PySide6.QtCore import QObject, QEvent, Qt
from PySide6.QtWidgets import QPushButton, QApplication


class MyButton(QPushButton):
    def __init__(self):
        super().__init__('Button')
        # イベント発生時に eventFilter が呼ばれるようになる
        self.installEventFilter(self)

        # イベントフィルターを削除する
        # self.removeEventFilter(self)

    def eventFilter(self, watched: QObject, event: QEvent):
        # 右クリックイベントを処理する
        if event.type() == QEvent.MouseButtonPress:
            mouse_event = event
            if mouse_event.button() == Qt.RightButton:
                print("Right Click")
                return True  # 処理したら True を返す
        return False  # 処理しなかったら False を返す


app = QApplication()
button = MyButton()
button.show()
app.exec()
