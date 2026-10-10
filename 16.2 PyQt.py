import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
                             QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


QUESTIONS = [
    {
        "question": "Из какого материала делали мечи в Древней Греции?",
        "options": ["Железо", "Бронза", "Сталь", "Кость"],
        "correct": "Бронза"
    },
    {
        "question": "Какова была длина сариссы — копья македонской фаланги?",
        "options": ["1-2 метра", "2-3 метра", "4-6 метров", "8-10 метров"],
        "correct": "4-6 метров"
    },
    {
        "question": "В какой стране появилась алебарда?",
        "options": ["Франция", "Швейцария", "Италия", "Англия"],
        "correct": "Швейцария"
    },
    {
        "question": "Какова примерная длина английского длинного лука?",
        "options": ["1 метр", "1.2-1.4 метра", "1.8-2 метра", "2.5-3 метра"],
        "correct": "1.8-2 метра"
    },
    {
        "question": "Что такое аркебуза?",
        "options": [
            "Метательное копьё",
            "Раннее огнестрельное оружие",
            "Тип щита",
            "Разновидность меча"
        ],
        "correct": "Раннее огнестрельное оружие"
    },
    {
        "question": "В какой стране появился мушкет?",
        "options": ["Испания", "Германия", "Османская империя", "Италия"],
        "correct": "Испания"
    },
    {
        "question": "Как назывался круглый щит древнегреческого гоплита?",
        "options": ["Скутум", "Аспис", "Парма", "Клипеус"],
        "correct": "Аспис"
    },
    {
        "question": "Из чего изготавливали тетиву для арбалета в Средневековье?",
        "options": ["Лён", "Конский волос", "Кишки животных", "Хлопок"],
        "correct": "Кишки животных"
    }
]


class QuizApp(QWidget):
    def __init__(self):
        super().__init__()
        self.current = 0
        self.score = 0
        self.initUI()
        self.show_question()

    def initUI(self):
        self.setWindowTitle("Викторина: Историческое оружие")
        self.setGeometry(300, 300, 550, 400)

        layout = QVBoxLayout()

        self.label_score = QLabel("Вопрос 1 из 8 | Счёт: 0")
        self.label_score.setFont(QFont("Arial", 10))
        self.label_score.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label_score)

        self.label_question = QLabel()
        font = QFont("Arial", 13)
        font.setBold(True)
        self.label_question.setFont(font)
        self.label_question.setAlignment(Qt.AlignCenter)
        self.label_question.setWordWrap(True)
        layout.addWidget(self.label_question)

        self.buttons = []
        for i in range(4):
            btn = QPushButton()
            btn.setFont(QFont("Arial", 11))
            btn.setMinimumHeight(40)
            btn.clicked.connect(lambda checked, b=btn: self.check_answer(b))
            layout.addWidget(btn)
            self.buttons.append(btn)

        self.btn_next = QPushButton("Следующий вопрос →")
        self.btn_next.setFont(QFont("Arial", 11))
        self.btn_next.setMinimumHeight(40)
        self.btn_next.clicked.connect(self.next_question)
        self.btn_next.hide()
        layout.addWidget(self.btn_next)

        self.setLayout(layout)

    def show_question(self):
        q = QUESTIONS[self.current]
        self.label_score.setText(
            f"Вопрос {self.current + 1} из {len(QUESTIONS)} | Счёт: {self.score}"
        )
        self.label_question.setText(q["question"])

        for i, option in enumerate(q["options"]):
            self.buttons[i].setText(option)
            self.buttons[i].setStyleSheet("")
            self.buttons[i].setEnabled(True)

        self.btn_next.hide()

    def check_answer(self, clicked_button):
        q = QUESTIONS[self.current]
        correct = q["correct"]

        for btn in self.buttons:
            btn.setEnabled(False)
            if btn.text() == correct:
                btn.setStyleSheet("background-color: #4CAF50; color: white;")

        if clicked_button.text() == correct:
            self.score += 1
        else:
            clicked_button.setStyleSheet("background-color: #e53935; color: white;")

        self.label_score.setText(
            f"Вопрос {self.current + 1} из {len(QUESTIONS)} | Счёт: {self.score}"
        )
        self.btn_next.show()

        if self.current == len(QUESTIONS) - 1:
            self.btn_next.setText("Показать результат →")

    def next_question(self):
        self.current += 1

        if self.current >= len(QUESTIONS):
            self.show_result()
            return

        self.show_question()

    def show_result(self):
        self.label_question.setText(
            f"Викторина завершена!\n\nВаш результат: {self.score} из {len(QUESTIONS)}"
        )

        for btn in self.buttons:
            btn.hide()

        self.btn_next.setText("Пройти заново")
        self.btn_next.clicked.disconnect()
        self.btn_next.clicked.connect(self.restart)
        self.btn_next.show()

    def restart(self):
        self.current = 0
        self.score = 0

        for btn in self.buttons:
            btn.show()

        self.btn_next.setText("Следующий вопрос →")
        self.btn_next.clicked.disconnect()
        self.btn_next.clicked.connect(self.next_question)

        self.show_question()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QuizApp()
    window.show()
    sys.exit(app.exec_())