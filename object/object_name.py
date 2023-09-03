"""オブジェクトの名前を設定／取得するサンプル."""

from PySide6.QtCore import QObject


def _on_object_name_changed(name):
    """オブジェクト名が変更されたときに呼ばれる."""
    print(f'ObjectNameChanged : {name}')


obj = QObject()
obj.objectNameChanged.connect(_on_object_name_changed)  # 変更時のシグナルに接続

obj.setObjectName('A')
#  ObjectNameChanged : A

print(obj.objectName())
#  A
