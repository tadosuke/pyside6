"""infrastructure.mainwindow モジュールのテスト."""

import unittest
from unittest import mock
from unittest.mock import MagicMock

from PySide6.QtWidgets import QApplication

from adapter.presenter import ViewModel
from infrastructure.mainwindow import MainWindow
from infrastructure.parameterwidget import ParameterWidget


_IS_SHOW = False  # 表示テストを行うか？


class TestMainWindow(unittest.TestCase):

    def setUp(self):
        self._app = QApplication.instance() or QApplication([])
        self._controller = MagicMock()
        self._presenter = MagicMock()
        self._window = MainWindow(self._controller, self._presenter)

    def tearDown(self):
        self._window.deleteLater()
        self._app.quit()

    def test_init(self):
        """生成後の状態が正しいか？"""
        self.assertEqual(self._controller, self._window._controller)
        self.assertEqual(self._presenter, self._window._presenter)
        self.assertIsInstance(self._window._parameter_widget, ParameterWidget)

        if _IS_SHOW:
            self._window.show()
            self._app.exec()

    def test_update_view(self):
        """子ウィジェットの更新処理が呼ばれるか？"""
        vm = ViewModel(name='Goblin', hp=10)
        with mock.patch.object(self._window._parameter_widget, 'update_view') as mp_update:
            self._window._update_view(vm)
            mp_update.assert_called_once_with(vm)


if __name__ == "__main__":
    unittest.main()