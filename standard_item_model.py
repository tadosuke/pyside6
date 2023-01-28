"""QStandardItemModel のサンプル."""

from PySide6.QtCore import Qt, QItemSelection, QItemSelectionModel
from PySide6.QtGui import QStandardItem, QStandardItemModel, QColor, QBrush
from PySide6.QtWidgets import QApplication, QComboBox, QWidget, QStyle, QMainWindow, QStatusBar, QListView, QTreeView, \
    QTableView


def _test_model() -> None:
    """QStandardItemModel 機能のテスト."""

    print('[TestModel]')
    model = QStandardItemModel()

    # アイテム変更時に呼ばれるシグナル
    model.itemChanged.connect(_on_item_changed)

    # アイテムの追加：itemChanged は呼ばれない
    model.appendRow(QStandardItem('item1'))
    model.appendRow(QStandardItem('item2'))
    model.appendRow(QStandardItem('item3'))

    # row を指定したアイテム取得
    item = model.item(1)
    print(f'text={item.text()}')
    # 編集：itemChanged が呼ばれる
    item.setData('item2_', Qt.ItemDataRole.DisplayRole)

    # テキストによるアイテム検索
    item = model.findItems('item3')[0]
    print(f'text={item.text()}')
    # アイテムから index を取得
    print(f'index={model.indexFromItem(item)}')

    # アイテムのソート（降順）
    # model.sort(0, Qt.SortOrder.DescendingOrder)

    # MIMEデータ
    # 　ドラッグ＆ドロップで転送できる情報を記述するために使用される
    print(f'mimeTypes={model.mimeTypes()}')
    print(f'mimeData={model.mimeData([item.index()])}')


def _on_item_changed(item: QStandardItem) -> None:
    """アイテムが変更された時に呼ばれる."""

    print(f'itemChanged({item.text()})')


def _create_combobox() -> QComboBox:
    """QComboBox を生成する."""

    print('[TestComboBox]')
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

    # 独自ロール
    item = QStandardItem('item6')
    item.setData('Hoge', Qt.ItemDataRole.UserRole)
    print(f'UserRole = {item.data(Qt.ItemDataRole.UserRole)}')
    model.appendRow(item)

    widget = QComboBox()
    widget.setModel(model)

    return widget


def _create_listview() -> QListView:
    """QListView を生成する."""

    print('[TestListView]')
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

    # 選択モデル
    selection = widget.selectionModel()
    selection.selectionChanged.connect(_on_selection_changed)
    index = model.index(1, 0)  # row=1 のアイテムを...
    selection.select(index, QItemSelectionModel.SelectionFlag.Select)  # 選択。selectionChangedが呼ばれる
    selection.clear()  # 選択解除。selectionChangedが呼ばれる
    print(f'isRowSelected(1) = {selection.isRowSelected(1)}')
    print(f'isIndexSelected(1, 0) = {selection.isSelected(index)}')

    return widget


def _create_tableview() -> QTableView:
    """QTableView を生成する."""

    print('[TestTableView]')
    model = QStandardItemModel()

    # ツールチップ、ステータスバーテキスト
    item1 = QStandardItem('item1')
    item1.setToolTip('ToolTip')
    item1.setStatusTip('StatusTip')

    # 編集不可
    item2 = QStandardItem('item2')
    item2.setEditable(False)

    # 選択不可・無効
    item3 = QStandardItem('item3')
    item3.setSelectable(False)
    item3.setEnabled(False)

    # チェック可能
    item4 = QStandardItem('item4')
    item4.setCheckable(True)
    item4.setCheckState(Qt.CheckState.Checked)

    # スタイル
    item5 = QStandardItem('item5')
    item5.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)  # 右寄せ
    item5.setBackground(QColor('red'))
    item5.setForeground(QColor(255, 255, 255))

    # アイコン
    item6 = QStandardItem('item6')
    icon = QApplication.style().standardIcon(QStyle.SP_TitleBarMenuButton)
    item6.setIcon(icon)

    model.appendRow([item1, item2])
    model.appendRow([item3, item4])
    model.appendRow([item5, item6])

    widget = QTableView()
    widget.setModel(model)

    return widget


def _on_selection_changed(selected: QItemSelection, deselected: QItemSelection) -> None:
    """選択状態が変化した時に呼ばれる.
    
    :param selected: 選択された項目
    :param deselected: 非選択になった項目
    """

    print(f'[selectionChanged]\n'
          f'  selected={selected.data()}\n'
          f'  deselected={deselected.data()})')


def _create_treeview() -> QTreeView:
    """QTreeView を生成する."""

    print('[TestTreeView]')
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

        # _test_model()

        # widget = QWidget()
        # widget = _create_combobox()
        # widget = _create_listview()
        widget = _create_tableview()
        # widget = _create_treeview()

        self.setCentralWidget(widget)
        self.setStatusBar(QStatusBar())


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
