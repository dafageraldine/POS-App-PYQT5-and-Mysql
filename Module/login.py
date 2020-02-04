from PyQt5 import QtCore, QtGui, QtWidgets


class Login():
    def __init__(self, w):
        self.w = w
        self.isLogin = False
        self.Dialog = QtWidgets.QDialog(w)
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(416, 567)
        self.pin = QtWidgets.QLineEdit(self.Dialog)
        self.pin.setGeometry(QtCore.QRect(20, 30, 371, 81))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pin.setFont(font)
        self.pin.setStyleSheet("padding: 0 20px;")
        self.pin.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pin.setObjectName("pin")
        self.pin.textChanged.connect(self.check)
        self.pin.setPlaceholderText("PIN")
        self.pin.setReadOnly(True)
        self.pin.clear()
        self.val = ""

        self.btn1 = QtWidgets.QPushButton(self.Dialog)
        self.btn1.setGeometry(QtCore.QRect(30, 130, 90, 90))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.btn1.setFont(font)
        self.btn1.setStyleSheet("QPushButton {border-radius:45%;\
background: white;\
}\
QPushButton:pressed{\
background: #ccc;\
}")
        self.btn1.setObjectName("btn1")
        self.btn1.clicked.connect(self.click1)

        self.btn2 = QtWidgets.QPushButton(self.Dialog)
        self.btn2.setGeometry(QtCore.QRect(160, 130, 90, 90))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.btn2.setFont(font)
        self.btn2.setStyleSheet("QPushButton {border-radius:45%;\
background: white;\
}\
QPushButton:pressed{\
background: #ccc;\
}")
        self.btn2.setObjectName("btn2")
        self.btn2.clicked.connect(self.click2)

        self.btn3 = QtWidgets.QPushButton(self.Dialog)
        self.btn3.setGeometry(QtCore.QRect(290, 130, 90, 90))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.btn3.setFont(font)
        self.btn3.setStyleSheet("QPushButton {border-radius:45%;\
background: white;\
}\
QPushButton:pressed{\
background: #ccc;\
}")
        self.btn3.setObjectName("btn3")
        self.btn3.clicked.connect(self.click3)

        self.btn5 = QtWidgets.QPushButton(self.Dialog)
        self.btn5.setGeometry(QtCore.QRect(160, 240, 90, 90))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.btn5.setFont(font)
        self.btn5.setStyleSheet("QPushButton {border-radius:45%;\
background: white;\
}\
QPushButton:pressed{\
background: #ccc;\
}")
        self.btn5.setObjectName("btn5")
        self.btn5.clicked.connect(self.click5)

        self.btn4 = QtWidgets.QPushButton(self.Dialog)
        self.btn4.setGeometry(QtCore.QRect(30, 240, 90, 90))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.btn4.setFont(font)
        self.btn4.setStyleSheet("QPushButton {border-radius:45%;\
background: white;\
}\
QPushButton:pressed{\
background: #ccc;\
}")
        self.btn4.setObjectName("btn4")
        self.btn4.clicked.connect(self.click4)

        self.btn6 = QtWidgets.QPushButton(self.Dialog)
        self.btn6.setGeometry(QtCore.QRect(290, 240, 90, 90))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.btn6.setFont(font)
        self.btn6.setStyleSheet("QPushButton {border-radius:45%;\
background: white;\
}\
QPushButton:pressed{\
background: #ccc;\
}")
        self.btn6.setObjectName("btn6")
        self.btn6.clicked.connect(self.click6)

        self.btn8 = QtWidgets.QPushButton(self.Dialog)
        self.btn8.setGeometry(QtCore.QRect(160, 350, 90, 90))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.btn8.setFont(font)
        self.btn8.setStyleSheet("QPushButton {border-radius:45%;\
background: white;\
}\
QPushButton:pressed{\
background: #ccc;\
}")
        self.btn8.setObjectName("btn8")
        self.btn8.clicked.connect(self.click8)

        self.btn9 = QtWidgets.QPushButton(self.Dialog)
        self.btn9.setGeometry(QtCore.QRect(290, 350, 90, 90))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.btn9.setFont(font)
        self.btn9.setStyleSheet("QPushButton {border-radius:45%;\
background: white;\
}\
QPushButton:pressed{\
background: #ccc;\
}")
        self.btn9.setObjectName("btn9")
        self.btn9.clicked.connect(self.click9)

        self.btn7 = QtWidgets.QPushButton(self.Dialog)
        self.btn7.setGeometry(QtCore.QRect(30, 350, 90, 90))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.btn7.setFont(font)
        self.btn7.setStyleSheet("QPushButton {border-radius:45%;\
background: white;\
}\
QPushButton:pressed{\
background: #ccc;\
}")
        self.btn7.setObjectName("btn7")
        self.btn7.clicked.connect(self.click7)

        self.btn0 = QtWidgets.QPushButton(self.Dialog)
        self.btn0.setGeometry(QtCore.QRect(160, 460, 90, 90))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.btn0.setFont(font)
        self.btn0.setStyleSheet("QPushButton {border-radius:45%;\
background: white;\
}\
QPushButton:pressed{\
background: #ccc;\
}")
        self.btn0.setObjectName("btn0")
        self.btn0.clicked.connect(self.click0)

        self.btnDel = QtWidgets.QPushButton(self.Dialog)
        self.btnDel.setGeometry(QtCore.QRect(290, 460, 90, 90))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.btnDel.setFont(font)
        self.btnDel.setStyleSheet("QPushButton {border-radius:45%;\
background: white;\
}\
QPushButton:pressed{\
background: #ccc;\
}")
        self.btnDel.setObjectName("btnHashtag")
        self.btnDel.clicked.connect(self.clickDel)

        self.btnAsterisk = QtWidgets.QPushButton(self.Dialog)
        self.btnAsterisk.setGeometry(QtCore.QRect(30, 460, 90, 90))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setKerning(False)
        self.btnAsterisk.setFont(font)
        self.btnAsterisk.setStyleSheet("QPushButton {border-radius:45%;\
background: white;\
padding-top:15px;\
}\
QPushButton:pressed{\
background: #ccc;\
}")
        self.btnAsterisk.setObjectName("btnAsterisk")
        self.btnAsterisk.clicked.connect(self.clickAsterisk)

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "PIN"))
        self.btn1.setText(_translate("Dialog", "1"))
        self.btn1.setShortcut(_translate("Dialog", "1"))
        self.btn2.setText(_translate("Dialog", "2"))
        self.btn3.setText(_translate("Dialog", "3"))
        self.btn3.setShortcut(_translate("Dialog", "1"))
        self.btn5.setText(_translate("Dialog", "5"))
        self.btn4.setText(_translate("Dialog", "4"))
        self.btn6.setText(_translate("Dialog", "6"))
        self.btn8.setText(_translate("Dialog", "8"))
        self.btn9.setText(_translate("Dialog", "9"))
        self.btn7.setText(_translate("Dialog", "7"))
        self.btn0.setText(_translate("Dialog", "0"))
        self.btnDel.setText(_translate("Dialog", "Del"))
        self.btnAsterisk.setText(_translate("Dialog", "*"))
        self.close()

    def click0(self):
        if self.val is "" or self.val is None:
            self.pin.setText('0')
            self.val = self.pin.text()
            return
        self.val = self.val + '0'
        self.pin.setText(self.val)

    def click1(self):
        if self.val is "" or self.val is None:
            self.pin.setText('1')
            self.val = self.pin.text()
            return
        self.val = self.val + '1'
        self.pin.setText(self.val)

    def click2(self):
        if self.val is "" or self.val is None:
            self.pin.setText('2')
            self.val = self.pin.text()
            return
        self.val = self.val + '2'
        self.pin.setText(self.val)

    def click3(self):
        if self.val is "" or self.val is None:
            self.pin.setText('3')
            self.val = self.pin.text()
            return
        self.val = self.val + '3'
        self.pin.setText(self.val)

    def click4(self):
        if self.val is "" or self.val is None:
            self.pin.setText('4')
            self.val = self.pin.text()
            return
        self.val = self.val + '4'
        self.pin.setText(self.val)

    def click5(self):
        if self.val is "" or self.val is None:
            self.pin.setText('5')
            self.val = self.pin.text()
            return
        self.val = self.val + '5'
        self.pin.setText(self.val)

    def click6(self):
        if self.val is "" or self.val is None:
            self.pin.setText('6')
            self.val = self.pin.text()
            return
        self.val = self.val + '6'
        self.pin.setText(self.val)

    def click7(self):
        if self.val is "" or self.val is None:
            self.pin.setText('7')
            self.val = self.pin.text()
            return
        self.val = self.val + '7'
        self.pin.setText(self.val)

    def click8(self):
        if self.val is "" or self.val is None:
            self.pin.setText('8')
            self.val = self.pin.text()
            return
        self.val = self.val + '8'
        self.pin.setText(self.val)

    def click9(self):
        if self.val is "" or self.val is None:
            self.pin.setText('9')
            self.val = self.pin.text()
            return
        self.val = self.val + '9'
        self.pin.setText(self.val)

    def clickAsterisk(self):
        if self.val is "" or self.val is None:
            self.pin.setText('*')
            self.val = self.pin.text()
            return
        self.val = self.val + '*'
        self.pin.setText(self.val)

    def clickDel(self):
        if self.val is "" or self.val is None:
            return
        self.pin.backspace()
        self.val = self.pin.text()

    def check(self):
        if len(self.val) == 4:
            key = "password = \"{}\""
            key = key.format(self.pin.text())
            data = self.w.mysql.findCol("password", "bulleyearchery.admin", key, False)
            if data is None:
                self.w.showDialog("warning", "PIN salah!",
                                  "Harap masukkan PIN dengan benar!")
                self.pin.clear()
                self.val = ""
                return
            self.isLogin = True
            self.close()

    def close(self):
        self.Dialog.close()

    def show(self):
        self.Dialog.exec_()
