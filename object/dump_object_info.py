"""オブジェクトのデバッグ情報を出力するサンプル."""

from PySide6.QtCore import QObject, Signal


class MyObject(QObject):
    signal = Signal()
    def __init__(self):
        super().__init__()
        self.value = 1

def slot():
    pass

obj = MyObject()
obj.signal.connect(slot)

obj.dumpObjectInfo()
# OBJECT MyObject::unnamed
#   SIGNALS OUT
#         signal: signal()
#           --> __GlobalReceiver__::unnamed slot29559d86480()
#   SIGNALS IN
#         <None>
