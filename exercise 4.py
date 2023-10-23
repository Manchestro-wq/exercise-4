from PyQt5.QtWidgets import QApplication,QWidget, QLabel, QRadioButton, QMessageBox

app = QApplication([])
win=QWidget()

win.setWindowTitle("Конкурс від Афріканських Хлоп'ят")
win.resize(400, 200)
win.move(100,100)

text=QLabel(win)
text.setText('Скільки я взяв в плен дітей')
text.move(50, 10)

button1 = QRadioButton(win)
button1.setText('1945')
button1.move(100,60)

button2 = QRadioButton(win)
button2.setText('2001')
button2.move(200,60)

button3 = QRadioButton(win)
button3.setText('2023')
button3.move(100,120)

button4 = QRadioButton(win)
button4.setText('1991')
button4.move(200,120)

def show_win():
    box = QMessageBox()
    box.setText('Правильно!')
    box.exec_()

def show_lose():
    box = QMessageBox()
    box.setText('Неправильно')
    box.exec_()

button1.clicked.connect(show_lose)
button2.clicked.connect(show_win)
button3.clicked.connect(show_lose)
button4.clicked.connect(show_lose)

win.show()
app.exec()