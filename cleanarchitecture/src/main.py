"""アプリケーションのエントリポイント."""

from PySide6.QtWidgets import QApplication

from view import MainWindow


def main():
    """エントリポイント."""
    app = QApplication()
    window = MainWindow()

    window.show()
    app.processEvents()
    app.exec()


if __name__ == "__main__":
    main()