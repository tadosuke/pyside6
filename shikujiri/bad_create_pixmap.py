"""QPixmap の生成をメインスレッド外で行ってしまうサンプル：ダメな例."""

import concurrent.futures

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QLabel


_IMAGE_FILE = '../resource/face.png'


def _load_pixmap():
    """Pixmap を読み込む."""
    return QPixmap(_IMAGE_FILE)


if __name__ == '__main__':
    app = QApplication([])

    # QPixmap をメインスレッド外で生成
    executor = concurrent.futures.ThreadPoolExecutor()
    future = executor.submit(_load_pixmap)
    pixmap = future.result()

    label = QLabel()
    label.setPixmap(pixmap)
    label.show()

    app.exec()

