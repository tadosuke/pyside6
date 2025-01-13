"""パラメータ設定ウィジェットのモジュール."""

from PySide6.QtWidgets import QWidget, QLineEdit, QSpinBox, QFormLayout


class ParameterWidget(QWidget):
    """パラメータ設定ウィジェット.

    :param parent: 親ウィジェット
    """

    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent=parent)
        self._create_children()
        self._create_layout()

    def _create_children(self) -> None:
        self._name_edit = QLineEdit('', parent=self)

        self._hp_spin_box = QSpinBox()
        self._hp_spin_box.setValue(0)
        self._hp_spin_box.setMinimum(0)
        self._hp_spin_box.setMaximum(99999)

    def _create_layout(self):
        layout = QFormLayout()
        layout.addRow('名前', self._name_edit)
        layout.addRow('HP', self._hp_spin_box)
        self.setLayout(layout)