"""ウィジェットかウィンドウかを調べるサンプル."""

from PySide6 import QtGui, QtWidgets
from PySide6.QtWidgets import QApplication


app = QApplication()

main_window = QtWidgets.QMainWindow()
print(main_window.isWidgetType())
print(main_window.isWindowType())
#  True, False

gui_window = QtGui.QWindow()
print(gui_window.isWidgetType())
print(gui_window.isWindowType())
#  False, True
