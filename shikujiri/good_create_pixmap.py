"""QPixmap の生成をメインスレッド外で行ってしまうサンプル：よい例."""

import concurrent.futures

from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import QApplication, QLabel


_IMAGE_FILE = '../resource/face.png'


def _load_image():
    """QImage を読み込む."""
    return QImage(_IMAGE_FILE)


if __name__ == '__main__':
    app = QApplication([])

    # QImage をメインスレッド外で生成
    executor = concurrent.futures.ThreadPoolExecutor()
    future = executor.submit(_load_image)
    image = future.result()

    # メインスレッド上で QImage から QPixmap を生成
    pixmap = QPixmap.fromImage(image)

    label = QLabel()
    label.setPixmap(pixmap)
    label.show()

    app.exec()

