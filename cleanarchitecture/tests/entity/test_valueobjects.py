"""entity.valueobject モジュールのテスト."""

import unittest

from entity.valueobjects import Hp


class TestHp(unittest.TestCase):

    def test_init(self):
        """有効な値で初期化できるか？"""
        hp = Hp(5000)
        self.assertEqual(hp.value, 5000)

        hp = Hp(Hp.MIN)
        self.assertEqual(hp.value, Hp.MIN)

        hp = Hp(Hp.MAX)
        self.assertEqual(hp.value, Hp.MAX)

    def test_init_error(self):
        """最小/最大範囲外の値で初期化すると ValueError が発生するか？"""
        with self.assertRaises(ValueError):
            Hp(Hp.MIN - 1)

        with self.assertRaises(ValueError):
            Hp(Hp.MAX + 1)


if __name__ == "__main__":
    unittest.main()