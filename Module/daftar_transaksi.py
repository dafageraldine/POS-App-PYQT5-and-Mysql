from PyQt5 import QtCore, QtGui, QtWidgets
from Module.transaksi_pelanggan import *
from PIL import Image, ImageWin

import os,datetime
import win32print, win32ui, win32con

class DaftarTransaksi():
    def __init__(self, parent):
        self.parent = parent
        self.query = parent.mysql
        current = QtCore.QDate.currentDate()

        self.daftarTransaksiWidget = QtWidgets.QWidget(parent)
        self.daftarTransaksiWidget.setMinimumSize(QtCore.QSize(350, 0))
        self.daftarTransaksiWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.daftarTransaksiWidget.setStyleSheet("")
        self.daftarTransaksiWidget.setObjectName("daftarTransaksiWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.daftarTransaksiWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_4 = QtWidgets.QWidget(self.daftarTransaksiWidget)
        self.widget_4.setStyleSheet("")
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabel_customer = QtWidgets.QTableWidget(self.widget_4)
        self.tabel_customer.setObjectName("tabel_customer")
        self.tabel_customer.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tabel_customer.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tabel_customer.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabel_customer.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tabel_customer.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tabel_customer.setColumnCount(4)
        self.tabel_customer.setRowCount(0)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabel_customer.sizePolicy().hasHeightForWidth())
        self.tabel_customer.setSizePolicy(sizePolicy)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_customer.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_customer.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_customer.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_customer.setHorizontalHeaderItem(3, item)
        self.tabel_customer.itemClicked.connect(self.getData)
        self.tabel_customer.itemDoubleClicked.connect(self.riwayatTransaksi)
        header = self.tabel_customer.horizontalHeader()
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

        self.gridLayout_2.addWidget(self.tabel_customer, 3, 0, 1, 6)
        self.label_sampai = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_sampai.setFont(font)
        self.label_sampai.setObjectName("label_sampai")
        self.gridLayout_2.addWidget(self.label_sampai, 1, 2, 1, 1)
        self.deleteBtn = QtWidgets.QPushButton(self.widget_4)
        self.deleteBtn.setMinimumSize(QtCore.QSize(100, 35))
        self.deleteBtn.setStyleSheet("QPushButton {\n"
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
        self.deleteBtn.setObjectName("deleteBtn")
        self.deleteBtn.clicked.connect(self.delete)
        if self.tabel_customer.currentItem() is None:
            self.deleteBtn.hide()

        self.gridLayout_2.addWidget(self.deleteBtn, 4, 5, 1, 1)
        self.label_dari = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_dari.setFont(font)
        self.label_dari.setObjectName("label_dari")
        self.gridLayout_2.addWidget(self.label_dari, 1, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.widget_4)
        self.line.setStyleSheet("")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 6, 0, 1, 6)
        self.dari_tanggal = QtWidgets.QDateEdit(self.widget_4)
        self.dari_tanggal.setDateTime(QtCore.QDateTime(QtCore.QDate(current.year(), current.month(), 1), QtCore.QTime(0, 0, 0)))
        self.dari_tanggal.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dari_tanggal.setCalendarPopup(True)
        self.dari_tanggal.setTimeSpec(QtCore.Qt.LocalTime)
        self.dari_tanggal.setDate(QtCore.QDate(current.year(), current.month(), 1))
        self.dari_tanggal.setObjectName("dari_tanggal")
        self.dari = self.dari_tanggal.date().toString("yyyy-MM-dd")
        self.dari_tanggal.dateChanged.connect(self.ubah_dari)

        self.gridLayout_2.addWidget(self.dari_tanggal, 2, 0, 1, 2)
        self.sampai_tanggal = QtWidgets.QDateEdit(self.widget_4)
        self.sampai_tanggal.setDateTime(QtCore.QDateTime(QtCore.QDate.currentDate(), QtCore.QTime.currentTime()))
        self.sampai_tanggal.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.sampai_tanggal.setCalendarPopup(True)
        self.sampai_tanggal.setTimeSpec(QtCore.Qt.LocalTime)
        self.sampai_tanggal.setDate(QtCore.QDate.currentDate())
        self.sampai_tanggal.setObjectName("sampai_tanggal")
        self.sampai_tanggal.dateChanged.connect(self.ubah_sampai)
        self.sampai = self.sampai_tanggal.date().addDays(1).toString("yyyy-MM-dd")

        self.gridLayout_2.addWidget(self.sampai_tanggal, 2, 2, 1, 2)
        self.cariBtn = QtWidgets.QPushButton(self.widget_4)
        self.cariBtn.setMinimumSize(QtCore.QSize(0, 35))
        self.cariBtn.setStyleSheet("QPushButton {\n"
"    background: #555;\n"
"    border-radius: 6px;\n"
"    border: none;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: #ccc;\n"
"    color: #555;\n"
"}")
        self.cariBtn.setObjectName("cariBtn")
        self.gridLayout_2.addWidget(self.cariBtn, 2, 4, 1, 1)
        self.verticalLayout_3.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.daftarTransaksiWidget)
        self.widget_5.setStyleSheet("")
        self.widget_5.setObjectName("widget_5")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_5)
        self.gridLayout.setObjectName("gridLayout")
        self.cetakBtn = QtWidgets.QPushButton(self.widget_5)
        self.cetakBtn.setMinimumSize(QtCore.QSize(135, 35))
        self.cetakBtn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cetakBtn.setStyleSheet("QPushButton {\n"
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
        self.cetakBtn.setObjectName("cetakBtn")
        self.cetakBtn.clicked.connect(self.print)
        self.getData()

        self.gridLayout.addWidget(self.cetakBtn, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.tabel_produk = QtWidgets.QTableWidget(self.widget_5)
        self.tabel_produk.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tabel_produk.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabel_produk.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tabel_produk.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tabel_produk.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tabel_produk.setObjectName("tabel_produk")
        self.tabel_produk.setColumnCount(6)
        self.tabel_produk.setRowCount(0)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabel_produk.sizePolicy().hasHeightForWidth())
        self.tabel_produk.setSizePolicy(sizePolicy)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_produk.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_produk.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_produk.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_produk.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_produk.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_produk.setHorizontalHeaderItem(5, item)
        self.gridLayout.addWidget(self.tabel_produk, 0, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 2, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.widget_5)
        header = self.tabel_produk.horizontalHeader()
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

        self.retranslateUi(parent)
        QtCore.QMetaObject.connectSlotsByName(parent)
        self.close()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tabel_customer.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID Transaksi"))
        item = self.tabel_customer.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nama Customer"))
        item = self.tabel_customer.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Nama Barang"))
        item = self.tabel_customer.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Tanggal"))
        self.label_sampai.setText(_translate("Form", "Sampai:"))
        self.deleteBtn.setText(_translate("Form", "Delete"))
        self.label_dari.setText(_translate("Form", "Dari:"))
        self.dari_tanggal.setDisplayFormat(_translate("Form", "dd/MM/yyyy"))
        self.sampai_tanggal.setDisplayFormat(_translate("Form", "dd/MM/yyyy"))
        self.cariBtn.setText(_translate("Form", "Cari"))
        self.cetakBtn.setText(_translate("Form", "Cetak Struk"))
        item = self.tabel_produk.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID Produk"))
        item = self.tabel_produk.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nama Produk"))
        item = self.tabel_produk.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Harga"))
        item = self.tabel_produk.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Qty"))
        item = self.tabel_produk.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Diskon%"))
        item = self.tabel_produk.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Jumlah"))

    def getData(self):
        if self.tabel_customer.currentItem() is not None:
            self.deleteBtn.show()
        key = "waktu >= \"{}\" AND waktu < \"{}\""
        key = key.format(self.dari,self.sampai)
        transaksi = self.parent.mysql.findCol("idTransaksi, pelanggan, produk, DATE_FORMAT(waktu, \'%d/%m/%Y\')", "transaksi", key, True)
        if transaksi is None:
            return
        self.tabel_customer.setRowCount(len(transaksi))
        row = 0
        for r in transaksi:
            col = 0
            for data in r:
                data = str(data)
                self.tabel_customer.setItem(row,col,QtWidgets.QTableWidgetItem(data))
                col = col + 1
            row = row + 1

        selected = self.tabel_customer.currentItem()
        if selected is None or not selected.isSelected():
            return
        elif selected.isSelected():
            customer = self.tabel_customer.currentRow()
            customer = self.tabel_customer.item(customer, 0).text()
            key = "idTransaksi = \"{}\" AND waktu >= \"{}\" AND waktu < \"{}\""
            key = key.format(customer,self.dari,self.sampai,self.sampai)

        produk = self.parent.mysql.findCol("idProduk, produk, harga, jumlah, total", "transaksi", key, True)
        if produk is None:
            return
        self.tabel_produk.setRowCount(len(produk))
        row = 0
        key = "idProduk = \"{}\""
        for r in produk:
            col = 0
            key = key.format(r[col])
            diskon = self.parent.mysql.findCol("diskon","daftarbarang",key,False)
            if diskon is None:
                diskon = [0]
            for data in r:
                if col == 4 and diskon != None:
                    self.tabel_produk.setItem(row,col,QtWidgets.QTableWidgetItem(str(diskon[0])))
                else:
                    self.tabel_produk.setItem(row,col,QtWidgets.QTableWidgetItem(str(data)))
                col = col+1
            self.tabel_produk.setItem(row,col,QtWidgets.QTableWidgetItem(str(data)))
            row = row+1

    def riwayatTransaksi(self):
        row = self.tabel_customer.currentRow()
        customer = self.tabel_customer.item(row, 1).text()
        key = "pelanggan = \"{}\""
        key = key.format(customer)
        self.nama_customer = customer
        self.customer = self.parent.mysql.findCol("idTransaksi, idProduk, produk, harga, jumlah, total, jenisTransaksi, line, waktu", "transaksi", key, True)
        riwayat = Transaksi_pelanggan(self.parent)
        riwayat.show()

    def ubah_dari(self):
        self.dari = self.dari_tanggal.date().toString("yyyy-MM-dd")
        self.getData()
    def ubah_sampai(self):
        self.sampai = self.sampai_tanggal.date()
        self.sampai = self.sampai_tanggal.date().addDays(1).toString("yyyy-MM-dd")
        self.getData()

    def delete(self):
        customer = self.tabel_customer.currentItem()

        if customer is None or not customer.isSelected():
            self.parent.showDialog("warning","Tidak dapat menghapus", "Harap pilih item yang akan dihapus")
            return
        elif customer.isSelected():
            prompt = self.parent.showDialog("question", "hapus data?", "Apakah ingin menghapus data?")
            if prompt == QtWidgets.QMessageBox.Yes:
                row = self.tabel_customer.currentRow()
                key = "idTransaksi = \"{}\""
                key = key.format(self.tabel_customer.item(row,0).text())
                self.parent.mysql.delete("transaksi", key)
                self.parent.showDialog("information", "Success", "Data berhasil dihapus!")
                self.getData()
            return

    def count(self):
        self.ttl =[]
        self.ttlname=[]
        self.ttlz =[]
        self.ttlid =[]
        self.ttlprice=[]
        self.rowz = self.tabel_produk.rowCount()
        for i in range (self.rowz):
            itemid = self.tabel_produk.item(i,0).text()
            itemname=self.tabel_produk.item(i,1).text()
            itemprice=self.tabel_produk.item(i,2).text() 
            itemz = self.tabel_produk.item(i,3).text()
            item = self.tabel_produk.item(i,5).text()
            self.ttl.append(int(item))
            self.ttlprice.append(itemprice)
            self.ttlname.append(itemname)
            self.ttlz.append(int(itemz))
            self.ttlid.append(itemid)
        self.alls = 0
        for x in range (self.rowz):
            self.alls = self.alls + self.ttl[x]
        self.total = "Rp " + str(self.alls)

    def struck(self):
        row = self.tabel_produk.rowCount()
        self.records = []
        for i in range (row):
            self.records.append([])
            for j in range (4):
                if j == 0:
                    item = self.tabel_produk.item(i,1).text()
                if j == 1:
                    item = self.tabel_produk.item(i,3).text()
                if j == 2:
                    item = self.tabel_produk.item(i,2).text()
                if j == 3:
                    item = self.tabel_produk.item(i,5).text()
                self.records[i].append(item)

    def print(self):
        sel = self.tabel_customer.currentItem()
        if sel is not None and sel.isSelected():
            self.count()
            self.struck()
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
            r = self.tabel_customer.currentRow()
            id_t =self.tabel_customer.item(r,0).text()
            t = datetime.datetime.now()
            date = t.strftime("%d/%m/%Y")
            time = t.strftime("%H:%M")
            tanggal = date + " " + time + " " + id_t
            y += 50
            printer.TextOut(80,y,tanggal)
            
            #print nama
            k = "nama=\"" + self.tabel_customer.item(r,1).text() + "\""
            self.id = self.query.findCol("idPelanggan", "pelanggan", k, False)
            id_p = self.id[0]
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
            total=str(self.total)
            total_harga = "Total Harga:"
            y += 50
            printer.TextOut(0,y,total_harga)
            printer.TextOut(280,y,total)
            #self.tt = self.total.text() 
            #result = self.tt
            
            #finish print
            printer.EndPage()
            printer.EndDoc()

    def show(self):
        self.getData()
        self.daftarTransaksiWidget.show()

    def close(self):
        self.daftarTransaksiWidget.close()
