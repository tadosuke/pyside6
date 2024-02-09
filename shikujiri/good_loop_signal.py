"""GUI をプログラムから更新する際にシグナルがループしてしまうサンプル：よい例."""

import sys
from contextlib import contextmanager

from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget, QLabel


class MyModel(QObject):
    """モデルクラス."""

    value_changed = Signal()

    def __init__(self, parent: QObject):
        super().__init__(parent=parent)
        self.value = 0

    def set_value(self, value: int):
        self.value = value
        self.value_changed.emit()


class MyLabel(QLabel):
    """ラベルクラス."""

    value_changed = Signal()

    def __init__(self, parent: QWidget):
        super().__init__('0', parent=parent)

    def set_value(self, value: int):
        self.setText(str(value))
        self.value_changed.emit()


class MyWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.model = MyModel(parent=self)
        self.model.value_changed.connect(self._on_model_changed)

        self.label = MyLabel(parent=self)
        self.label.value_changed.connect(self._on_view_changed)

        layout = QVBoxLayout()
        layout.addWidget(self.label)

        self.setLayout(layout)

    def _on_view_changed(self):
        print('view_changed')
        with block_signals(self.model):  # model からのシグナルをブロック
            self.model.set_value(int(self.label.text()))

    def _on_model_changed(self):
        print('model_changed')
        with block_signals(self.label):  # view からのシグナルをブロック
            self.label.set_value(self.model.value)


@contextmanager
def block_signals(obj: QObject):
    """コンテキストの間だけ、obj のシグナルをブロックする."""
    obj.blockSignals(True)
    yield
    obj.blockSignals(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = MyWidget()
    widget.show()

    widget.model.set_value(1)
    widget.label.set_value(2)

    sys.exit(app.exec())
