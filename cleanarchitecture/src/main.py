"""アプリケーションのエントリポイント."""

from PySide6.QtWidgets import QApplication

from adapter.controller import Controller
from adapter.presenter import Presenter
from infrastructure.fileaccess import FileAccess
from infrastructure.mainwindow import MainWindow
from usecase.interactor import UseCaseInteractor


def main():
    """エントリポイント."""
    app = QApplication()

    file_access = FileAccess()
    presenter = Presenter()
    usecase_interactor = UseCaseInteractor(file_access, output=presenter)
    controller = Controller(usecase_interactor)

    view = MainWindow(controller, presenter)
    view.show()
    app.exec()


if __name__ == "__main__":
    main()
