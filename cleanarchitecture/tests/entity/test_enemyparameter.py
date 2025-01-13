"""entity.enemyparameter モジュールのテスト."""

import unittest

from entity.enemyparameter import EnemyParameter


class TestEnemyParameter(unittest.TestCase):

    def test_init(self):
        """生成後の状態が正しいか？"""
        enemy = EnemyParameter()
        self.assertEqual(enemy.name, '')
        self.assertEqual(enemy.hp, 0)

    def test_name_within_length(self):
        """名前が8文字以内で設定されるか？"""
        enemy = EnemyParameter()
        enemy.name = "Valid"
        self.assertEqual(enemy.name, "Valid")

    def test_name_too_long(self):
        """名前が8文字を超えている場合にエラーになるか？"""
        enemy = EnemyParameter()
        with self.assertRaises(ValueError):
            enemy.name = "A" * 9

    def test_hp_within_range(self):
        """HPが範囲内で設定されるか？"""
        enemy = EnemyParameter()
        enemy.hp = 5000
        self.assertEqual(enemy.hp, 5000)

    def test_hp_out_of_range(self):
        """HPが最小～最大範囲外の場合にエラーになるか？"""
        enemy = EnemyParameter()
        with self.assertRaises(ValueError):
            enemy.hp = -1
        with self.assertRaises(ValueError):
            enemy.hp = 100000


if __name__ == "__main__":
    unittest.main()