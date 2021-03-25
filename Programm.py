import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from main2 import Ui_Form
import math
import time

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()

symbol = ''
view_numbers = ''
num_1 = ''
num_2 = ''

def button_0():
    global view_numbers
    global num_1
    view_numbers = view_numbers + '0'
    ui.lineEdit.setText(view_numbers) #Вывод текста

ui.pushButton_0.clicked.connect(button_0)


def button_1():
    global view_numbers
    global num_1
    view_numbers = view_numbers + '1'
    ui.lineEdit.setText(view_numbers) #Вывод текста
    num1 = num_1 + '1'

ui.pushButton_1.clicked.connect(button_1)


def button_2():
    global view_numbers
    global num_1
    view_numbers = view_numbers + '2'
    ui.lineEdit.setText(view_numbers) #Вывод текста
    num1 = num_1 + '2'

ui.pushButton_2.clicked.connect(button_2)


def button_3():
    global view_numbers
    global num_1
    view_numbers = view_numbers + '3'
    ui.lineEdit.setText(view_numbers) #Вывод текста
    num1 = num_1 + '3'

ui.pushButton_3.clicked.connect(button_3)


def button_4():
    global view_numbers
    global num_1
    view_numbers = view_numbers + '4'
    ui.lineEdit.setText(view_numbers) #Вывод текста
    num1 = num_1 + '4'

ui.pushButton_4.clicked.connect(button_4)


def button_5():
    global view_numbers
    global num_1
    view_numbers = view_numbers + '5'
    ui.lineEdit.setText(view_numbers) #Вывод текста
    num1 = num_1 + '5'

ui.pushButton_5.clicked.connect(button_5)


def button_6():
    global view_numbers
    global num_1
    view_numbers = view_numbers + '6'
    ui.lineEdit.setText(view_numbers) #Вывод текста
    num1 = num_1 + '6'

ui.pushButton_6.clicked.connect(button_6)


def button_7():
    global view_numbers
    global num_1
    view_numbers = view_numbers + '7'
    ui.lineEdit.setText(view_numbers) #Вывод текста
    num1 = num_1 + '7'

ui.pushButton_7.clicked.connect(button_7)


def button_8():
    global view_numbers
    global num_1
    view_numbers = view_numbers + '8'
    ui.lineEdit.setText(view_numbers) #Вывод текста
    num1 = num_1 + '8'

ui.pushButton_8.clicked.connect(button_8)


def button_9():
    global view_numbers
    global num_1
    view_numbers = view_numbers + '9'
    ui.lineEdit.setText(view_numbers) #Вывод текста
    num1 = num_1 + '9'

ui.pushButton_9.clicked.connect(button_9)


def backspace():
    global view_numbers
    global num_1
    view_numbers = view_numbers[0:-1]
    ui.lineEdit.setText(view_numbers)
    num_1 = num_1[0:-1]

ui.pushButton_nazad.clicked.connect(backspace)

def delete():
    global view_numbers
    global num_1
    global num_2
    view_numbers = ''
    ui.lineEdit.setText(view_numbers)
    num_1 = ''
    num_2 = ''

ui.pushButton_del.clicked.connect(delete)


def percent():
    global view_numbers
    global num_1
    if float(view_numbers) < 0 or '+' in view_numbers or '-' in view_numbers \
            or 'x' in view_numbers or '/' in view_numbers:
        ui.lineEdit.setText('Ошибка')
    else:
        num_1 = float(view_numbers)
        num_1 = num_1 * 0.01
        num_1 = str(num_1)
        view_numbers = num_1
        ui.lineEdit.setText(view_numbers)

ui.pushButton_percent.clicked.connect(percent)


def factorial():
    global view_numbers
    global num_1
    if '+' in view_numbers or '-' in view_numbers \
            or 'x' in view_numbers or '/' in view_numbers:
        ui.lineEdit.setText('Ошибка')
    else:
        if float(view_numbers) < 0:
            ui.lineEdit.setText('Число меньше нуля')
        else:
            try:
                fact = 1
                i = int(view_numbers)
                while i > 0:
                    fact = fact * i
                    i -= 1
                num_1 = str(fact)
                view_numbers = num_1
                ui.lineEdit.setText(view_numbers)
            except:
                ui.lineEdit.setText('Вероятно, число нецелое')

ui.pushButton_voskl.clicked.connect(factorial)


def close():
    q = 'УПС'
    ui.lineEdit.setText(q)
    time.sleep(0.5)
    sys.exit(app.exec_())

