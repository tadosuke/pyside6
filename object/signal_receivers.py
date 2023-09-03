"""シグナルに接続されているスロットの数を取得するサンプル."""

from PySide6.QtCore import QObject, Signal, SIGNAL


def slot1():
    pass

def slot2():
    pass

def slot3():
    pass


class MyObject(QObject):
    my_signal = Signal()

obj = MyObject()
obj.my_signal.connect(slot1)
obj.my_signal.connect(slot2)
obj.my_signal.connect(slot3)

print(obj.receivers(SIGNAL('my_signal()')))
#  3
