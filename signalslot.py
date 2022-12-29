"""Signal & Slot のサンプル."""

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class MainWindow(QWidget):
    """メインウィンドウ."""

    on_changed = Signal(int)

    def __init__(self) -> None:
        super().__init__()

        self._count = 0

        button = QPushButton('Button')
        button.clicked.connect(self._on_button_clicked)

        layout = QVBoxLayout()
        layout.addWidget(button)

        self.setLayout(layout)

    def _on_button_clicked(self) -> None:
        self._count += 1
        self.on_changed.emit(self._count)


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.on_changed.connect(lambda c: print(f'Count={c}'))

    window.show()
    app.exec()
