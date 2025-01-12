"""entities モジュールのテスト."""

import unittest

import entities


class TestEntity(unittest.TestCase):

    def test_init(self):
        """初期状態が正しいか？"""
        self.assertEqual(1, entities.one())


if __name__ == "__main__":
    unittest.main()