ui.pushButton_14.clicked.connect(close)


# def plus():
#     global num_1
#     global view_numbers
#     global num_2
#     num_1 = float(view_numbers)
#     view_numbers = view_numbers + ' + '
#     ui.lineEdit.setText(view_numbers)
#
# ui.pushButton_plus.clicked.connect(plus)


def point():
    global num_1
    global view_numbers
    global num_2
    if '.' in num_1:
        pass
    else:
        num_1 += '.'
        view_numbers += '.'
        ui.lineEdit.setText(view_numbers)

ui.pushButton_tochka.clicked.connect(point)


def division():
    global num_1
    global view_numbers
    global num_2
    global symbol
    if '+' in view_numbers or '-' in view_numbers[2:] \
            or 'x' in view_numbers or '/' in view_numbers:
        pass
    else:
        symbol = '/'
        view_numbers += ' / '
        ui.lineEdit.setText(view_numbers)
        num_2 = num_1
        num_1 = ''

ui.pushButton_delenie.clicked.connect(division)


def plus():
    global num_1
    global view_numbers
    global num_2
    global symbol
    if '+' in view_numbers or '-' in view_numbers[2:] \
            or 'x' in view_numbers or '/' in view_numbers:
        pass
    else:
        symbol = '+'
        view_numbers += ' + '
        ui.lineEdit.setText(view_numbers)
        num_2 = num_1
        num_1 = ''

ui.pushButton_plus.clicked.connect(plus)


def chmin(znak):
    global view_numbers
    count = 0
    for i in view_numbers:
        if i == znak:
            count += 1
    return count
    count = 0

def minus():
    global num_1
    global view_numbers
    global num_2
    global symbol
    if '+' in view_numbers or chmin('-') > 1 \
            or 'x' in view_numbers or '/' in view_numbers:
        pass
    else:
        symbol = '-'
        view_numbers += ' - '
        if view_numbers[1] == '-':
            symbol = ''
            ui.lineEdit.setText(view_numbers)
        else:
            ui.lineEdit.setText(view_numbers)
            num_2 = num_1
            num_1 = ''

ui.pushButton_minus.clicked.connect(minus)


def mnozh():
    global num_1
    global view_numbers
    global num_2
    global symbol
    if '+' in view_numbers or '-' in view_numbers[2:] \
            or 'x' in view_numbers or '/' in view_numbers:
        pass
    else:
        symbol = 'x'
        view_numbers += ' x '
        ui.lineEdit.setText(view_numbers)
        num_2 = num_1
        num_1 = ''

ui.pushButton_umnozh.clicked.connect(mnozh)


def sinus():
    global num_1
    global view_numbers
    if '+' in view_numbers or '-' in view_numbers \
            or 'x' in view_numbers or '/' in view_numbers:
        pass
    else:
        if view_numbers == '':
            ui.lineEdit.setText('Введите число, а потом повторите операцию')
        else:
            num_1 = float(view_numbers)
            num_1 = math.sin(num_1)
            num_1 = str(num_1)
            view_numbers = num_1
            ui.lineEdit.setText(view_numbers)

ui.pushButton_sin.clicked.connect(sinus)


def cosinus():
    global num_1
    global view_numbers
    if '+' in view_numbers or '-' in view_numbers \
            or 'x' in view_numbers or '/' in view_numbers:
        pass
    else:
        if view_numbers == '':
            ui.lineEdit.setText('Введите число, а потом повторите операцию')
        else:
            num_1 = float(view_numbers)
            num_1 = math.cos(num_1)
            num_1 = str(num_1)
            view_numbers = num_1
            ui.lineEdit.setText(view_numbers)

ui.pushButton_cos.clicked.connect(cosinus)

def tg():
    global num_1
    global view_numbers
    if '+' in view_numbers or '-' in view_numbers \
            or 'x' in view_numbers or '/' in view_numbers:
        pass
    else:
        if view_numbers == '':
            ui.lineEdit.setText('Введите число, а потом повторите операцию')
        else:
            num_1 = float(view_numbers)
            num_1 = math.tan(num_1)
            num_1 = str(num_1)
            view_numbers = num_1
            ui.lineEdit.setText(view_numbers)

ui.pushButton_tg.clicked.connect(tg)

