"""Model/View Programming のサンプル."""

import typing as tp

from PySide6.QtCore import QAbstractListModel, QModelIndex, Qt
from PySide6.QtWidgets import QApplication, QComboBox, QVBoxLayout, QWidget


class MyModel(QAbstractListModel):
    """独自定義の ListModel クラス."""

    def __init__(self) -> None:
        super().__init__()

        self._items: list[str] = []

    def add(self, text: str) -> None:
        """アイテムを追加します."""

        self._items.append(text)

    def data(self, index, role) -> tp.Any:
        """(override) index, role に対応するデータを取得します."""

        if role == Qt.DisplayRole:
            return self._items[index.row()]

        return None

    def rowCount(self, parent=QModelIndex()) -> int:
        """(override) 行数を得ます."""

        return len(self._items)


class MyComboBox(QWidget):
    """MyModel の使用を強制する独自コンボボックス.

    コンボボックスを継承ではなく内包することで、View を直接操作する手段を制限しています。
    """

    def __init__(self, model: MyModel, parent: QWidget = None) -> None:
        super().__init__(parent=parent)
        self._combobox = QComboBox()
        self._combobox.setModel(model)

        layout = QVBoxLayout(self)
        layout.addWidget(self._combobox)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

    def select(self, index: int) -> None:
        """指定したインデックスのアイテムを選択します."""

        self._combobox.setCurrentIndex(index)


def _create_combobox_with_original_model() -> QComboBox:
    """独自実装の ItemModel を利用してコンボボックスを生成する."""

    combobox = QComboBox()

    model = MyModel()
    combobox.setModel(model)

    model.add('item1')
    model.add('item2')
    combobox.setCurrentIndex(0)

    return combobox


def _create_original_combobox() -> MyComboBox:
    """独自コンボボックスを生成する."""

    model = MyModel()
    combobox = MyComboBox(model)

    model.add('item1')
    model.add('item2')
    combobox.select(1)

    return combobox


class MainWindow(QWidget):
    """メインウィンドウ."""

    def __init__(self) -> None:
        super().__init__()

        combobox1 = _create_combobox_with_original_model()
        combobox2 = _create_original_combobox()

        layout = QVBoxLayout(self)
        layout.addWidget(combobox1)
        layout.addWidget(combobox2)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
