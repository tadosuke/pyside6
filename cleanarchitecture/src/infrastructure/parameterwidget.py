"""パラメータ設定ウィジェットのモジュール."""

from PySide6.QtWidgets import QWidget, QLineEdit, QSpinBox, QFormLayout

from adapter.presenter import ViewModel
from entity.enemyparameter import EnemyParameter


class ParameterWidget(QWidget):
    """パラメータ設定ウィジェット.

    :param parent: 親ウィジェット
    """

    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent=parent)
        self._create_children()
        self._create_layout()

    def update_view(self, view_model: ViewModel) -> None:
        """ViewModel の内容をもとにビューを更新する.

        :param view_model: ViewModel
        """
        pass

    def _create_children(self) -> None:
        self._name_edit = QLineEdit('', parent=self)

        self._hp_spin_box = QSpinBox(parent=self)
        self._hp_spin_box.setValue(0)
        self._hp_spin_box.setMinimum(EnemyParameter.HP_MIN)
        self._hp_spin_box.setMaximum(EnemyParameter.HP_MAX)

    def _create_layout(self):
        layout = QFormLayout()
        layout.addRow('名前', self._name_edit)
        layout.addRow('HP', self._hp_spin_box)
        self.setLayout(layout)
