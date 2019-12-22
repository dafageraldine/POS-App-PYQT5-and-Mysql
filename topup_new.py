from PyQt5 import QtCore, QtGui, QtWidgets
from Module.sql import *

class Topup():
    def __init__(self, w):
        self.w = w 
        self.Dialog = QtWidgets.QDialog(w)
        self.Dialog.setWindowTitle("Top up Saldo")
        self.Dialog.resize(316, 282)
        self.price = QtWidgets.QLineEdit(self.Dialog)
        self.price.setGeometry(QtCore.QRect(50, 100, 211, 29))
        self.price.setPlaceholderText("Masukkan Nominal Top up")
        self.Btn = QtWidgets.QPushButton(self.Dialog)
        self.Btn.setGeometry(QtCore.QRect(100, 160, 101, 29))
        self.Btn.setText("Top up")
        self.Btn.clicked.connect(self.isi)
    
    def isi(self):
        cek = self.price.text()
        if cek == "":
            self.w.pelanggan.parent.showDialog("information", "Informasi","Masukkan nominal top up")
        if cek.isdigit():
            saldo = self.w.pelanggan.saldo.text()
            money = saldo[3:]
            lmoney = int(money) + int(self.price.text())
            val = "saldo= {}"
            val = val.format(lmoney)
            key = "idPelanggan = \"{}\""
            key = key.format(self.w.pelanggan.ID.text())
            self.w.mysql.update("pelanggan",val,key)
            self.Dialog.close()
            self.w.pelanggan.getProduct()
            self.w.pelanggan.parent.showDialog("information", "Informasi","Berhasil melakukan Top up\n sebesar Rp"+ str(self.price.text()))
            self.price.clear()
            self.w.pelanggan.img.setPixmap(self.w.pelanggan.pixmap.scaled(200, 170, QtCore.Qt.KeepAspectRatio))
            self.w.pelanggan.nama.clear()
            self.w.pelanggan.alamat.clear()
            self.w.pelanggan.hp.clear()
            self.w.pelanggan.saldo.clear()
            self.w.pelanggan.point.clear()
            self.w.pelanggan.point2.hide()
            self.w.pelanggan.ID.clear()
            self.w.pelanggan.gender.clear()
            self.w.pelanggan.radioButton.show()
            self.w.pelanggan.radioButton_2.show()
            self.w.pelanggan.gender.hide()
            self.w.pelanggan.getProduct()
            self.w.pelanggan.tabelPelanggan.clearSelection()
            self.w.pelanggan.ID.hide()
            self.w.pelanggan.labelid.hide()
        else:
            self.w.pelanggan.parent.showDialog("information", "Informasi","input harus berupa angka bukan karakter")

    def show(self):
        self.Dialog.exec_()