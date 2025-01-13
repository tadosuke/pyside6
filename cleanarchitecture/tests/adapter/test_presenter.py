"""adapter.presenter モジュールのテスト."""

import unittest

from adapter.presenter import Presenter, ViewModel
from entity.enemyparameter import EnemyParameter
from usecase.outputboundary import OutputData


class TestPresenter(unittest.TestCase):

    def setUp(self):
        self._called_vm = None

    def test_output(self):
        """渡されたデータにもとづき、ViewModel がシグナルで発火されるか？"""
        def _on_update_view(vm):
            self._called_vm = vm

        presenter = Presenter()
        presenter.update_view.connect(_on_update_view)

        enemy_parameter = EnemyParameter()
        enemy_parameter.name = 'Goblin'
        enemy_parameter.hp = 100
        output_data = OutputData(enemy_parameter)

        presenter.output(output_data)

        exp_vm = ViewModel(enemy_parameter.name, enemy_parameter.hp)
        self.assertEqual(exp_vm, self._called_vm)


if __name__ == "__main__":
    unittest.main()