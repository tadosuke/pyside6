"""ウィジェットに名前をつける."""

from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget

app = QApplication([])

label1 = QLabel("Label 1")
label2 = QLabel("Label 2")

# ウィジェットに名前を設定
label1.setObjectName("important_label")
label2.setObjectName("normal_label")

# 名前を取得
print(label1.objectName())
print(label2.objectName())

# 名前を指定してスタイルシートを設定
app.setStyleSheet("""
    QLabel#important_label {
        font-size: 18px;
        font-weight: bold;
        color: red;
    }

    QLabel#normal_label {
        font-size: 14px;
        color: blue;
    }
""")

layout = QVBoxLayout()
layout.addWidget(label1)
layout.addWidget(label2)
widget = QWidget()
widget.setLayout(layout)
widget.show()

# 名前を指定して子ウィジェットを検索
w = widget.findChild(QLabel, 'important_label')
print(w.text())

app.exec()
