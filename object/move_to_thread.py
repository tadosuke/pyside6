"""オブジェクトを別スレッドで実行するサンプル."""

import sys

from PySide6.QtCore import QObject, QThread
from PySide6.QtWidgets import QApplication


class Worker(QObject):

    def do_work(self) -> None:
        # 今いるスレッドを表示
        print(f"{self.thread()=}")


app = QApplication(sys.argv)

worker = Worker()
worker.do_work()

# ワーカーをスレッドに移動
thread = QThread()
worker.moveToThread(thread)
thread.start()

worker.do_work()
