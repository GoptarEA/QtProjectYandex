from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QDialog, QFileDialog
import sys
from ui.startWindow import Ui_StartWindow
from ui.loginWindow import Ui_LoginWindow
from ui.registerWindow import Ui_RegisterWindow
from ui.roleWindow import Ui_RoleWindow
from ui.main_menu import Ui_MainMenu
from ui.dialog_win import Ui_Dialog
from ui.generate_test import Ui_GenerateTestWindow
from ui.recent_files import Ui_RecentFiles
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


class RecentWindow(QMainWindow, Ui_RecentFiles):
    def __init__(self, *args, **kwargs):
        super(RecentWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.return_back.clicked.connect(self.return_to_menu)

    def return_to_menu(self):
        app_window.setCurrentWidget(menuWindow)

    def show_users_works(self, userid):
        print(get_all_users_works(userid))


class GenerateTestWindow(QMainWindow, Ui_GenerateTestWindow):
    def __init__(self, *args, **kwargs):
        super(GenerateTestWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.comboBox.addItems(["Арифм. операции в разл. с.с.", "Переводы между с.с."])
        self.comboBox_2.addItems([".pdf", ".txt", ".docx"])
        self.spinBox_2.setValue(4)
        self.userid = ""
        self.label_5.setText(os.getcwd())
        self.generate_button.clicked.connect(self.generate_test)
        self.returntomenu.clicked.connect(self.openmenu)
        self.choose_place.clicked.connect(self.choose_folder)

    def set_user_id(self, userid):
        self.userid = userid

    def generate_test(self):
        add_new_work(
            self.comboBox.currentText(),
            self.spinBox.value(),
            self.spinBox_2.value(),
            self.comboBox_2.currentText(),
            self.userid
        )
        if self.comboBox.currentText() == "Арифм. операции в разл. с.с.":
            for variant_number in range(self.spinBox.value()):
                print(self.spinBox.value())
                generate_ariphmetic_pdf(
                    "Арифметические операции",
                    self.spinBox_2.value(),
                    ['+', '-', "*"],
                    [2, 4, 8, 16],
                    self.comboBox_2.currentText(),
                    self.label_5.text(),
                    variant_number
                )
        elif self.comboBox.currentText() == "Переводы между с.с.":
            for variant_number in range(self.spinBox.value()):
                generate_systems_pdf(
                    8,
                    ["двоичная", "четверичная", "восьмеричная", "шестнадцатеричная"],
                    self.comboBox_2.currentText(),
                    self.label_5.text(),
                    variant_number
                )


    def openmenu(self):
        app_window.setCurrentWidget(menuWindow)

    def choose_folder(self):
        dirlist = QFileDialog.getExistingDirectory(self,"Выбрать папку",".")
        self.label_5.setText(dirlist)


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
            menuWindow.set_user_id(get_user(self.login_input.text())[0][0])
            print(get_user(self.login_input.text())[0][0])
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
        self.userid = ""
        self.new_test.clicked.connect(self.opengeneratewindow)
        self.exit_btn.clicked.connect(self.close_app)
        self.recent_tests.clicked.connect(self.recent_files)

    def close_app(self):
        dialog = CloseDialog()
        dialog.exec()

    def set_user_id(self, userid):
        self.userid = userid

    def opengeneratewindow(self):
        app_window.setCurrentWidget(generateTestWindow)
        generateTestWindow.set_user_id(self.userid)

    def recent_files(self):
        app_window.setCurrentWidget(recentWindow)
        recentWindow.show_users_works(self.userid)


if __name__ == '__main__':
    create_db()

    app = QApplication(sys.argv)
    startWindow = StartWindow()
    loginWindow = LoginWindow()
    registerWindow = RegisterWindow()
    roleWindow = RoleWindow()
    menuWindow = MenuWindow()
    recentWindow = RecentWindow()
    generateTestWindow = GenerateTestWindow()

    app_window = ApplicationWindow([startWindow,
                                    loginWindow,
                                    registerWindow,
                                    roleWindow,
                                    menuWindow,
                                    generateTestWindow,
                                    recentWindow])

    app_window.show()
    sys.exit(app.exec())
