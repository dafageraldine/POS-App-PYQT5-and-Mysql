from PyQt5 import QtCore, QtGui, QtWidgets
from Module.pelanggan import *
from PIL import Image, ImageWin

import os,datetime
import win32print, win32ui, win32con

class Transaksi():
    def __init__(self, parent):
        self.parent = parent
        self.pelanggan = parent.mysql
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.transaksiWidget = QtWidgets.QWidget(parent)
        self.transaksiWidget.setMinimumSize(QtCore.QSize(350, 0))
        self.transaksiWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.transaksiWidget.setStyleSheet("")
        self.transaksiWidget.setObjectName("transaksiWidget")
        self.transaksiWidget.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.transaksiWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_4 = QtWidgets.QWidget(self.transaksiWidget)
        self.widget_4.setStyleSheet("")
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget_6 = QtWidgets.QWidget(self.widget_4)
        self.widget_6.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_6.setStyleSheet("")
        self.widget_6.setObjectName("widget_6")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_6)
        self.gridLayout.setObjectName("gridLayout")
        self.img = QtWidgets.QLabel(self.widget_6)
        self.img.setMinimumSize(QtCore.QSize(180, 230))
        self.img.setStyleSheet("background: lightgrey;")
        self.img.setAlignment(QtCore.Qt.AlignCenter)
        pixmap = QtGui.QPixmap("placeholder.png")
        self.img.setPixmap(pixmap.scaled(200, 170, QtCore.Qt.KeepAspectRatio))
        self.img.setObjectName("img")

        self.gridLayout.addWidget(self.img, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(21, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 37, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem1, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(21, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 2, 1, 1)
        self.gridLayout_3.addWidget(self.widget_6, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.id = QtWidgets.QLineEdit(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.id.setFont(font)
        self.id.setPlaceholderText("")
        self.id.setClearButtonEnabled(True)
        self.id.setObjectName("id")
        self.id.returnPressed.connect(self.search)

        self.gridLayout_2.addWidget(self.id, 0, 2, 1, 1)
        self.gender = QtWidgets.QLineEdit(self.widget_4)
        self.gender.setReadOnly(True)
        self.gender.setObjectName("gender")
        self.gridLayout_2.addWidget(self.gender, 2, 2, 1, 1)
        self.alamat = QtWidgets.QLineEdit(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.alamat.setFont(font)
        self.alamat.setReadOnly(True)
        self.alamat.setClearButtonEnabled(True)
        self.alamat.setObjectName("alamat")
        self.gridLayout_2.addWidget(self.alamat, 3, 2, 1, 1)
        self.label_hpp = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_hpp.setFont(font)
        self.label_hpp.setObjectName("label_hpp")
        self.gridLayout_2.addWidget(self.label_hpp, 4, 0, 1, 1)
        self.nama = QtWidgets.QLineEdit(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nama.setFont(font)
        self.nama.setReadOnly(True)
        self.nama.setClearButtonEnabled(True)
        self.nama.setObjectName("nama")
        self.gridLayout_2.addWidget(self.nama, 1, 2, 1, 1)
        self.nomor_hp = QtWidgets.QLineEdit(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nomor_hp.setFont(font)
        self.nomor_hp.setReadOnly(True)
        self.nomor_hp.setClearButtonEnabled(True)
        self.nomor_hp.setObjectName("nomor_hp")
        self.gridLayout_2.addWidget(self.nomor_hp, 4, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)
        self.widget_7 = QtWidgets.QWidget(self.widget_4)
        self.widget_7.setMaximumSize(QtCore.QSize(16777215, 87))
        self.widget_7.setObjectName("widget_7")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_7)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.point = QtWidgets.QLineEdit(self.widget_7)
        self.point.setStyleSheet("background-color: #ff8f00;\n"
"border: 2px solid #ff8f00;\n"
"color:white;\n"
"font-size: 18pt;")
        self.point.setAlignment(QtCore.Qt.AlignCenter)
        self.point.setReadOnly(True)
        self.point.setObjectName("point")
        self.gridLayout_4.addWidget(self.point, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget_7)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: #00c853;")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 0, 1, 1, 1)
        self.saldo = QtWidgets.QLineEdit(self.widget_7)
        self.saldo.setStyleSheet("background-color: #00c853;\n"
"border: 2px solid #00c853;\n"
"color:white;\n"
"padding: 0 3px;\n"
"font-size: 18pt;")
        self.saldo.setAlignment(QtCore.Qt.AlignCenter)
        self.saldo.setReadOnly(True)
        self.saldo.setObjectName("saldo")
        self.gridLayout_4.addWidget(self.saldo, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget_7)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("    color: #ff8f00;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.widget_7, 5, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.widget_4)
        self.line.setStyleSheet("")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_3.addWidget(self.line, 1, 0, 1, 2)
        self.verticalLayout_3.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.transaksiWidget)
        self.widget_5.setStyleSheet("")
        self.widget_5.setObjectName("widget_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.widget_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.tabelTransaksi = QtWidgets.QTableWidget(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabelTransaksi.sizePolicy().hasHeightForWidth())
        self.tabelTransaksi.setSizePolicy(sizePolicy)
        self.tabelTransaksi.verticalHeader().setDefaultSectionSize(38)
        self.tabelTransaksi.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tabelTransaksi.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tabelTransaksi.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabelTransaksi.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tabelTransaksi.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tabelTransaksi.setObjectName("tabelTransaksi")
        self.tabelTransaksi.setColumnCount(6)
        self.tabelTransaksi.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabelTransaksi.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelTransaksi.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelTransaksi.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelTransaksi.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelTransaksi.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelTransaksi.setHorizontalHeaderItem(5, item)
        self.tabelTransaksi.horizontalHeader().setCascadingSectionResizes(True)
        header = self.tabelTransaksi.horizontalHeader()
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

        self.gridLayout_6.addWidget(self.tabelTransaksi, 0, 0, 1, 2)
        self.widget = QtWidgets.QWidget(self.widget_5)
        self.widget.setMinimumSize(QtCore.QSize(0, 46))
        self.widget.setObjectName("widget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.hapusBtn = QtWidgets.QPushButton(self.widget)
        self.hapusBtn.setMinimumSize(QtCore.QSize(0, 35))
        self.hapusBtn.setStyleSheet("QPushButton {\n"
"    background: #ff3d00;\n"
"    border-radius: 6px;\n"
"    border: none;\n"
"    color: white;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 2px solid #ff3d00;\n"
"    background: white;\n"
"    color: #ff3d00;\n"
"}")
        self.hapusBtn.setFlat(False)
        self.hapusBtn.setObjectName("hapusBtn")
        self.hapusBtn.clicked.connect(self.deleteProduct)
        self.horizontalLayout_2.addWidget(self.hapusBtn)

        self.prosesBtn = QtWidgets.QPushButton(self.widget)
        self.prosesBtn.setMinimumSize(QtCore.QSize(0, 35))
        self.prosesBtn.setStyleSheet("QPushButton {\n"
"    background: #2962ff;\n"
"    border-radius: 6px;\n"
"    border: none;\n"
"    color: white;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 2px solid #2962ff;\n"
"    background: white;\n"
"    color: #2962ff;\n"
"}")
        self.prosesBtn.setObjectName("prosesBtn")
        self.prosesBtn.clicked.connect(self.go)

        self.horizontalLayout_2.addWidget(self.prosesBtn)
        self.gridLayout_5.addLayout(self.horizontalLayout_2, 1, 4, 1, 1)
        self.total = QtWidgets.QLineEdit(self.widget)
        self.total.setMaximumSize(QtCore.QSize(390, 16777215))
        self.total.setMinimumSize(QtCore.QSize(300, 16777215))
        self.total.setStyleSheet("font-size: 14pt;\n"
"padding: 0 10px;")
        self.total.setAlignment(QtCore.Qt.AlignCenter)
        self.total.setReadOnly(True)
        self.total.setObjectName("total")
        self.gridLayout_5.addWidget(self.total, 0, 4, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(485, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem3, 1, 1, 1, 1)
        self.cancel = QtWidgets.QPushButton(self.widget)
        self.cancel.setMinimumSize(QtCore.QSize(200, 35))
        self.cancel.setStyleSheet("QPushButton {\n"
"    background: #ff3d00;\n"
"    border-radius: 6px;\n"
"    border: none;\n"
"    color: white;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 2px solid #ff3d00;\n"
"    background: white;\n"
"    color: #ff3d00;\n"
"}")
        self.cancel.setObjectName("cancel")
        self.cancel.clicked.connect(self.dont)

        self.gridLayout_5.addWidget(self.cancel, 2, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_5.addWidget(self.comboBox, 1, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_5.addItem(spacerItem4, 2, 1, 1, 1)
        self.gridLayout_6.addWidget(self.widget, 1, 0, 1, 2)
        self.verticalLayout_3.addWidget(self.widget_5)
        self.label_7 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 0, 2, 1, 1)
        self.line_game = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.line_game.setFont(font)
        self.line_game.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.line_game.setObjectName("line_game")
        self.gridLayout_5.addWidget(self.line_game, 0, 0, 1, 1)

        self.retranslateUi(parent)
        QtCore.QMetaObject.connectSlotsByName(parent)
        self.close()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.img.setText(_translate("Form", "Image"))
        self.label_3.setText(_translate("Form", "Gender"))
        self.label_hpp.setText(_translate("Form", "No. HP"))
        self.label.setText(_translate("Form", "ID"))
        self.label_2.setText(_translate("Form", "Nama"))
        self.label_5.setText(_translate("Form", "Alamat"))
        self.label_6.setText(_translate("Form", "Saldo"))
        self.label_4.setText(_translate("Form", "Point"))
        item = self.tabelTransaksi.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID Produk"))
        item = self.tabelTransaksi.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nama Produk"))
        item = self.tabelTransaksi.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Harga"))
        item = self.tabelTransaksi.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Qty"))
        item = self.tabelTransaksi.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Diskon %"))
        item = self.tabelTransaksi.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Jumlah"))
        self.hapusBtn.setText(_translate("Form", "Hapus"))
        self.prosesBtn.setText(_translate("Form", "Proses"))
        self.total.setText(_translate("Form", "Rp 0"))
        self.cancel.setText(_translate("Form", "Cancel"))
        self.label_7.setText(_translate("Form", "Total"))
        self.line_game.setText(_translate("Form", "Line Game"))

    def show(self):
            self.availableLine()
            self.transaksiWidget.show()
            
    def close(self):
            self.transaksiWidget.close()

    def showDialog(self, msgType: str, title: str, message: str):
        msgBox = QtWidgets.QMessageBox()
        if msgType is "critical":
            msgBox.critical(self, title, message)
        elif msgType is "warning":
            msgBox.warning(self, title, message)
        elif msgType is "information":
            msgBox.information(self, title, message)
        elif msgType is "question":
            return msgBox.question(self, title, message)

    def deleteProduct(self):
        i = 0
        tt = self.tabelTransaksi.currentRow()
        if tt <= -1:
            self.parent.showDialog("information", "Informasi","Tolong pilih item yang hendak dihapus")
            return 
        else:
            self.tabelTransaksi.removeRow(tt) 
        self.count()

    def search(self):
        if self.id.text() == "":
            self.parent.showDialog("warning","warning","tidak ada data yang cocok")
            return
        else:
            print(self.id.text())
        listPelanggan = self.pelanggan.find(
            "`idPelanggan`,`nama`,`gender`,`alamat`,`kontak`,`saldo`,`point`", "pelanggan",
            "`idPelanggan`", self.id.text(), True,
            "idPelanggan ASC")
        if len(listPelanggan) < 1:
            listPelanggan = self.pelanggan.find(
                "idPelanggan,nama,gender,alamat,kontak,saldo,point", "pelanggan",
                "rfid", self.id.text(), True,
                "idPelanggan ASC")

        if len(listPelanggan) < 1:
            self.parent.showDialog("warning","warning","tidak ada data yang cocok")
            return
        if len(listPelanggan) > 0:
            col = 0
            for data in listPelanggan:
                for val in data:
                    if col is 0:
                        val = self.id.setText(str(val))
                        path = QtCore.QDir.currentPath()
                        path = path + '/Module/static'
                        imagepath = path + '/' + self.id.text()+str(".jpg")
                        pixmap = QtGui.QPixmap(imagepath)
                        self.img.setPixmap(pixmap.scaled(200,170, QtCore.Qt.KeepAspectRatio))
                    if col is 1:
                        val = self.nama.setText(str(val))
                    if col is 2:
                        val = self.gender.setText(str(val))
                    if col is 3:
                        val = self.alamat.setText(str(val))
                    if col is 4:
                        val = self.nomor_hp.setText(str(val))
                    if col is 5:
                        val = self.saldo.setText(str(val))
                    if col is 6:
                        val = self.point.setText(str(val))
                    col = col + 1

    def dont(self):
        self.id.clear()
        self.nama.clear()
        self.gender.clear()
        self.alamat.clear()
        self.nomor_hp.clear()
        self.saldo.clear()
        self.point.clear()
        self.total.setText("Rp0")
        pixmap = QtGui.QPixmap("placeholder.png")
        self.img.setPixmap(pixmap.scaled(200, 170, QtCore.Qt.KeepAspectRatio))
        row = self.tabelTransaksi.rowCount()
        for i in range (row):
            self.tabelTransaksi.removeRow(0)
            self.tabelTransaksi.removeRow(i)

    def undo(self):
        self.id.clear()
        self.nama.clear()
        self.gender.clear()
        self.alamat.clear()
        self.nomor_hp.clear()
        self.saldo.clear()
        self.point.clear()
        pixmap = QtGui.QPixmap("placeholder.png")
        self.img.setPixmap(pixmap.scaled(200, 170, QtCore.Qt.KeepAspectRatio))

    def count(self):
        self.ttl =[]
        self.ttlname=[]
        self.ttlz =[]
        self.ttlid =[]
        self.ttlprice=[]
        self.rowz = self.tabelTransaksi.rowCount()
        for i in range (self.rowz):
            itemid = self.tabelTransaksi.item(i,0).text()
            itemname=self.tabelTransaksi.item(i,1).text()
            itemprice=self.tabelTransaksi.item(i,2).text() 
            itemz = self.tabelTransaksi.item(i,3).text()
            item = self.tabelTransaksi.item(i,5).text()
            self.ttl.append(int(item))
            self.ttlprice.append(itemprice)
            self.ttlname.append(itemname)
            self.ttlz.append(int(itemz))
            self.ttlid.append(itemid)
        self.alls = 0
        for x in range (self.rowz):
            self.alls = self.alls + self.ttl[x]
        self.total.setText("Rp " + str(self.alls))
        self.struck()


    def struck(self):
        row = self.tabelTransaksi.rowCount()
        self.records = []
        for i in range (row):
            self.records.append([])
            for j in range (4):
                if j == 0:
                    item = self.tabelTransaksi.item(i,1).text()
                if j == 1:
                    item = self.tabelTransaksi.item(i,3).text()
                if j == 2:
                    item = self.tabelTransaksi.item(i,2).text()
                if j == 3:
                    item = self.tabelTransaksi.item(i,5).text()
                self.records[i].append(item)

    def go(self):
        saldo = self.saldo.text()
        x = self.total.text()
        price = x[3:]
        row = self.tabelTransaksi.rowCount()
        if row == 0:
            self.parent.showDialog("warning", "warning","anda belum memilih item untuk dibeli")
        if row > 0:
            if self.nama.text() == "":
                self.parent.showDialog("warning", "warning","tidak ada data pelanggan pada form")
                return
            if (int(saldo) < int(price)):
                self.parent.showDialog("warning", "warning","saldo tidak mencukupi silahkan lakukan Top up terlebih dahulu")
                return
            if (int(saldo) >= int(price)):
                self.idt = self.pelanggan.select("id", "transaksi", False, "id DESC")
                if self.idt != None :
                    self.idt = '{:09d}'.format(self.idt[0]+1)
                else:
                    self.idt = '{:09d}'.format(1)
                self.idt = "PAY-" + str(self.idt)
                m = []
                for i in range (self.rowz):
                    keyz = "idProduk = \"{}\""
                    keyz = keyz.format(self.ttlid[i])
                    idp = self.ttlid[i]
                    nam = self.ttlname[i]
                    har = self.ttlprice[i]
                    tot = self.ttl[i]
                    y = self.pelanggan.findCol("stock","daftarbarang",keyz,True)
                    stockambil = self.ttlz[i]
                    for s in range(1):
                        stockawal = y[0][0]
                        stockakhir =  stockawal - stockambil
                        keluar = 0 - stockambil
                        val = "stock =  {}"
                        val = val.format(stockakhir)
                        vals = "\"{}\",\"{}\",{}"
                        vals = vals.format(idp,nam,keluar)
                        self.pelanggan.insertTo("stock","idProduk,nama,jumlah",vals)
                        self.pelanggan.update("daftarbarang",val,keyz)
                        valz = "\"{}\",\"{}\",\"{}\",{},{},\"{}\",\"{}\",\"{}\",{}"
                        valz = valz.format(self.idt,idp,nam,har,stockambil,self.id.text(),self.nama.text(),"beli",tot)
                        self.pelanggan.insertTo("transaksi","idTransaksi,idProduk,produk,harga,jumlah,idPelanggan,pelanggan,jenisTransaksi,total",valz)

                money = int(self.saldo.text())
                lastmoney = money - self.alls
                val = "saldo= {}"
                val = val.format(lastmoney)
                key = "idPelanggan = \"{}\""
                key = key.format(self.id.text())
                self.pelanggan.update("pelanggan",val,key)
                self.sendLine()
                self.struck()
                self.print()
                self.parent.showDialog("information", "Informasi","Transaksi Berhasil")
                self.dont()
                # QtWidgets.QMessageBox.Yes:
        # print("halo")

    def print(self):
        #value
        p1= ["barang","QTY","harga","total"]

        #variable
        y = 0
        x = 0

        #open image
        filename = "Module/foto_pada_struck.jpeg"
        img = Image.open(filename, 'r')
        img_width = img.size[0] + 20
        img_height = img.size[1] + 20

        #create enter
        for i in range(len(self.records)):
            p_tampung_0 = ""
            p_tampung_3 = ""
            flag = False
            data = len(self.records[i][0])
            for j in range(len(self.records[i][0])):
                if self.records[i][0][j] == " " or j == 6:
                    flag = True

                if flag == True:
                    p_tampung_3 += self.records[i][0][j]
                else:
                    p_tampung_0 += self.records[i][0][j]

                if j == data-1:
                    self.records[i][0] = p_tampung_0
                    self.records[i].append(p_tampung_3)
        
        #initial print
        printer = win32ui.CreateDC()
        printer.CreatePrinterDC(win32print.GetDefaultPrinter())
        print(win32print.GetDefaultPrinter())
        printer.StartDoc("EPPSON")
        printer.StartPage ()

        #print image
        dib = ImageWin.Dib(img)
        dib.draw(printer.GetHandleOutput(), (40, y, img_width, img_height))
        y+=180

        #print tanggal
        id_t =self.idt
        t = datetime.datetime.now()
        date = t.strftime("%d/%m/%Y")
        time = t.strftime("%H:%M")
        tanggal = date + " " + time + " " + id_t
        y += 50
        printer.TextOut(80,y,tanggal)
        
        #print nama
        id_p = self.id.text()
        list_p = "List order from " + id_p
        y += 50
        printer.TextOut(30,y,list_p)
        y +=50
        #self.rr = self.id.text()
        #id_pelanggan = self.rr
        
        #print nama table
        for i in range(4):
            printer.TextOut(x,y,p1[i])
            if i == 1:
                x += 80
            else:
                x += 110
            if i == 3:
                y += 50
                x = 0
        
        #print data table
        for i in range(len(self.records)):
            #print(i)
            for j in range(4):
                printer.TextOut(x,y,str(self.records[i][j]))
                if j == 0:
                    x += 120
                if j == 1:
                    x += 50
                if j == 2:
                    x += 120
                    
                #reset variable and add if string to much
                if j == 3:
                    x = 0
                    if self.records[i][4] != "":
                        y += 30
                        printer.TextOut(x,y,str(self.records[i][4]))
                    y += 50

       #print garis bawah
        garis_bawah = "_______________________________"
        #y += 50
        printer.TextOut(0,y,garis_bawah)
        
        #print total
        total=str(self.total.text())
        total_harga = "Total Harga:"
        y += 50
        printer.TextOut(0,y,total_harga)
        printer.TextOut(280,y,total)
        #self.tt = self.total.text() 
        #result = self.tt
        
        #finish print
        printer.EndPage()
        printer.EndDoc()

    def availableLine(self):

        self.comboBox.clear()

        lineList = self.parent.mysql.select("available,line", "IPline", True, "id ASC")
        getip = self.parent.socketThread.get_ip
        row = 0
 
        for data in lineList:
            col = 0
            for val in data:
                if col == 0:
                    if val == True:
                        col = col + 1
                elif col == 1:
                    self.comboBox.addItem(val)


    def sendLine(self):
        getip = self.parent.socketThread.get_ip
        setline = self.comboBox.currentText()
        setmessage = '#1,'+self.id.text()+'*'
        data = False
        setip = ""
        IPlist = self.parent.mysql.select("line,ipAddress", "IPline", True, "id ASC")
        
        row = 0
        for data in IPlist:
            col = 0
            for val in data:
                if col == 0:
                    if val == setline:
                        col = col + 1
                elif col == 1:
                    setip = val
                else:
                    return
            row = row + 1
        
        for myip in getip:
            addr,conn = myip
            if addr == setip:
                getconn = conn
                data = True
                break
            data = False

        if data == True:
            status = 'Connected'
            val = "available = {}"
            val = val.format(False)
            key = "ipAddress = \"{}\""
            key = key.format(setip)
            err = self.parent.mysql.update("IPline", val, key)

            val = "line = \"{}\""
            val = val.format(setline)
            key = "idPelanggan = \"{}\""
            key = key.format(self.id.text())
            self.pelanggan.update("pelanggan",val,key)
            getconn.send(bytes(setmessage + "\r\n",'UTF-8'))
        else:
            val = "line = \"{}\""
            val = val.format("")
            key = "idPelanggan = \"{}\""
            key = key.format(self.id.text())
            self.pelanggan.update("pelanggan",val,key)
            
        self.availableLine()
