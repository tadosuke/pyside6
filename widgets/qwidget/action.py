"""アクションを設定/取得/削除する."""

from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # アクションを生成する
        exit_action = QAction('Exit', self)
        exit_action.triggered.connect(self.close)  # アクション実行時にウィンドウを閉じる

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('File')
        file_menu.addAction(exit_action)  # メニューにアクションを追加

        # file_menu.removeAction(exit_action)  # アクションを削除
        print(f'{file_menu.actions()=}')  # アクションを取得


app = QApplication()
main_window = MainWindow()
main_window.show()
app.exec()
