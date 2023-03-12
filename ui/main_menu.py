# Form implementation generated from reading ui file 'main-menu.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainMenu(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setStyleSheet("background-color: #eee;")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.025, y1:0.238636, x2:1, y2:1, stop:0 rgba(110, 69, 226, 255), stop:1 rgba(136, 211, 206, 255))")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(150, 50, 150, 100)
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName("verticalLayout")
        self.new_test = QtWidgets.QPushButton(parent=self.centralwidget)
        self.new_test.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    font-size: 36px;\n"
"    border-radius: 16px;\n"
"    padding: 10px;\n"
"    color:  rgba(110, 69, 226, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #EEE;\n"
"}")
        self.new_test.setObjectName("new_test")
        self.verticalLayout.addWidget(self.new_test)
        self.recent_tests = QtWidgets.QPushButton(parent=self.centralwidget)
        self.recent_tests.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    font-size: 36px;\n"
"    border-radius: 16px;\n"
"    padding: 10px;\n"
"    color:  rgba(110, 69, 226, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #EEE;\n"
"}")
        self.recent_tests.setObjectName("recent_tests")
        self.verticalLayout.addWidget(self.recent_tests)
        self.exit_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.exit_btn.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    font-size: 36px;\n"
"    border-radius: 16px;\n"
"    padding: 10px;\n"
"    color:  rgba(110, 69, 226, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #EEE;\n"
"}")
        self.exit_btn.setObjectName("exit_btn")
        self.verticalLayout.addWidget(self.exit_btn)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Тестирующая система"))
        self.new_test.setText(_translate("MainWindow", "Создать новый тест"))
        self.recent_tests.setText(_translate("MainWindow", "Созданные тесты"))
        self.exit_btn.setText(_translate("MainWindow", "Выход"))