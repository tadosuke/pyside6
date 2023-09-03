"""オブジェクトツリーを出力するサンプル."""

from PySide6.QtCore import QObject


obj_a = QObject()
obj_a.setObjectName('A')

obj_b = QObject(parent=obj_a)
obj_b.setObjectName('B')

obj_c = QObject(parent=obj_a)
obj_c.setObjectName('C')

obj_d = QObject(parent=obj_b)
obj_d.setObjectName('D')

obj_a.dumpObjectTree()
# QObject::A
#     QObject::B
#         QObject::D
#     QObject::C
