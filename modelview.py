"""ModelViewProgramming のサンプル."""

from PySide6 import QtWidgets, QtGui, QtCore


class MainWindow(QtWidgets.QWidget):
    """メインウィンドウ."""

    def __init__(self):
        super().__init__()

        combobox = self._create_combobox()

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(combobox)
        self.setLayout(layout)

    def _create_combobox(self) -> QtWidgets.QComboBox:
        combobox = QtWidgets.QComboBox()

        model = QtGui.QStandardItemModel()
        combobox.setModel(model)

        # item1
        item = QtGui.QStandardItem('text')
        # item.setEnabled(False)  # 項目を選択できなくする
        # item.setTextAlignment(QtCore.Qt.AlignRight)  # 右寄せ
        # item.setBackground(QtGui.QColor(255, 0, 0))  # 背景色を赤にする
        # item.setForeground(QtGui.QColor(0, 0, 255))  # 文字色を青にする
        # item.setToolTip('ToolTip Text')  # 項目をマウスオーバーした時に出てくるテキスト
        # item.setStatusTip('StatusTip Text')  # ステータスバーに表示する文字列
        model.appendRow(item)

        # item2
        icon = QtGui.QIcon('statusicon_ok.png')
        item = QtGui.QStandardItem(icon, 'OK')
        model.appendRow(item)

        return combobox


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = MainWindow()
    window.show()
    app.exec()
