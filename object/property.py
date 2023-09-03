"""Qt の Property を取得・設定するサンプル."""

from PySide6.QtCore import QObject, Property


class MyObject(QObject):
    def __init__(self):
        super().__init__()
        self._a = 1

    def get_a(self):
        return self._a

    def set_a(self, value):
        self._a = value

    property_a = Property(int, get_a, set_a)


obj = MyObject()

# プロパティを取得
print(obj.property('property_a'))
#  1

# 動的プロパティを追加
obj.setProperty('property_b', 'hoge')

# 動的に追加されたプロパティも取得できる
print(obj.property('property_b'))
#  hoge

# 動的プロパティの名前だけを取得する
for name in obj.dynamicPropertyNames():
    # dynamicPropertyNames は QByteArray を返すので、
    # 文字列表示するために変換
    print(bytes(name).decode())
#  property_b