def ln():
    global num_1
    global view_numbers
    if '+' in view_numbers or '-' in view_numbers \
            or 'x' in view_numbers or '/' in view_numbers:
        pass
    else:
        if num_1 == '0' or num_1 == '0.0':
            pass
        else:
            if view_numbers == '':
                ui.lineEdit.setText('Введите число, а потом повторите операцию')
            else:
                num_1 = float(view_numbers)
                num_1 = math.log(num_1)
                num_1 = str(num_1)
                view_numbers = num_1
                ui.lineEdit.setText(view_numbers)

ui.pushButton_ln.clicked.connect(ln)


def delx():
    global num_1
    global view_numbers
    if '+' in view_numbers or '-' in view_numbers \
            or 'x' in view_numbers or '/' in view_numbers:
        pass
    else:
        if view_numbers == '':
            ui.lineEdit.setText('Введите число, а потом повторите операцию')
        else:
            num_1 = float(view_numbers)
            num_1 = 1 / (num_1)
            num_1 = str(num_1)
            view_numbers = num_1
            ui.lineEdit.setText(view_numbers)

ui.pushButton_delx.clicked.connect(delx)


def step2():
    global num_1
    global view_numbers
    if '+' in view_numbers or '-' in view_numbers \
            or 'x' in view_numbers or '/' in view_numbers:
        pass
    else:
        if view_numbers == '':
            ui.lineEdit.setText('Введите число, а потом повторите операцию')
        else:
            num_1 = float(view_numbers)
            num_1 = (num_1)**2
            num_1 = str(num_1)
            view_numbers = num_1
            ui.lineEdit.setText(view_numbers)

ui.pushButton_step2.clicked.connect(step2)


def sqrt():
    global num_1
    global view_numbers
    if '+' in view_numbers or '-' in view_numbers \
            or 'x' in view_numbers or '/' in view_numbers:
        pass
    else:
        if view_numbers == '':
            ui.lineEdit.setText('Введите число, а потом повторите операцию')
        else:
            num_1 = float(view_numbers)
            num_1 = math.sqrt(num_1)
            num_1 = str(num_1)
            view_numbers = num_1
            ui.lineEdit.setText(view_numbers)

ui.pushButton_sqrt.clicked.connect(sqrt)


def equally():
    global num_1
    global view_numbers
    global num_2
    global symbol
    if symbol == '+':
        num_1 = view_numbers[0:view_numbers.index('+')]
        num_1 = float(num_1)
        num_2 = view_numbers[(view_numbers.index('+') + 1):]
        num_2 = float(num_2)
        answer = num_1 + num_2
        num_1 = answer
        answer = str(answer)
        ui.lineEdit.setText(answer)
        num_1 = str(num_1)
        num_2 = str(num_2)
        view_numbers = num_1
    elif symbol == '-':
        if view_numbers[1] == '-':
            num_1 = view_numbers[2:view_numbers.index('-')]
            num_1 = float(num_1)
            num_2 = view_numbers[(view_numbers[2:].index('-') + 1):]
            num_2 = float(num_2)
            answer = num_1 - num_2
            num_1 = answer
            answer = str(answer)
            ui.lineEdit.setText(answer)
            num_1 = str(num_1)
            num_2 = str(num_2)
            view_numbers = num_1
        else:
            num_1 = view_numbers[0:view_numbers.index('-')]
            num_1 = float(num_1)
            num_2 = view_numbers[(view_numbers.index('-') + 1):]
            num_2 = float(num_2)
            answer = num_1 - num_2
            num_1 = answer
            answer = str(answer)
            ui.lineEdit.setText(answer)
            num_1 = str(num_1)
            num_2 = str(num_2)
            view_numbers = num_1
    elif symbol == 'x':
        num_1 = view_numbers[0:view_numbers.index('x')]
        num_1 = float(num_1)
        num_2 = view_numbers[(view_numbers.index('x') + 1):]
        num_2 = float(num_2)
        answer = num_2 * num_1
        num_1 = answer
        answer = str(answer)
        ui.lineEdit.setText(answer)
        num_1 = str(num_1)
        num_2 = str(num_2)
        view_numbers = num_1
    elif symbol == '/':
        num_1 = view_numbers[0:view_numbers.index('/')]
        num_1 = float(num_1)
        num_2 = view_numbers[(view_numbers.index('/') + 1):]
        num_2 = float(num_2)
        answer = num_1 / num_2
        num_1 = answer
        answer = str(answer)
        ui.lineEdit.setText(answer)
        num_1 = str(num_1)
        num_2 = str(num_2)
        view_numbers = num_1

ui.pushButton_ravno.clicked.connect(equally)


sys.exit(app.exec_())

