"""QLayout のサンプル."""

from PySide6.QtWidgets import (
    QApplication,
    QVBoxLayout,
    QWidget,
    QLabel,
    QHBoxLayout,
    QLayout,
    QPushButton,
    QSizePolicy,
    QBoxLayout,
    QSpacerItem,
    QLayoutItem,
)
from PySide6.QtCore import Qt, QMargins


def _create_vbox_layout() -> QLayout:
    """VBoxLayout を利用したウィジェットを生成する."""

    # ボタンの生成
    button1 = QPushButton('Button1')
    button2 = QPushButton('Button2')
    button3 = QPushButton('Button3')

    # 拡縮時の挙動を設定する
    button1.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
    button2.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
    button3.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

    # レイアウトの生成、ウィジェットの追加
    layout = QVBoxLayout()
    layout.addWidget(button1)
    # layout.addStretch(1)  # 親ウィジェットが拡大した時に伸びるためのスペース
    # layout.addSpacing(20)  # 空白を追加する
    # layout.addSpacerItem(QSpacerItem(200, 50))  # 空白アイテムを追加する
    layout.addWidget(button2)
    # layout.addStretch(2)
    # layout.addStretch(3)  # 引数で他の Stretch スペースとの伸び率を設定できる
    layout.addWidget(button3)
    # layout.addStretch(3)

    # ウィジェットを指定位置に挿入
    # layout.insertWidget(2, QPushButton('insert'))

    # レイアウトを挿入
    """
    hlayout = QHBoxLayout()
    hlayout.addWidget(QPushButton('HButton1'))
    hlayout.addWidget(QPushButton('HButton2'))
    layout.insertLayout(4, hlayout)
    """

    # 水平方向の最小サイズを指定する
    layout.addStrut(200)

    # 親ウィジェトから内部要素までの距離(left, top, right, bottom)
    # layout.setContentsMargins(20, 30, 40, 50)
    # 予め作っておいた QMargin オブジェクトを渡すこともできる
    # margin = QMargins(20, 30, 40, 50)
    # layout.setContentsMargins(margin)

    # ウィジェット同士の間隔
    # layout.setSpacing(10)

    # QVBoxLayout では無効（NotImplementedError）
    # layout.addItem(QLayoutItem(Qt.AlignmentFlag.AlignTop))
    # layout.insertItem(1, QLayoutItem(Qt.AlignmentFlag.AlignTop))

    # ウィジェットを並べる向き
    # layout.setDirection(QBoxLayout.Direction.BottomToTop)  # 下から上に向かって並べる
    # print(f'Direction = {layout.direction()}')

    # 指定したウィジェットの伸縮率を設定する
    layout.setStretchFactor(button1, 1)
    layout.setStretchFactor(button2, 2)
    layout.setStretchFactor(button3, 3)
    print(f'Stretch1 = {layout.stretch(0)}')
    print(f'Stretch2 = {layout.stretch(1)}')
    print(f'Stretch3 = {layout.stretch(2)}')

    return layout


def _create_hbox_layout() -> QLayout:
    """HBoxLayout を利用したウィジェットを生成する."""

    layout = QHBoxLayout()
    layout.addWidget(QPushButton('button1'))
    layout.addWidget(QPushButton('button2'))
    layout.addWidget(QPushButton('button3'))

    return layout


class MyWidget(QWidget):
    """ウィジェットクラス."""

    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)

        layout = _create_vbox_layout()
        # layout = _create_hbox_layout()
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication()

    widget = MyWidget()
    widget.show()

    app.exec()
