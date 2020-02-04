from PyQt5 import QtCore, QtGui, QtWidgets


class Quantity():
    def __init__(self, w):
        self.w = w
        self.Dialog = QtWidgets.QDialog(w)
        self.Dialog.setModal(True)
        self.Dialog.setObjectName("self.Dialog")
        self.Dialog.resize(276, 228)
        self.okBtn = QtWidgets.QPushButton(self.Dialog)
        self.okBtn.setGeometry(QtCore.QRect(80, 150, 111, 29))
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

        self.quantity = QtWidgets.QSpinBox(self.Dialog)
        self.quantity.setGeometry(QtCore.QRect(60, 60, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.quantity.setFont(font)
        self.quantity.setAlignment(QtCore.Qt.AlignCenter)
        self.quantity.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.quantity.setProperty("value", 0)
        self.quantity.setObjectName("quantity")

        selected = w.tabelProduk.selectedItems()
        idProduk = selected[0].text()
        key = "idProduk = \"{}\""
        key = key.format(idProduk)
        qty = w.mysql.findCol("stock", "daftarbarang", key, False)
        row = self.w.transaksi.tabelTransaksi.rowCount()
        amount = r = 0
        while r < row:
            if self.w.transaksi.tabelTransaksi.item(r, 0).text() == idProduk:
                amount = int(self.w.transaksi.tabelTransaksi.item(r, 3).text())
                break
            r = r + 1

        self.habis = False
        self.overload = False
        if qty[0] < 1:
            self.habis = True
        self.maximum = qty[0] - amount
        if self.maximum < 1:
            self.overload = True
        self.quantity.setMaximum(self.maximum)
        self.label_quantity = QtWidgets.QLabel(self.Dialog)
        self.label_quantity.setGeometry(QtCore.QRect(90, 30, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_quantity.setFont(font)
        self.label_quantity.setObjectName("label_quantity")
        self.jumlah = None

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Quantity"))
        self.okBtn.setText(_translate("Dialog", "Ok"))
        self.label_quantity.setText(_translate("Dialog", "Jumlah Item"))

    def handler(self):
        val = int(self.quantity.text())
        if val < 1 or val is None:
            return
        self.jumlah = self.quantity.text()
        self.Dialog.close()
        
    def show(self):
        if self.habis:
            self.w.showDialog("warning", "Stock habis", "Stock produk sedang habis, harap lakukan restock")
            return
        if self.overload:
            self.w.showDialog("warning", "Stock terbatas", "Stock yang dimasukkan ke transaksi sudah mencapai maksimum!")
            return
        self.Dialog.exec_()