"""usecase.interactor モジュールのテスト."""

import unittest
from unittest.mock import MagicMock

from entity.enemyparameter import EnemyParameter
from usecase.interactor import UseCaseInteractor
from usecase.outputboundary import OutputData


class TestUseCaseInteractor(unittest.TestCase):

    def setUp(self):
        self._mock_output = MagicMock()  # 出力を確認するためのモック

    def test_init(self):
        """生成時の状態が正しいか？"""
        use_case = UseCaseInteractor(output=self._mock_output)
        self.assertIsInstance(use_case._enemy_param, EnemyParameter)
        self.assertIs(self._mock_output, use_case._output)

    def test_set_name(self):
        """名前が設定できるか？"""
        use_case = UseCaseInteractor(output=self._mock_output)

        use_case.set_name('Goblin')

        self.assertEqual('Goblin', use_case._enemy_param.name)
        # output() が呼ばれるか？
        exp_data = OutputData(use_case._enemy_param)
        self._mock_output.output.assert_called_once_with(exp_data)

    def test_set_hp(self):
        """HPが設定できるか？"""
        use_case = UseCaseInteractor(output=self._mock_output)

        use_case.set_hp(20)

        self.assertEqual(20, use_case._enemy_param.hp)
        # output() が呼ばれるか？
        exp_data = OutputData(use_case._enemy_param)
        self._mock_output.output.assert_called_once_with(exp_data)

    def test_save(self):
        """保存できるか？"""
        use_case = UseCaseInteractor(output=self._mock_output)
        use_case.save()
        
        # todo


if __name__ == "__main__":
    unittest.main()