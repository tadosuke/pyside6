"""シグナルとスロットを接続／切断するサンプル."""

from PySide6.QtCore import QObject, Signal, QMetaMethod


def slot():
    pass

class MyObject(QObject):
    my_signal = Signal()


obj = MyObject()
obj.my_signal.connect(slot)

meta_method = QMetaMethod.fromSignal(obj.my_signal)
print(obj.isSignalConnected(meta_method))
#  True

obj.my_signal.disconnect(slot)
print(obj.isSignalConnected(meta_method))
#  False
