"""子オブジェクトを検索するサンプル."""

from PySide6.QtCore import QObject

obj_a = QObject()
obj_a.setObjectName('A')

# 子オブジェクトを追加
obj_b = QObject(parent=obj_a)  # B の親を A に設定
obj_b.setObjectName('B')
obj_c = QObject(parent=obj_a)
obj_c.setObjectName('C')

# 子オブジェクトを一つだけ検索する
print(obj_a.findChild(QObject))
#  最初に登録した B のみが取得される

# QObject タイプの子オブジェクトを全て取得する
print(obj_a.findChildren(QObject))
#  B, C が取得される

# 名前が「C」の QObject を検索する
print(obj_a.findChildren(QObject, name='C'))
#  C のみが取得される
