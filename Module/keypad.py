from PyQt5 import QtCore, QtGui, QtWidgets


class Keypad():
    def __init__(self, w, maximum = 10, placeholder = None):
        self.w = w
        self.Dialog = QtWidgets.QDialog(w)
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(416, 667)
        self.value = QtWidgets.QLineEdit(self.Dialog)
        self.value.setGeometry(QtCore.QRect(20, 30, 371, 81))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.value.setFont(font)
        self.value.setStyleSheet("padding: 0 20px;")
        self.value.setObjectName("value")
        self.value.clear()
        self.value.setMaxLength(maximum)
        self.value.setReadOnly(True)
        self.value.setPlaceholderText(placeholder)
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

        self.btnEnter = QtWidgets.QPushButton(self.Dialog)
        self.btnEnter.setGeometry(QtCore.QRect(290, 460, 90, 90))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btnEnter.setFont(font)
        self.btnEnter.setStyleSheet("QPushButton {border-radius:45%;\
background: white;\
}\
QPushButton:pressed{\
background: #ccc;\
}")
        self.btnEnter.setObjectName("btnEnter")
        self.btnEnter.clicked.connect(self.clickEnter)

        self.btnDel = QtWidgets.QPushButton(self.Dialog)
        self.btnDel.setGeometry(QtCore.QRect(30, 460, 90, 90))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setKerning(False)
        self.btnDel.setFont(font)
        self.btnDel.setStyleSheet("QPushButton {border-radius:45%;\
background: white;\
}\
QPushButton:pressed{\
background: #ccc;\
}")
        self.btnDel.setObjectName("btnDel")
        self.btnDel.clicked.connect(self.clickDel)

        self.btnDot = QtWidgets.QPushButton(self.Dialog)
        self.btnDot.setGeometry(QtCore.QRect(30, 570, 90, 90))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setKerning(False)
        self.btnDot.setFont(font)
        self.btnDot.setStyleSheet("QPushButton {border-radius:45%;\
background: white;\
}\
QPushButton:pressed{\
background: #ccc;\
}")
        self.btnDot.setObjectName("btnDel")
        self.btnDot.clicked.connect(self.clickDot)

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Keypad"))
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
        self.btnDot.setText(_translate("Dialog", "."))
        self.btnEnter.setText(_translate("Dialog", "Enter"))
        self.btnDel.setText(_translate("Dialog", "Del"))
        self.close()

    def click0(self):
        if self.val is "" or self.val is None:
            self.value.setText('0')
            self.val = self.value.text()
            return
        self.val = self.val + '0'
        self.value.setText(self.val)

    def click1(self):
        if self.val is "" or self.val is None:
            self.value.setText('1')
            self.val = self.value.text()
            return
        self.val = self.val + '1'
        self.value.setText(self.val)

    def click2(self):
        if self.val is "" or self.val is None:
            self.value.setText('2')
            self.val = self.value.text()
            return
        self.val = self.val + '2'
        self.value.setText(self.val)

    def click3(self):
        if self.val is "" or self.val is None:
            self.value.setText('3')
            self.val = self.value.text()
            return
        self.val = self.val + '3'
        self.value.setText(self.val)

    def click4(self):
        if self.val is "" or self.val is None:
            self.value.setText('4')
            self.val = self.value.text()
            return
        self.val = self.val + '4'
        self.value.setText(self.val)

    def click5(self):
        if self.val is "" or self.val is None:
            self.value.setText('5')
            self.val = self.value.text()
            return
        self.val = self.val + '5'
        self.value.setText(self.val)

    def click6(self):
        if self.val is "" or self.val is None:
            self.value.setText('6')
            self.val = self.value.text()
            return
        self.val = self.val + '6'
        self.value.setText(self.val)

    def click7(self):
        if self.val is "" or self.val is None:
            self.value.setText('7')
            self.val = self.value.text()
            return
        self.val = self.val + '7'
        self.value.setText(self.val)

    def click8(self):
        if self.val is "" or self.val is None:
            self.value.setText('8')
            self.val = self.value.text()
            return
        self.val = self.val + '8'
        self.value.setText(self.val)

    def click9(self):
        if self.val is "" or self.val is None:
            self.value.setText('9')
            self.val = self.value.text()
            return
        self.val = self.val + '9'
        self.value.setText(self.val)

    def clickEnter(self):
        if self.value.text() is not "":
            self.val = self.value.text()
            self.value.clear()
            self.close()

    def clickDel(self):
        if self.val is "" or self.val is None:
            return
        self.value.backspace()
        self.val = self.value.text()

    def clickDot(self):
        if self.val is "" or self.val is None:
            self.value.setText('.')
            self.val = self.value.text()
            return
        self.val = self.val + '.'
        self.value.setText(self.val)

    def check(self):
        if len(self.val) == 4:
            key = "password = \"{}\""
            key = key.format(self.value.text())
            data = self.w.mysql.findCol("password", "bulleyearchery.admin", key, False)
            if data is None:
                self.w.showDialog("warning", "PIN salah!",
                                  "Harap masukkan PIN dengan benar!")
                self.value.clear()
                self.val = ""
                return
            self.isLogin = True
            self.close()

    def close(self):
        self.Dialog.close()

    def show(self):
        self.Dialog.exec_()
