"""ドラッグ＆ドロップ."""

from PySide6.QtGui import QDragEnterEvent, QDropEvent
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QMessageBox


class DropArea(QWidget):
    """ドロップを受け入れるウィジェット."""

    def __init__(self):
        super().__init__()

        self.setAcceptDrops(True)  # ウィジェットがドロップ操作を受け入れるように設定

        self.label = QLabel("ファイルをドロップ")
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

    def dragEnterEvent(self, event: QDragEnterEvent):
        """ドラッグされた時に呼ばれます."""
        # URL（ファイルパス）が含まれていたら処理
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        """ドロップされた時に呼ばれます."""
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()

            # ファイルパスをメッセージボックスで表示
            msg = QMessageBox()
            msg.setText(file_path)
            msg.exec()


app = QApplication()

drop_area = DropArea()
drop_area.show()

app.exec()
