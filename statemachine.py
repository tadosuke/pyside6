"""QStateMachine を使った状態遷移のサンプル."""

from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
from PySide6.QtStateMachine import QStateMachine, QState


def on_enter_state1():
    print('enter_state1')


def on_enter_state2():
    print('enter_state2')


def setup_state_machine(button: QPushButton) -> QStateMachine:
    machine = QStateMachine()

    # 状態の定義
    s1 = QState()
    s2 = QState()

    # 各状態に切り替わったとき、ボタンのプロパティを変更する
    s1.assignProperty(button, "text", "Click Me")
    s2.assignProperty(button, "text", "Hello, World!")

    # 各状態に切り替わったとき、指定した関数を呼ぶ
    s1.entered.connect(on_enter_state1)
    s2.entered.connect(on_enter_state2)

    # 状態の遷移条件を追加（ボタンがクリックされたとき）
    s1.addTransition(button.clicked, s2)
    s2.addTransition(button.clicked, s1)

    # StateMachine に状態を追加
    machine.addState(s1)
    machine.addState(s2)

    # 初期状態を設定
    machine.setInitialState(s1)

    # StateMachine の開始
    # 　これを呼ばないと、状態の更新などが起きない
    machine.start()

    return machine


if __name__ == "__main__":
    app = QApplication()

    button = QPushButton()
    layout = QVBoxLayout()
    layout.addWidget(button)

    window = QWidget()
    window.setLayout(layout)

    machine = setup_state_machine(button)

    window.show()
    app.exec()
