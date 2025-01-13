"""infrastructure.parameterwidget モジュールのテスト."""

import unittest

from PySide6.QtWidgets import QApplication

from adapter.presenter import ViewModel
from entity.enemyparameter import EnemyParameter
from infrastructure.parameterwidget import ParameterWidget


_IS_SHOW = False  # 表示テストを行うか？


class TestParameterWidget(unittest.TestCase):

    def setUp(self):
        self.app = QApplication.instance() or QApplication([])
        self.widget = ParameterWidget()

    def tearDown(self):
        self.widget.deleteLater()
        self.app.quit()

    def test_init(self):
        """生成後の状態が正しいか？"""
        # name
        self.assertEqual('', self.widget._name_edit.text())

        # hp
        self.assertEqual(0, self.widget._hp_spin_box.value())
        self.assertEqual(EnemyParameter.HP_MIN, self.widget._hp_spin_box.minimum())
        self.assertEqual(EnemyParameter.HP_MAX, self.widget._hp_spin_box.maximum())

        if _IS_SHOW:
            self.widget.show()
            self.app.exec()

    def test_update_view(self):
        """ViewModel の内容に応じて表示が更新されるか？"""
        view_model = ViewModel(name="Goblin", hp=50)

        self.widget.update_view(view_model)

        self.assertEqual("Goblin", self.widget._name_edit.text())
        self.assertEqual(50, self.widget._hp_spin_box.value())


if __name__ == "__main__":
    unittest.main()