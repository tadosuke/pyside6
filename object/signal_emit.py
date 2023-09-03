"""シグナルを手動で発行するサンプル."""

from PySide6.QtWidgets import QPushButton, QApplication


class MyButton(QPushButton):
    def __init__(self):
        super().__init__('Button')

    def emulate_click(self):
        """クリックしたことにする."""
        self.clicked.emit()

def _on_clicked():
    print('clicked')


app = QApplication()
button = MyButton()
button.clicked.connect(_on_clicked)
button.emulate_click()
# クリックしていなくても「clicked」が出力される
