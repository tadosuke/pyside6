"""独自のイベントフィルタを使用する."""

from PySide6.QtCore import QObject, QEvent
from PySide6.QtWidgets import QApplication, QPushButton


class MyEventFilter(QObject):
    """独自イベントフィルタのクラス."""

    def eventFilter(self, watched, event) -> bool:
        if event.type() == QEvent.Type.MouseButtonDblClick:  # ダブルクリック
            # watched はイベントが実行されたオブジェクト
            print(f"ボタンがダブルクリックされました。({watched.text()})")
            return True  # イベントを処理済みとして、伝播を止める
        return False  # イベントを処理せず、伝播させる


app = QApplication()

button = QPushButton("Click me")
event_filter = MyEventFilter()
button.installEventFilter(event_filter)  # イベントフィルタを設定する
# button.removeEventFilter(event_filter)  # イベントフィルタを削除する

button.show()
app.exec()
