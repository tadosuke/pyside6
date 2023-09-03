"""子オブジェクトを取得するサンプル."""

from PySide6.QtCore import QObject

parent = QObject()
child1 = QObject(parent=parent)
child2 = QObject(parent=parent)

print(parent.children())
#  [child1, child2]
