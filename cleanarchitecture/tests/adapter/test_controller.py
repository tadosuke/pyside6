"""adapter.controller モジュールのテスト."""

import unittest

from adapter.controller import Controller
from usecase.inputboundary import InputBoundary
from usecase.interactor import UseCaseInteractor


class TestController(unittest.TestCase):

    def setUp(self) -> None:
        self._input_boundary = UseCaseInteractor()

    def test_init(self):
        """生成時の状態が正しいか？"""
        controller = Controller(self._input_boundary)

        self.assertIsInstance(controller._input_boundary, InputBoundary)

    def test_set_name(self):
        """名前を設定できるか？"""
        controller = Controller(self._input_boundary)
        controller.set_name('Goblin')

        # todo

    def test_set_hp(self):
        """HP を設定できるか？"""
        controller = Controller(self._input_boundary)
        controller.set_hp(20)

        # todo


if __name__ == "__main__":
    unittest.main()