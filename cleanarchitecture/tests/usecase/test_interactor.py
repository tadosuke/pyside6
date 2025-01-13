"""usecase.interactor モジュールのテスト."""

import unittest
from unittest.mock import Mock

from entity.enemyparameter import EnemyParameter
from usecase.interactor import UseCaseInteractor


class TestUseCaseInteractor(unittest.TestCase):

    def setUp(self):
        self.mock_output = Mock()  # 出力を確認するためのモック

    def test_init(self):
        """生成時の状態が正しいか？"""
        use_case = UseCaseInteractor(output=self.mock_output)
        self.assertIsInstance(use_case._enemy_param, EnemyParameter)

    def test_set_name(self):
        """名前が設定できるか？"""
        use_case = UseCaseInteractor(output=self.mock_output)

        use_case.set_name('Goblin')

        self.assertEqual('Goblin', use_case._enemy_param.name)

    def test_set_hp(self):
        """HPが設定できるか？"""
        use_case = UseCaseInteractor(output=self.mock_output)

        use_case.set_hp(20)

        self.assertEqual(20, use_case._enemy_param.hp)


if __name__ == "__main__":
    unittest.main()