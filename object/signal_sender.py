"""シグナルを送信したオブジェクトについて調べるサンプル."""

from PySide6.QtCore import QObject, Signal


class MySlot(QObject):
    def func(self):
        print(self.sender())
        print(self.senderSignalIndex())


class MyObjectA(QObject):
    signal1 = Signal()
    signal2 = Signal()

    def do_something(self):
        self.signal1.emit()
        self.signal2.emit()

class MyObjectB(QObject):
    signal = Signal()

    def do_something(self):
        self.signal.emit()


slot = MySlot()

obj1 = MyObjectA()
obj1.signal1.connect(slot.func)
obj1.signal2.connect(slot.func)
obj1.do_something()
#  <__main__.MyObjectA(*) at *>
#  5
#  <__main__.MyObjectA(*) at *>
#  6

obj2 = MyObjectB()
obj2.signal.connect(slot.func)
obj2.do_something()
#  <__main__.MyObjectB(*) at *>
#  5
