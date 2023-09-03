"""指定クラスを継承しているかを調べる."""

from PySide6.QtWidgets import QWidget, QApplication, QPushButton

app = QApplication()

widget = QWidget()
button = QPushButton('Button')

print(widget.inherits('QObject'))
#  True
print(button.inherits('QWidget'))
#  True
print(button.inherits('QObject'))  # 親の親でも判定可能
#  True
print(widget.inherits('QPushButton'))
#  False
