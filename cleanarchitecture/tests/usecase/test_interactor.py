"""usecase.interactor モジュールのテスト."""

import unittest
from unittest.mock import MagicMock

from entity.enemyparameter import EnemyParameter
from usecase.interactor import UseCaseInteractor
from usecase.outputboundary import OutputData


class TestUseCaseInteractor(unittest.TestCase):

    def setUp(self):
        self._data_access = MagicMock()  # データアクセスを確認するためのモック
        self._mock_output = MagicMock()  # 出力を確認するためのモック
        self._interactor = UseCaseInteractor(self._data_access, output=self._mock_output)

    def test_init(self):
        """生成時の状態が正しいか？"""
        self.assertIsInstance(self._interactor._enemy_param, EnemyParameter)
        self.assertIs(self._mock_output, self._interactor._output)

    def test_set_name(self):
        """名前が設定できるか？"""
        self._interactor.set_name('Goblin')

        self.assertEqual('Goblin', self._interactor._enemy_param.name)
        # output() が呼ばれるか？
        exp_data = OutputData(self._interactor._enemy_param)
        self._mock_output.output.assert_called_once_with(exp_data)

    def test_set_hp(self):
        """HPが設定できるか？"""
        self._interactor.set_hp(20)

        self.assertEqual(20, self._interactor._enemy_param.hp)
        # output() が呼ばれるか？
        exp_data = OutputData(self._interactor._enemy_param)
        self._mock_output.output.assert_called_once_with(exp_data)

    def test_save(self):
        """保存時に DataAccessInterface の関数が呼ばれるか？"""
        self._interactor.save()

        self._data_access.save.assert_called_once()

    def test_load(self):
        """読込時に DataAccessInterface の関数が呼ばれるか？"""
        self._interactor.load()

        self._data_access.load.assert_called_once()


if __name__ == "__main__":
    unittest.main()