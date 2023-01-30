"""QStringListModel のサンプル."""

from PySide6.QtCore import QStringListModel, QModelIndex, Qt
from PySide6.QtWidgets import QApplication, QComboBox, QWidget, QMainWindow, QListView, QTableView


def _on_data_changed(top_left: QModelIndex, bottom_right: QModelIndex) -> None:
    """データが変更された."""

    print(f'dataChanged(topLeft={top_left}, bottom_right={bottom_right})')


def _create_combobox() -> QComboBox:
    """QComboBox を生成する."""

    model = QStringListModel()
    model.dataChanged.connect(_on_data_changed)
    model.setStringList(['item1', 'item2', 'item3'])
    print(f'stringsList = {model.stringList()}')

    # 降順に並び替える
    model.sort(0, Qt.SortOrder.DescendingOrder)

    widget = QComboBox()
    widget.setModel(model)

    return widget


def _create_listview() -> QListView:
    """QListView を生成する."""

    model = QStringListModel(['item1', 'item2', 'item3'])
    model.dataChanged.connect(_on_data_changed)

    # 行の挿入もできるが、item を直接指定できないため使いにくい
    model.insertRow(2)
    model.setData(model.index(2), 'item4')  # dataChanged が呼ばれる

    widget = QListView()
    widget.setModel(model)

    return widget


def _create_tableview() -> QTableView:
    """QTableView を生成する.

    StringList は1次元データなので、2次元のビューには不向き
    """

    model = QStringListModel()
    model.dataChanged.connect(_on_data_changed)
    model.setStringList(['item1', 'item2', 'item3'])

    widget = QTableView()
    widget.setModel(model)

    return widget


class MainWindow(QMainWindow):

    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)

        # widget = _create_combobox()
        widget = _create_listview()
        # widget = _create_tableview()

        self.setCentralWidget(widget)
        # self.setStatusBar(QStatusBar())


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
