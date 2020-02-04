from PyQt5 import QtCore, QtGui, QtWidgets

class Diskon():
    def __init__(self, w):
        self.val = 0
        self.Dialog = QtWidgets.QDialog(w)
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(276, 228)
        self.diskon = QtWidgets.QSpinBox(self.Dialog)
        self.diskon.setGeometry(QtCore.QRect(60, 60, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.diskon.setFont(font)
        self.diskon.setAlignment(QtCore.Qt.AlignCenter)
        self.diskon.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.diskon.setProperty("value", 0)
        self.diskon.setObjectName("diskon")
        self.label_diskon = QtWidgets.QLabel(self.Dialog)
        self.label_diskon.setGeometry(QtCore.QRect(100, 30, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_diskon.setFont(font)
        self.label_diskon.setObjectName("label_diskon")
        self.okBtn = QtWidgets.QPushButton(self.Dialog)
        self.okBtn.setGeometry(QtCore.QRect(80, 140, 111, 33))
        self.okBtn.setStyleSheet("QPushButton {\n"
"    background: #555;\n"
"    border-radius: 6px;\n"
"    border: none;\n"
"    color: white;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 2px solid #555;\n"
"    background: white;\n"
"    color: #555;\n"
"}")
        self.okBtn.setObjectName("okBtn")
        self.okBtn.clicked.connect(self.handler)

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Atur Diskon"))
        self.label_diskon.setText(_translate("Dialog", "Diskon %"))
        self.okBtn.setText(_translate("Dialog", "Ok"))

    def show(self):
        self.Dialog.exec_()

    def handler(self):
        self.val = self.diskon.text()
        self.Dialog.close()
