"""QPixmap の生成をメインスレッド外で行ってしまうサンプル."""

import concurrent.futures

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QLabel


_IMAGE_FILE = '../resource/face.png'


def _good_case():
    """良い例：メインスレッド内で QPixmap の生成を行っている."""
    app = QApplication([])

    # QPixmap をメインスレッド内で生成
    pixmap = QPixmap(_IMAGE_FILE)

    label = QLabel()
    label.setPixmap(pixmap)
    label.show()

    app.exec()


def _bad_case():
    """悪い例：メインスレッド外で QPixmap の生成を行っている."""
    app = QApplication([])

    # QPixmap をメインスレッド外で生成
    executor = concurrent.futures.ThreadPoolExecutor()
    future = executor.submit(_load_pixmap)
    pixmap = future.result()

    label = QLabel()
    label.setPixmap(pixmap)
    label.show()

    app.exec()


def _load_pixmap():
    """Pixmap を読み込む."""
    return QPixmap(_IMAGE_FILE)


if __name__ == '__main__':
    # _good_case()
    _bad_case()

