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

    def test_comparisons(self):
        """比較演算子が正しく機能するか？"""
        hp1 = Hp(50)
        hp2 = Hp(100)
        hp3 = Hp(50)

        self.assertTrue(hp1 == hp3)
        self.assertFalse(hp1 == hp2)
        self.assertTrue(hp1 != hp2)

        self.assertTrue(hp1 < hp2)
        self.assertFalse(hp2 < hp1)

        self.assertTrue(hp1 <= hp3)
        self.assertTrue(hp1 <= hp2)
        self.assertFalse(hp2 <= hp1)

        self.assertTrue(hp2 > hp1)
        self.assertFalse(hp1 > hp2)

        self.assertTrue(hp1 >= hp3)
        self.assertTrue(hp2 >= hp1)
        self.assertFalse(hp1 >= hp2)

    def test_comparison_with_non_hp(self):
        """Hp 以外のクラスと比較しようとした際にエラーが発生するか？"""
        hp = Hp(50)

        with self.assertRaises(TypeError):
            hp == 50

        with self.assertRaises(TypeError):
            hp != 50

        with self.assertRaises(TypeError):
            hp < 50

        with self.assertRaises(TypeError):
            hp <= 50

        with self.assertRaises(TypeError):
            hp > 50

        with self.assertRaises(TypeError):
            hp >= 50


if __name__ == "__main__":
    unittest.main()