# Form implementation generated from reading ui file 'choose_directory.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ChooseDirectory(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(488, 153)
        self.directory = QtWidgets.QLabel(parent=Dialog)
        self.directory.setGeometry(QtCore.QRect(290, 30, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Play")
        font.setPointSize(14)
        self.directory.setFont(font)
        self.directory.setStyleSheet("background-color: white;\n"
"border-radius: 8px;")
        self.directory.setText("")
        self.directory.setObjectName("directory")
        self.choose_btn = QtWidgets.QPushButton(parent=Dialog)
        self.choose_btn.setGeometry(QtCore.QRect(10, 20, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Play")
        font.setPointSize(14)
        self.choose_btn.setFont(font)
        self.choose_btn.setAutoDefault(True)
        self.choose_btn.setObjectName("choose_btn")
        self.generate_btn = QtWidgets.QPushButton(parent=Dialog)
        self.generate_btn.setGeometry(QtCore.QRect(100, 100, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Play")
        font.setPointSize(14)
        self.generate_btn.setFont(font)
        self.generate_btn.setAutoDefault(True)
        self.generate_btn.setObjectName("generate_btn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.choose_btn.setText(_translate("Dialog", "Выбрать папку:"))
        self.generate_btn.setText(_translate("Dialog", "Сгенерировать"))