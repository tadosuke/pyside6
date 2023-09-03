"""シグナルの発行を一時的に抑えるサンプル."""

from PySide6.QtCore import QObject, Signal


def _on_done():
    print('done')


class MyObject(QObject):

    done = Signal()

    def do_something(self):
        self.done.emit()


my_obj = MyObject()
my_obj.done.connect(_on_done)

print(my_obj.signalsBlocked())
#  False

my_obj.do_something()
#  done

# シグナルをブロック
my_obj.blockSignals(True)
print(my_obj.signalsBlocked())
#  True

my_obj.do_something()
#  (何も出ない)
