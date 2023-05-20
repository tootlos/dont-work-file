from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()
window.setWindowTitle('Memory card')

class Question:
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.q = question
        self.ra = right_answer
        self.w1 = wrong1
        self.w2 = wrong2
        self.w3 = wrong3

ask1 = Question(
    q = 'ok i pull up?',
    ra = 'ok i pull up',
    w1 = 'Ok I Pull Up',
    w2 = 'ok i pull down',
    w3 = 'ok pull i up'
)

ask(ask1)

btn_ok = QPushButton('Ответить')
question_label = QLabel('Какой национальности не существует?')

RadioGroupBox = QGroupBox('Варианты ответов')

rbtn1 = QRadioButton('Энцы')
rbtn2 = QRadioButton('Чулымцы')
rbtn3 = QRadioButton('Смурфы')
rbtn4 = QRadioButton('Алеуты')

layout1 = QHBoxLayout()
layout2 = QVBoxLayout()
layout3 = QVBoxLayout()

layout2.addWidget(rbtn1)
layout2.addWidget(rbtn2)
layout3.addWidget(rbtn3)
layout3.addWidget(rbtn4)
layout1.addLayout(layout2)
layout1.addLayout(layout3)

RadioGroupBox.setLayout(layout1)


layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(question_label, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)

layout_line3.addStretch(1)
layout_line3.addWidget(btn_ok, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addLayout(layout_line3, stretch=2)

layout_card.setSpacing(5)


AnsGroupBox = QGroupBox('Результат теста')
b_result = QLabel('Прав ты или нет?')
c_result = QLabel('ответ будет тут!')

layout_line4 = QVBoxLayout()
layout_line4.addWidget(b_result, alignment = (Qt.AlignLeft | Qt.AlignTop ))

layout_line5 = QHBoxLayout
layout_line5.addWidget(c_result, alignment = (Qt.AlignHCenter | Qt.AlignVcenter))

AnsGroupBox.setLayout(layout_line4)


def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_ok.setText('Следующий вопрос')



def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    btn_ok.setText('Ответить')
    RadioGroupBox.wetExlusive(False)
    rbtn1.setCheched(False)
    rbtn2.setCheched(False)
    rbtn3.setCheched(False)
    rbtn4.setCheched(False)
    RadioGroupBox.setExlusive()


def start_test():
    if btn_ok.text() == 'Ответить':
        show_result()
    else:
        show_question()


# """ док скрин """
answers = [rbtn1, rbtn2, rbtn3, rbtn4]

def ask(q: Question):
    shuffle(answers)
    answers[2].setText(q.ra)
    answers[0].setText(q.w1)
    answers[1].setText(q.w2)
    answers[3].setText(q.w3)
    question_label.setText('')
    correct.setText(q.ra)
    show_question()



window.setLayout(layout_card)
window.show()
app.exec()