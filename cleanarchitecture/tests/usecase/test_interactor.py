"""usecase.interactor モジュールのテスト."""

import unittest
from unittest import mock
from unittest.mock import Mock

from usecase.inputboundary import InputData
from usecase.interactor import UseCaseInteractor


class TestUseCaseInteractor(unittest.TestCase):

    def setUp(self):
        self.mock_output = Mock()  # 出力を確認するためのモック

    def test_input_enemy_parameter_registered(self):
        """エネミー情報が登録されるか？"""
        use_case = UseCaseInteractor(output=self.mock_output)
        input_data = InputData(name="Goblin", hp=100)

        use_case.input(input_data)

        param = use_case._enemy_param_dict["Goblin"]
        self.assertEqual("Goblin", param.name)
        self.assertEqual(100, param.hp)

    def test_input_enemy_parameter_overwrites(self):
        """登録済みのエネミー情報が上書きされるか？"""
        use_case = UseCaseInteractor(output=self.mock_output)
        input_data1 = InputData(name="Orc", hp=150)
        use_case.input(input_data1)

        input_data2 = InputData(name="Orc", hp=200)
        use_case.input(input_data2)

        self.assertEqual(1, len(use_case._enemy_param_dict))
        param = use_case._enemy_param_dict["Orc"]
        self.assertEqual(200, param.hp)


if __name__ == "__main__":
    unittest.main()