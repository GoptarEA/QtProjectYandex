from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QDialog
import sys
from ui.startWindow import Ui_StartWindow
from ui.loginWindow import Ui_LoginWindow
from ui.registerWindow import Ui_RegisterWindow
from ui.roleWindow import Ui_RoleWindow
from ui.main_menu import Ui_MainMenu
from ui.dialog_win import Ui_Dialog
from ui.generate_test import Ui_GenerateTestWindow
from file_generator import *
from db_functions import *


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
        self.comboBox.addItems(["Арифм. операции в разл. с.с.", "Переводы между с.с."])
        self.generate_button.clicked.connect(self.generate_test)
        self.returntomenu.clicked.connect(self.openmenu)

    def generate_test(self):
        generate_systems_pdf(8, ["двоичная", "четверичная", "восьмеричная", "шестнадцатеричная"])
        generate_ariphmetic_pdf("Арифметические операции", 6, ['+', '-', "*"], [2, 4, 8, 16])

    def openmenu(self):
        app_window.setCurrentWidget(menuWindow)


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
        self.reg_button.clicked.connect(self.register_user)
        self.login_input.editingFinished.connect(self.login_message)
        self.password_repeat.editingFinished.connect(self.password_message)
        self.login_ok = False
        self.password_ok = False
        self.reg_button.setEnabled(False)

    def register_user(self):
        salt = os.urandom(32)
        password = self.password_input.text()
        add_new_user(self.login_input.text(), hashUsersPassword(password, salt))
        app_window.setCurrentWidget(loginWindow)

    def login_message(self):
        if check_user(self.login_input.text()):
            self.error_label.setText("Такой пользователь уже существует")
            self.login_ok = False
            self.reg_button.setEnabled(False)
        else:
            self.login_ok = True
            self.error_label.setText("")
            if self.password_ok:
                self.reg_button.setEnabled(True)

    def password_message(self):
        if self.password_input.text() != self.password_repeat.text():
            self.error_label.setText("Пароли не совпадают")
            self.password_ok = False
            self.reg_button.setEnabled(False)
        else:
            self.error_label.setText("")
            self.password_ok = True
            if self.login_ok:
                self.reg_button.setEnabled(True)

    def returntomenu(self):
        app_window.setCurrentWidget(startWindow)


class LoginWindow(QMainWindow, Ui_LoginWindow):
    def __init__(self, *args, **kwargs):
        super(LoginWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.login_input.editingFinished.connect(self.returnedit)
        self.login_button.clicked.connect(self.openmenu)

    def returnedit(self):
        if not check_user(self.login_input.text()):
            self.error_label.setText("Такого пользователя не существует")
            self.login_button.setEnabled(False)
        else:
            self.error_label.setText("")
            self.login_button.setEnabled(True)

    def openmenu(self):
        login, password = get_user(self.login_input.text())[0][1:]
        print(login, password)
        if check_password(password, self.password_input.text()):
            app_window.setCurrentWidget(menuWindow)
        else:
            self.error_label.setText("Введён неверный пароль")


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
    create_db()
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
