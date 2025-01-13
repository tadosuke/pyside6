"""アプリケーションのエントリポイント."""

from PySide6.QtWidgets import QApplication

from adapter.controller import Controller
from adapter.presenter import Presenter
from infrastructure.mainwindow import MainWindow
from usecase.interactor import UseCaseInteractor


def main():
    """エントリポイント."""
    app = QApplication()

    presenter = Presenter()
    usecase_interactor = UseCaseInteractor(presenter)
    controller = Controller(usecase_interactor)

    view = MainWindow(controller, presenter)
    view.show()
    app.exec()


if __name__ == "__main__":
    main()