from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import shuffle

class Question:

    def __init__(self, question, right_answer, 
                wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

app = QApplication([])
# Создаем панель вопроса
btn_OK = QPushButton('Нажми на меня')
lb_Question = QLabel('ТЫквенные семечки')

questions = [
    Question('Масква сазданье', '1147', '1234', '111', '11111'),
    Question('Масква  время жизьни', '875', '2222', '222', '22222'),
    Question('Масква зарпата(в руплях)', '136401', '333333', '111111', '124508'),
    Question('Самый умный герой в доте', 'Огр маг', 'Рубик', 'антимаг', 'снайпер'),
]

questionNumber = -1
lb_Question = QLabel(questions[questionNumber].question)

RadioGroupBox = QGroupBox("")

rbtn_1 = QRadioButton(questions[questionNumber].right_answer)
rbtn_2 = QRadioButton(questions[questionNumber].wrong1)
rbtn_3 = QRadioButton(questions[questionNumber].wrong2)
rbtn_4 = QRadioButton(questions[questionNumber].wrong3)

answersQuest = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
shuffle(answersQuest)

layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # два ответа в первый столбец
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # два ответа во второй столбец
layout_ans3.addWidget(rbtn_4)


layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)


RadioGroupBox.setLayout(layout_ans1)
# Создаем панель результата
AnsGroupBox = QGroupBox("правельна - про, ниправельна - нуб")
lb_Result = QLabel('йцукен') # здесь размещается надпись "правильно" или "неправильно"
lb_Correct = QLabel('красавчек') # здесь будет написан текст правильного ответа


layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)


# Размещаем все виджеты в окне:
layout_line1 = QHBoxLayout() # вопрос
layout_line2 = QHBoxLayout() # варианты ответов или результат теста
layout_line3 = QHBoxLayout() # кнопка "Ответить"


layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
# Размещаем в одной строке обе панели, одна из них будет скрываться, другая показываться:
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # кнопка должна быть большой
layout_line3.addStretch(1)

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

def check_answer():
    if answersQuest[0].isChecked():
        return True
    return False

def next_question():
    global questionNumber
    questionNumber = (questionNumber + 1) % len(answersQuest)
    lb_Question.setText(questions[questionNumber].question)
    shuffle(answersQuest)
    answersQuest[0].setText((questions[questionNumber].right_answer))
    answersQuest[1].setText(questions[questionNumber].wrong1)
    answersQuest[2].setText(questions[questionNumber].wrong2)
    answersQuest[3].setText(questions[questionNumber].wrong3)

def show_answer():
    if btn_OK.text() == 'Нажми на меня':
        btn_OK.setText('следующая поПЫТКА')
        RadioGroupBox.hide()
        AnsGroupBox.show()
        if check_answer():
            lb_Result.setText('што, ты читир')
            btn_OK.setText('давай ищо вапрос')
        else:
            lb_Result.setText('нет, лошара')
            lb_Correct.setText(f"Правельно {answersQuest[0].text()}")
    else:
        btn_OK.setText("Нажми на меня")
        RadioGroupBox.show()
        AnsGroupBox.hide()
        RadioGroup.setExclusive(False)
        rbtn_1.setChecked(False)
        rbtn_2.setChecked(False)
        rbtn_3.setChecked(False)
        rbtn_4.setChecked(False)
        next_question()


# Теперь созданные строки разместим друг под другой:
layout_card = QVBoxLayout()


layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробелы между содержимым
AnsGroupBox.hide()

btn_OK.clicked.connect(show_answer)

rbtn_1.clicked.connect
next_question()
window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Тест, на которого атветав не будит!')
window.resize(600,300)



window.show()
app.exec()