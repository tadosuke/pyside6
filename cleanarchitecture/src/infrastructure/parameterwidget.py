"""パラメータ設定ウィジェットのモジュール."""

from PySide6.QtWidgets import QWidget, QLineEdit, QSpinBox, QFormLayout

from adapter.controller import Controller
from adapter.presenter import ViewModel
from entity.enemyparameter import EnemyParameter


class ParameterWidget(QWidget):
    """パラメータ設定ウィジェット.

    :param controller: コントローラ
    :param parent: 親ウィジェット
    """

    def __init__(
            self,
            controller: Controller,
            parent: QWidget = None) -> None:
        super().__init__(parent=parent)

        self._controller = controller

        self._create_children()
        self._create_layout()

    def update_view(self, view_model: ViewModel) -> None:
        """ViewModel の内容をもとにビューを更新する.

        :param view_model: ViewModel
        """
        self._name_edit.setText(view_model.name)
        self._hp_spin_box.setValue(view_model.hp)

    def _create_children(self) -> None:
        self._name_edit = QLineEdit('', parent=self)
        self._name_edit.textEdited.connect(self._on_name_edited)

        self._hp_spin_box = QSpinBox(parent=self)
        self._hp_spin_box.setValue(0)
        self._hp_spin_box.setMinimum(EnemyParameter.HP_MIN)
        self._hp_spin_box.setMaximum(EnemyParameter.HP_MAX)
        self._hp_spin_box.valueChanged.connect(self._on_hp_changed)

    def _create_layout(self):
        layout = QFormLayout()
        layout.addRow('名前', self._name_edit)
        layout.addRow('HP', self._hp_spin_box)
        self.setLayout(layout)

    def _on_name_edited(self, text: str) -> None:
        self._controller.set_name(text)

    def _on_hp_changed(self, value: int) -> None:
        self._controller.set_hp(value)
