"""親オブジェクトを取得／設定するサンプル."""

from PySide6.QtCore import QObject


obj_a = QObject()
obj_a.setObjectName('A')

obj_b = QObject(parent=obj_a)  # B の親を A に設定
obj_b.setObjectName('B')
print(obj_b.parent().objectName())
#  A

obj_c = QObject()
obj_c.setObjectName('C')
obj_b.setParent(obj_c)  # 親を A → C に付け替える
print(obj_b.parent().objectName())
#  C
