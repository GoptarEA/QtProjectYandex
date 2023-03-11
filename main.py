from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QDialog
import sys
from startWindow import Ui_StartWindow
from loginWindow import Ui_LoginWindow
from registerWindow import Ui_RegisterWindow
from roleWindow import Ui_RoleWindow
from main_menu import Ui_MainMenu
from dialog_win import Ui_Dialog
from generate_test import Ui_GenerateTestWindow

from fpdf import FPDF
from random import randint, choice

import requests
import sqlite3

import hashlib
import os

import datetime

users = sqlite3.connect('users.db')
users_cur = users.cursor()

works = sqlite3.connect('works.db')
works_cur = works.cursor()


def create_db():
    users_cur.execute("""CREATE TABLE IF NOT EXISTS users(
       userid INT PRIMARY KEY AUTOINCREMENT,
       login TEXT NOT NULL,
       password TEXT NOT NULL);
    """)
    users.commit()

    works_cur.execute("""CREATE TABLE IF NOT EXISTS works(
           workid INT PRIMARY KEY AUTOINCREMENT,
           theme TEXT NOT NULL,
           varcount INT NOT NULL,
           excount INT NOT NULL,
           creation_date TEXT NOT NULL);
        """)
    works.commit()



def add_new_user(login, password):
    users_cur.execute("INSERT INTO users VALUES(?, ?);", (login, password))
    users.commit()


def add_new_work(theme, varcount, excount):
    works_cur.execute("INSERT INTO works VALUES(?, ?);", (theme, varcount, excount, datetime.date.today()))

def check_user(login):
    users_cur.execute(f"select * from users WHERE login={login}")
    users_list = users_cur.fetchall()
    return len(users_list) != 0




def hashUsersPassword(password, salt):
    key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        100000,
        dklen=128
    )
    return salt + key

def check_password(db_password, input_password):
    salt = db_password[:32]
    password = db_password[32:]
    return password == hashUsersPassword(input_password, salt)


class CloseDialog(QDialog, Ui_Dialog):
    def __init__(self, *args, **kwargs):
        super(CloseDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.pushButton.clicked.connect(lambda: sys.exit(app.exec()))
        self.pushButton_2.clicked.connect(lambda: self.close())


class ApplicationWindow(QStackedWidget):
    def __init__(self, widgets):
        super().__init__()
        self.setFixedWidth(800)
        self.setFixedHeight(600)
        self.setWindowTitle("Тестирующая система")
        for widget in widgets:
            self.addWidget(widget)


class GenerateTestWindow(QMainWindow, Ui_GenerateTestWindow):
    def __init__(self, *args, **kwargs):
        super(GenerateTestWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.generate_button.clicked.connect(self.generate_test)

    def generate_exercise_text(self):
        exercise_text = []
        for i in "abcd":
            exercise_text += [i + ') ' + bin(randint(10, 1000))[2:] + choice(['+', '-', '*']) \
                             + bin(randint(10, 1000))[2:]]
        return exercise_text

    def generate_test(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.add_font("Roboto", "B", "Roboto-Regular.ttf", uni=True)
        pdf.set_font('Roboto', 'B', 16)
        for i in range(20):
            pdf.cell(40, i * 10, "№ " + str(i))
            for item in self.generate_exercise_text():
                pdf.cell(40, 10, item)
                pdf.ln(5)
            pdf.ln(10)
        pdf.output('Самостоятельная работа.pdf', 'F')


class StartWindow(QMainWindow, Ui_StartWindow):
    def __init__(self, *args, **kwargs):
        super(StartWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.loginButton.clicked.connect(self.openLoginWindow)
        self.loginButton_2.clicked.connect(self.changeRoleWindow)

    def openLoginWindow(self):
        app_window.setCurrentWidget(loginWindow)

    def changeRoleWindow(self):
        app_window.setCurrentWidget(roleWindow)


class RegisterWindow(QMainWindow, Ui_RegisterWindow):
    def __init__(self, *args, **kwargs):
        super(RegisterWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.recovery_button.linkActivated.connect(self.returntomenu)

    def returntomenu(self):
        app_window.setCurrentWidget(startWindow)


class LoginWindow(QMainWindow, Ui_LoginWindow):
    def __init__(self, *args, **kwargs):
        super(LoginWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.login_input.editingFinished.connect(self.returnedit)
        self.login_button.clicked.connect(self.openmenu)

    def returnedit(self):
        self.error_label.setText("Пользователя с данными логином не существует")

    def openmenu(self):
        app_window.setCurrentWidget(menuWindow)


class RoleWindow(QMainWindow, Ui_RoleWindow):
    def __init__(self, *args, **kwargs):
        super(RoleWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.student_button.clicked.connect(self.openRegisterWin)
        self.teacher_button.clicked.connect(self.openRegisterWin)

    def openRegisterWin(self):
        app_window.setCurrentWidget(registerWindow)


class MenuWindow(QMainWindow, Ui_MainMenu):
    def __init__(self, *args, **kwargs):
        super(MenuWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.new_test.clicked.connect(self.opengeneratewindow)
        self.exit_btn.clicked.connect(self.close_app)

    def close_app(self):
        dialog = CloseDialog()
        dialog.exec()

    def opengeneratewindow(self):
        app_window.setCurrentWidget(generateTestWindow)


if __name__ == '__main__':


    app = QApplication(sys.argv)
    startWindow = StartWindow()
    loginWindow = LoginWindow()
    registerWindow = RegisterWindow()
    roleWindow = RoleWindow()
    menuWindow = MenuWindow()
    generateTestWindow = GenerateTestWindow()

    app_window = ApplicationWindow([startWindow,
                                    loginWindow,
                                    registerWindow,
                                    roleWindow,
                                    menuWindow,
                                    generateTestWindow])

    app_window.show()
    sys.exit(app.exec())
