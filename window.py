# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import script as sc

class Ui_winSignUp(object):
    def openOther(self):
        ui = Ui_winLogin()
        ui.setupUi(MainWindow)
        MainWindow.show()

    def setupUi(self, winSignUp):
        winSignUp.setObjectName("winSignUp")
        winSignUp.resize(200, 300)
        self.centralwidget = QtWidgets.QWidget(winSignUp)
        self.centralwidget.setObjectName("centralwidget")
        self.lbHeader = QtWidgets.QLabel(self.centralwidget)
        self.lbHeader.setGeometry(QtCore.QRect(0, 10, 201, 20))
        self.lbHeader.setAlignment(QtCore.Qt.AlignCenter)
        self.lbHeader.setObjectName("lbHeader")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 50, 135, 160))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.formLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbEmail = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbEmail.setObjectName("lbEmail")
        self.verticalLayout.addWidget(self.lbEmail)
        self.lineEmail = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEmail.setStyleSheet("magin: auto")
        self.lineEmail.setObjectName("lineEmail")
        self.verticalLayout.addWidget(self.lineEmail)
        self.lbUser = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbUser.setObjectName("lbUser")
        self.verticalLayout.addWidget(self.lbUser)
        self.lineUser = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineUser.setStyleSheet("magin: auto")
        self.lineUser.setObjectName("lineUser")
        self.verticalLayout.addWidget(self.lineUser)
        self.lbPasswd = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbPasswd.setObjectName("lbPasswd")
        self.verticalLayout.addWidget(self.lbPasswd)
        self.linePasswd = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.linePasswd.setStyleSheet("magin: auto")
        self.linePasswd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.linePasswd.setObjectName("linePasswd")
        self.verticalLayout.addWidget(self.linePasswd)
        self.btnSign = QtWidgets.QPushButton(self.formLayoutWidget)
        self.btnSign.setObjectName("btnSign")
        self.verticalLayout.addWidget(self.btnSign)
        self.lbError = QtWidgets.QLabel(self.centralwidget)
        self.lbError.setGeometry(QtCore.QRect(10, 30, 181, 20))
        self.lbError.setStyleSheet("color: rgb(255, 0, 0)")
        self.lbError.setText("")
        self.lbError.setObjectName("lbError")
        self.btnHaveAccount = QtWidgets.QPushButton(self.centralwidget)
        self.btnHaveAccount.setGeometry(QtCore.QRect(41, 216, 111, 16))
        self.btnHaveAccount.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnHaveAccount.setStyleSheet("color: blue;\n"
"border: none;\n"
"background-color: rgba(0,0,0,0)")
        self.btnHaveAccount.setObjectName("btnHaveAccount")
        winSignUp.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(winSignUp)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 200, 21))
        self.menubar.setObjectName("menubar")
        winSignUp.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(winSignUp)
        self.statusbar.setObjectName("statusbar")
        winSignUp.setStatusBar(self.statusbar)

        self.retranslateUi(winSignUp)
        QtCore.QMetaObject.connectSlotsByName(winSignUp)

        self.btnSign.clicked.connect(lambda: sc.submit(self))
        self.btnHaveAccount.clicked.connect(lambda: self.openOther())

    def retranslateUi(self, winSignUp):
        _translate = QtCore.QCoreApplication.translate
        winSignUp.setWindowTitle(_translate("winSignUp", "MainWindow"))
        self.lbHeader.setText(_translate("winSignUp", "Sign Up"))
        self.lbEmail.setText(_translate("winSignUp", "Email"))
        self.lbUser.setText(_translate("winSignUp", "Username"))
        self.lbPasswd.setText(_translate("winSignUp", "Password"))
        self.btnSign.setText(_translate("winSignUp", "Sign Up"))
        self.btnHaveAccount.setText(_translate("winSignUp", "Already have account"))

class Ui_winLogin(object):
    def openOther(self):
        ui = Ui_winSignUp()
        ui.setupUi(MainWindow)
        MainWindow.show()

    def setupUi(self, winLogin):
        winLogin.setObjectName("winLogin")
        winLogin.resize(200, 300)
        self.centralwidget = QtWidgets.QWidget(winLogin)
        self.centralwidget.setObjectName("centralwidget")
        self.lbHeader = QtWidgets.QLabel(self.centralwidget)
        self.lbHeader.setGeometry(QtCore.QRect(0, 10, 201, 20))
        self.lbHeader.setAlignment(QtCore.Qt.AlignCenter)
        self.lbHeader.setObjectName("lbHeader")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 50, 135, 134))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.formLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbEmail = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbEmail.setObjectName("lbEmail")
        self.verticalLayout.addWidget(self.lbEmail)
        self.lineEmail = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEmail.setStyleSheet("magin: auto")
        self.lineEmail.setObjectName("lineEmail")
        self.verticalLayout.addWidget(self.lineEmail)
        self.lbPasswd = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbPasswd.setObjectName("lbPasswd")
        self.verticalLayout.addWidget(self.lbPasswd)
        self.linePasswd = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.linePasswd.setStyleSheet("magin: auto")
        self.linePasswd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.linePasswd.setObjectName("linePasswd")
        self.verticalLayout.addWidget(self.linePasswd)
        self.btnLogin = QtWidgets.QPushButton(self.formLayoutWidget)
        self.btnLogin.setObjectName("btnLogin")
        self.verticalLayout.addWidget(self.btnLogin)
        self.btnNoAccount = QtWidgets.QPushButton(self.centralwidget)
        self.btnNoAccount.setGeometry(QtCore.QRect(46, 190, 101, 16))
        self.btnNoAccount.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnNoAccount.setStyleSheet("color: blue;\n"
"border: none;\n"
"background-color: rgba(0,0,0,0)")
        self.btnNoAccount.setObjectName("btnNoAccount")
        self.lbError = QtWidgets.QLabel(self.centralwidget)
        self.lbError.setGeometry(QtCore.QRect(10, 30, 181, 20))
        self.lbError.setStyleSheet("color: rgb(255, 0, 0)")
        self.lbError.setText("")
        self.lbError.setObjectName("lbError")
        winLogin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(winLogin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 200, 21))
        self.menubar.setObjectName("menubar")
        winLogin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(winLogin)
        self.statusbar.setObjectName("statusbar")
        winLogin.setStatusBar(self.statusbar)

        self.retranslateUi(winLogin)
        QtCore.QMetaObject.connectSlotsByName(winLogin)

        self.btnLogin.clicked.connect(lambda: sc.login(self))
        self.btnNoAccount.clicked.connect(lambda: self.openOther())

    def retranslateUi(self, winLogin):
        _translate = QtCore.QCoreApplication.translate
        winLogin.setWindowTitle(_translate("winLogin", "MainWindow"))
        self.lbHeader.setText(_translate("winLogin", "Log in"))
        self.lbEmail.setText(_translate("winLogin", "Email"))
        self.lbPasswd.setText(_translate("winLogin", "Password"))
        self.btnLogin.setText(_translate("winLogin", "Log in"))
        self.btnNoAccount.setText(_translate("winLogin", "Don't have account"))

if __name__ == "__main__":
    import sys
            
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_winSignUp()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())