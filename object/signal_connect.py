"""シグナルとスロットを接続／切断するサンプル."""

from PySide6.QtCore import QObject, Signal, QMetaMethod


def slot():
    print('slot')

class MyObject(QObject):
    something_done = Signal()

    def do_something(self):
        self.something_done.emit()


obj = MyObject()

# 接続
obj.something_done.connect(slot)

# シグナルが接続されているかを調べる
meta_method = QMetaMethod.fromSignal(obj.something_done)
print(obj.isSignalConnected(meta_method))
#  True

obj.do_something()
#  slot

# 切断
obj.something_done.disconnect(slot)

obj.do_something()
#  (何も表示されない)
print(obj.isSignalConnected(meta_method))
#  False
