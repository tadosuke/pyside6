"""entity.enemyparameter モジュールのテスト."""

import unittest

from entity.enemyparameter import EnemyParameter


class TestEnemyParameter(unittest.TestCase):

    def test_init(self):
        """生成後の状態が正しいか？"""
        param = EnemyParameter('Goblin')
        self.assertEqual('Goblin', param.name)
        self.assertEqual(0, param.hp)

    def test_name_too_long(self):
        """名前が8文字を超えている場合にエラーになるか？"""
        with self.assertRaises(ValueError):
            EnemyParameter(name="SuperGoblin", hp=100)

    def test_hp_below_min(self):
        """HPが範囲外の場合にエラーになるか？"""
        with self.assertRaises(ValueError):
            EnemyParameter(name="Goblin", hp=-1)

        with self.assertRaises(ValueError):
            EnemyParameter(name="Goblin", hp=100000)


if __name__ == "__main__":
    unittest.main()