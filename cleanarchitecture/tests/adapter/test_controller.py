"""adapter.controller モジュールのテスト."""

import unittest
from unittest import mock

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
        """名前を設定時、InputBoundary に入力が渡されるか？"""
        controller = Controller(self._input_boundary)

        with mock.patch.object(self._input_boundary, 'set_name') as mp_set:
            controller.set_name('Goblin')
            mp_set.assert_called_once_with('Goblin')

    def test_set_hp(self):
        """HP 設定時、InputBoundary に入力が渡されるか？"""
        controller = Controller(self._input_boundary)

        with mock.patch.object(self._input_boundary, 'set_hp') as mp_set:
            controller.set_hp(20)
            mp_set.assert_called_once_with(20)


if __name__ == "__main__":
    unittest.main()