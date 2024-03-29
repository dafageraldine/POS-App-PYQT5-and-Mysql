from PyQt5 import QtCore, QtGui, QtWidgets

class Transaksi_pelanggan():
    def __init__(self, w):
        self.w = w
        self.Dialog = QtWidgets.QDialog(w)
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(792, 576)
        self.label_nama = QtWidgets.QLabel(self.Dialog)
        self.label_nama.setGeometry(QtCore.QRect(230, 90, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_nama.setFont(font)
        self.label_nama.setObjectName("label_nama")
        self.label_saldo = QtWidgets.QLabel(self.Dialog)
        self.label_saldo.setGeometry(QtCore.QRect(230, 140, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_saldo.setFont(font)
        self.label_saldo.setObjectName("label_saldo")
        self.label_id = QtWidgets.QLabel(self.Dialog)
        self.label_id.setGeometry(QtCore.QRect(230, 40, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_id.setFont(font)
        self.label_id.setObjectName("label_id")
        self.id = QtWidgets.QLineEdit(self.Dialog)
        self.id.setGeometry(QtCore.QRect(290, 30, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.id.setFont(font)
        self.id.setReadOnly(True)
        self.id.setObjectName("id")
        self.nama = QtWidgets.QLineEdit(self.Dialog)
        self.nama.setGeometry(QtCore.QRect(290, 80, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.nama.setFont(font)
        self.nama.setReadOnly(True)
        self.nama.setObjectName("nama")
        self.saldo = QtWidgets.QLineEdit(self.Dialog)
        self.saldo.setGeometry(QtCore.QRect(290, 130, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.saldo.setFont(font)
        self.saldo.setReadOnly(True)
        self.saldo.setObjectName("saldo")
        self.tabel_transaksi = QtWidgets.QTableWidget(self.Dialog)
        self.tabel_transaksi.setGeometry(QtCore.QRect(10, 210, 771, 351))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabel_transaksi.setFont(font)
        self.tabel_transaksi.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabel_transaksi.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tabel_transaksi.setObjectName("tabel_transaksi")
        self.tabel_transaksi.setColumnCount(9)
        self.tabel_transaksi.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_transaksi.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_transaksi.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_transaksi.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_transaksi.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_transaksi.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_transaksi.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_transaksi.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_transaksi.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_transaksi.setHorizontalHeaderItem(8, item)
        self.tabel_transaksi.verticalHeader().setDefaultSectionSize(50)

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Riwayat Transaksi"))
        self.label_nama.setText(_translate("Dialog", "Nama"))
        self.label_saldo.setText(_translate("Dialog", "Saldo"))
        self.label_id.setText(_translate("Dialog", "ID"))
        item = self.tabel_transaksi.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "ID Transaksi"))
        item = self.tabel_transaksi.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "ID Produk"))
        item = self.tabel_transaksi.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Produk"))
        item = self.tabel_transaksi.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Harga"))
        item = self.tabel_transaksi.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Jumlah"))
        item = self.tabel_transaksi.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Total"))
        item = self.tabel_transaksi.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "Jenis"))
        item = self.tabel_transaksi.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "Line"))
        item = self.tabel_transaksi.horizontalHeaderItem(8)
        item.setText(_translate("Dialog", "Waktu"))
        self.close()

    def show(self):
        key = "nama = \"{}\""
        key = key.format(self.w.daftar_transaksi.nama_customer)
        data = self.w.mysql.findCol("idPelanggan, nama, saldo", "pelanggan", key, False)
        if data is not None:
            self.id.setText(data[0])
            self.nama.setText(data[1])
            self.saldo.setText(str(data[2]))
        row = 0
        self.tabel_transaksi.setRowCount(len(self.w.daftar_transaksi.customer))
        for r in self.w.daftar_transaksi.customer:
            col = 0
            for data in r:
                data = str(data)
                self.tabel_transaksi.setItem(row,col,QtWidgets.QTableWidgetItem(data))
                col += 1
            row += 1
        self.Dialog.exec_()

    def close(self):
        self.Dialog.close()
