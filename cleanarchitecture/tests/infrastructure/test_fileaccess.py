"""infrastructure.fileaccess モジュールのテスト."""

import os
import unittest

from entity.enemyparameter import EnemyParameter
from infrastructure.fileaccess import FileAccess


_FILE_NAME = "enemy_param.json"


class TestFileAccess(unittest.TestCase):

    def setUp(self):
        self._file_access = FileAccess()

    def tearDown(self):
        # 出力したファイルを削除
        if os.path.exists(_FILE_NAME):
            os.remove(_FILE_NAME)

    def test_init(self):
        """生成時の状態が正しいか？"""
        f = FileAccess()
        self.assertIsInstance(f, FileAccess)

    def test_save_and_load(self):
        """save と load メソッドのテスト."""
        param = EnemyParameter()
        param.name = "Goblin"
        param.hp = 150

        # save
        self._file_access.save(param)
        self.assertTrue(os.path.exists(_FILE_NAME))

        # load
        loaded_param = self._file_access.load()
        self.assertEqual(loaded_param.name, param.name)
        self.assertEqual(loaded_param.hp, param.hp)

    def test_load_failed(self):
        """読み込みに失敗したとき、空のパラメータを返すか？"""
        loaded_param = self._file_access.load()
        self.assertEqual('', loaded_param.name)
        self.assertEqual(0, loaded_param.hp)


if __name__ == "__main__":
    unittest.main()