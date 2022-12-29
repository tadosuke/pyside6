""" QCheckBox のサンプル."""

from PySide6 import QtWidgets, QtCore


class MainWindow(QtWidgets.QWidget):
    """メインウィンドウ."""

    def __init__(self) -> None:
        super().__init__()

        check_box = QtWidgets.QCheckBox("CheckBox", self)
        check_box.stateChanged.connect(self._checkbox_changed)
        check_box.toggled.connect(self._checkbox_toggled)

    def _checkbox_toggled(self, checked: bool) -> None:
        """チェック状態が変更された.

        :param checked: ON なら True
        """

        print(checked)

    def _checkbox_changed(self, state: QtCore.Qt.CheckState) -> None:
        """チェック状態が変更された.

        :param state: チェック状態。中間状態も取れる
        """

        print(f'changed:{state}')


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = MainWindow()
    window.show()
    app.exec()
