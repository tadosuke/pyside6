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

    def test_save_and_load(self):
        """保存時にパラメータを渡しているか？"""
        self._interactor.save()

        self._data_access.save.assert_called_once_with(self._interactor._enemy_param)

    def test_load(self):
        """読み込んだデータでパラメータが上書きされるか？"""
        mock_param = EnemyParameter()
        mock_param.name = 'Goblin'
        mock_param.hp = 20

        self._data_access.load.return_value = mock_param
        self._interactor.load()

        param = self._interactor._enemy_param
        self.assertEqual('Goblin', param.name)
        self.assertEqual(20, param.hp)
        self._data_access.load.assert_called_once()

        # output() が呼ばれるか？
        exp_data = OutputData(self._interactor._enemy_param)
        self._mock_output.output.assert_called_once_with(exp_data)


if __name__ == "__main__":
    unittest.main()