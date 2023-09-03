"""一定間隔でイベントを発生させるサンプル."""

from PySide6.QtCore import QObject, QTimerEvent
from PySide6.QtWidgets import QApplication


class MyObject(QObject):
    def __init__(self) -> None:
        super(MyObject, self).__init__()
        # 1000ミリ秒（1秒）ごとにタイマーイベントを発生させる
        self.timer_id = self.startTimer(1000)
        self.num = 0

    def timerEvent(self, event: QTimerEvent) -> None:
        print(f'timerEvent:{self.num}')
        self.num += 1
        if 5 <= self.num:
            # タイマーイベントを停止させる
            self.killTimer(self.timer_id)


app = QApplication()
obj = MyObject()
app.exec()