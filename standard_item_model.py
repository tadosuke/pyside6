"""QStandardItemModel のサンプル."""

from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItem, QStandardItemModel, QColor
from PySide6.QtWidgets import QApplication, QComboBox, QWidget, QStyle, QMainWindow, QStatusBar, QListView, QTreeView


def _create_combobox() -> QComboBox:
    """QComboBox を生成する."""

    model = QStandardItemModel()

    # テキスト
    item = QStandardItem('item1')
    item.setToolTip('ToolTip Text')  # 項目をマウスオーバーした時に出てくるテキスト
    model.appendRow(item)

    # スタイル設定
    item = QStandardItem('item2')
    item.setTextAlignment(Qt.AlignRight)  # 右寄せ
    item.setBackground(QColor(255, 0, 0))  # 背景色を赤にする
    item.setForeground(QColor(0, 0, 255))  # 文字色を青にする
    model.appendRow(item)

    # アイコンも設定可能
    icon = QApplication.style().standardIcon(QStyle.SP_TitleBarMenuButton)
    item = QStandardItem(icon, 'item3')
    model.appendRow(item)

    # 無効
    item = QStandardItem('item4')
    item.setEnabled(False)
    model.appendRow(item)

    # 選択不可
    item = QStandardItem('item5')
    item.setSelectable(False)
    model.appendRow(item)

    widget = QComboBox()
    widget.setModel(model)
    return widget


def _create_listview() -> QListView:
    """QListView を生成する."""

    model = QStandardItemModel()

    # テキスト
    item = QStandardItem('item1')
    item.setStatusTip('Status')  # ステータスバーに表示されるテキスト
    model.appendRow(item)

    # チェック可能
    item = QStandardItem('item2')
    item.setCheckable(True)
    item.setUserTristate(True)
    item.setCheckState(Qt.CheckState.PartiallyChecked)
    model.appendRow(item)

    # 編集不可
    item = QStandardItem('item3')
    item.setEditable(False)
    model.appendRow(item)

    # 選択不可
    item = QStandardItem('item4')
    item.setSelectable(False)
    model.appendRow(item)

    # 無効
    item = QStandardItem('item5')
    item.setEnabled(False)
    model.appendRow(item)

    widget = QListView()
    widget.setModel(model)
    return widget


def _create_treeview() -> QTreeView:
    """QTreeView を生成する."""

    model = QStandardItemModel()

    # テキスト
    item = QStandardItem('item1')
    item.setToolTip('ToolTip')  # マウスオーバー中に出てくるテキスト
    item.setStatusTip('StatusTip')  # ステータスバーに表示されるテキスト
    model.appendRow(item)

    # 子
    item = QStandardItem('item2')
    child_item = QStandardItem('child1')
    item.setChild(0, 0, child_item)
    child_item.setChild(0, 0, QStandardItem('child2'))
    model.appendRow(item)

    # 追加・削除
    item = QStandardItem('item3')
    item.insertColumn(0, [QStandardItem('child1')])  # 列
    item.insertRow(0, [QStandardItem('child2')])  # 行挿入
    item.appendRow(QStandardItem('child3'))  # 行追加
    item.removeRow(2)  # 削除
    model.appendRow(item)

    widget = QTreeView()
    widget.setModel(model)
    return widget


class MainWindow(QMainWindow):

    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)

        # widget = _create_combobox()
        # widget = _create_listview()
        widget = _create_treeview()

        self.setCentralWidget(widget)
        self.setStatusBar(QStatusBar())


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
