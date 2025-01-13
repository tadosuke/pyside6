"""infrastructure.parameterwidget モジュールのテスト."""

import unittest
from unittest.mock import MagicMock

from PySide6.QtWidgets import QApplication

from adapter.presenter import ViewModel
from entity.enemyparameter import EnemyParameter
from infrastructure.parameterwidget import ParameterWidget


_IS_SHOW = False  # 表示テストを行うか？


class TestParameterWidget(unittest.TestCase):

    def setUp(self):
        self._app = QApplication.instance() or QApplication([])
        self._controlelr = MagicMock()
        self._widget = ParameterWidget(self._controlelr)

    def tearDown(self):
        self._widget.deleteLater()
        self._app.quit()

    def test_init(self):
        """生成後の状態が正しいか？"""
        # name
        self.assertEqual('', self._widget._name_edit.text())

        # hp
        self.assertEqual(0, self._widget._hp_spin_box.value())
        self.assertEqual(EnemyParameter.HP_MIN, self._widget._hp_spin_box.minimum())
        self.assertEqual(EnemyParameter.HP_MAX, self._widget._hp_spin_box.maximum())

        if _IS_SHOW:
            self._widget.show()
            self._app.exec()

    def test_update_view(self):
        """ViewModel の内容に応じて表示が更新されるか？"""
        view_model = ViewModel(name="Goblin", hp=50)

        self._widget.update_view(view_model)

        self.assertEqual("Goblin", self._widget._name_edit.text())
        self.assertEqual(50, self._widget._hp_spin_box.value())


if __name__ == "__main__":
    unittest.main()