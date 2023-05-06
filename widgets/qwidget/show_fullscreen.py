"""ウィンドウをフルスクリーンで表示する."""

import time

from PySide6 import QtWidgets
from PySide6.QtCore import QCoreApplication

app = QtWidgets.QApplication()
window = QtWidgets.QWidget()

# フルスクリーンで表示する
window.showFullScreen()

# タイトルバーもつかめなくなってしまうので、自動で閉じるようにしています
start_time = time.time()
while time.time() < start_time + 1:
    QCoreApplication.processEvents()
window.close()
