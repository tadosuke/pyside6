"""シグナルの発火を一時的に抑えるサンプル."""

from PySide6.QtCore import QObject, Signal


class Hero(QObject):
    attacked = Signal()


class Monster(QObject):
    def react(self):
        print("Monster: 攻撃された！")


hero = Hero()
monster = Monster()

# シグナルとスロットを接続
hero.attacked.connect(monster.react)

# シグナルを一時的にブロック
hero.blockSignals(True)

# シグナルを発行
hero.attacked.emit()
#  (何も出力されない)

# シグナルのブロックを解除
hero.blockSignals(False)

# シグナルを再度発行
hero.attacked.emit()
#  Monster: 攻撃された！
