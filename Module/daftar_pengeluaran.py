from PyQt5 import QtCore, QtGui, QtWidgets

class DaftarPengeluaran():
    def __init__(self, parent):
        self.parent = parent
        self.daftarPengeluaranWidget = QtWidgets.QWidget(parent)
        self.daftarPengeluaranWidget.setMinimumSize(QtCore.QSize(350, 0))
        self.daftarPengeluaranWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.daftarPengeluaranWidget.setStyleSheet("")
        self.daftarPengeluaranWidget.setObjectName("daftarPengeluaranWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.daftarPengeluaranWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_4 = QtWidgets.QWidget(self.daftarPengeluaranWidget)
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
        self.gridLayout_3.addWidget(self.widget_6, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.widget_4)
        self.line.setStyleSheet("")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_3.addWidget(self.line, 1, 0, 1, 2)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_7 = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 4, 0, 1, 1)
        self.item = QtWidgets.QLineEdit(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.item.setFont(font)
        self.item.setPlaceholderText("")
        self.item.setClearButtonEnabled(True)
        self.item.setObjectName("item")
        self.gridLayout_2.addWidget(self.item, 0, 2, 1, 1)
        self.jumlah = QtWidgets.QLineEdit(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.jumlah.setFont(font)
        self.jumlah.setClearButtonEnabled(True)
        self.jumlah.setObjectName("jumlah")
        self.jumlah.setReadOnly(True)
        self.gridLayout_2.addWidget(self.jumlah, 3, 2, 1, 1)
        self.widget_7 = QtWidgets.QWidget(self.widget_4)
        self.widget_7.setObjectName("widget_7")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_7)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.simpanBtn = QtWidgets.QPushButton(self.widget_7)
        self.simpanBtn.setMinimumSize(QtCore.QSize(120, 35))
        self.simpanBtn.setMaximumSize(QtCore.QSize(150, 16777215))
        self.simpanBtn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.simpanBtn.setStyleSheet("QPushButton {\n"
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
        self.simpanBtn.setObjectName("inputProduk")
        self.simpanBtn.clicked.connect(self.addData)
        self.gridLayout_4.addWidget(self.simpanBtn, 0, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(600, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 0, 1, 1, 1)
        self.hapusProduk = QtWidgets.QPushButton(self.widget_7)
        self.hapusProduk.setMinimumSize(QtCore.QSize(120, 35))
        self.hapusProduk.setMaximumSize(QtCore.QSize(150, 16777215))
        self.hapusProduk.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.hapusProduk.setStyleSheet("QPushButton {\n"
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
        self.hapusProduk.setObjectName("hapusProduk")
        self.hapusProduk.clicked.connect(self.hapusData)
        self.gridLayout_4.addWidget(self.hapusProduk, 0, 2, 1, 1)
        self.gridLayout_2.addWidget(self.widget_7, 6, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.struk = QtWidgets.QLineEdit(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.struk.setFont(font)
        self.struk.setClearButtonEnabled(True)
        self.struk.setObjectName("struk")
        self.gridLayout_2.addWidget(self.struk, 4, 2, 1, 1)
        self.nominal = QtWidgets.QLineEdit(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nominal.setFont(font)
        self.nominal.setClearButtonEnabled(True)
        self.nominal.setObjectName("nominal")
        self.nominal.editingFinished.connect(self.sum)
        self.gridLayout_2.addWidget(self.nominal, 1, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 5, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)

        current = QtCore.QDate.currentDate()
        time = QtCore.QDateTime.currentDateTime().toString("HH:mm:ss")

        self.tanggal = QtWidgets.QDateEdit(self.widget_4)
        self.tanggal.setDate(current)
        self.tanggal.setCalendarPopup(True)
        self.tanggal.setObjectName("tanggal")
        self.tanggal.setMaximumSize(QtCore.QSize(200, 16777215))
        self.gridLayout_2.addWidget(self.tanggal, 5, 2, 1, 1)
        self.qty = QtWidgets.QLineEdit(self.widget_4)
        self.qty.setObjectName("lineEdit")
        self.qty.editingFinished.connect(self.sum)
        self.gridLayout_2.addWidget(self.qty, 2, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.daftarPengeluaranWidget)
        self.widget_5.setStyleSheet("")
        self.widget_5.setObjectName("widget_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.widget_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.cariBtn = QtWidgets.QPushButton(self.widget_5)
        self.cariBtn.setMinimumSize(QtCore.QSize(105, 30))
        self.cariBtn.setMaximumSize(QtCore.QSize(120, 35))
        self.cariBtn.setStyleSheet("QPushButton {\n"
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
        self.cariBtn.setObjectName("cariBtn")
        self.gridLayout_6.addWidget(self.cariBtn, 1, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget_5)
        self.label_6.setObjectName("label_6")
        self.gridLayout_6.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.widget_5)
        self.label_8.setObjectName("label_8")
        self.gridLayout_6.addWidget(self.label_8, 0, 1, 1, 1)
        self.dari_tanggal = QtWidgets.QDateEdit(self.widget_5)
        self.dari_tanggal.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dari_tanggal.setCalendarPopup(True)
        self.dari_tanggal.setDate(QtCore.QDate(current.year(), current.month(), 1))
        self.dari_tanggal.setObjectName("dari_tanggal")
        self.dari_tanggal.dateChanged.connect(self.ubah_dari)
        self.dari = self.dari_tanggal.date().toString("yyyy-MM-dd")
        self.gridLayout_6.addWidget(self.dari_tanggal, 1, 0, 1, 1)
        self.sampai_tanggal = QtWidgets.QDateEdit(self.widget_5)
        self.sampai_tanggal.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 1, 1), QtCore.QTime(0, 0, 0)))
        self.sampai_tanggal.setCalendarPopup(True)
        self.sampai_tanggal.setDate(current)
        self.sampai_tanggal.setObjectName("sampai_tanggal")
        self.sampai_tanggal.dateChanged.connect(self.ubah_sampai)
        self.sampai = self.sampai_tanggal.date().addDays(1).toString("yyyy-MM-dd")
        self.gridLayout_6.addWidget(self.sampai_tanggal, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem1, 1, 3, 1, 1)
        self.tabel_pengeluaran = QtWidgets.QTableWidget(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabel_pengeluaran.sizePolicy().hasHeightForWidth())
        self.tabel_pengeluaran.setSizePolicy(sizePolicy)
        self.tabel_pengeluaran.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tabel_pengeluaran.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tabel_pengeluaran.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabel_pengeluaran.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tabel_pengeluaran.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tabel_pengeluaran.setObjectName("tabel_pengeluaran")
        self.tabel_pengeluaran.setColumnCount(6)
        self.tabel_pengeluaran.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_pengeluaran.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_pengeluaran.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_pengeluaran.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_pengeluaran.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_pengeluaran.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_pengeluaran.setHorizontalHeaderItem(5, item)
        self.tabel_pengeluaran.horizontalHeader().setCascadingSectionResizes(True)
        self.tabel_pengeluaran.itemClicked.connect(self.selectData)
        header = self.tabel_pengeluaran.horizontalHeader()
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.gridLayout_6.addWidget(self.tabel_pengeluaran, 2, 0, 1, 4)
        self.verticalLayout_3.addWidget(self.widget_5)

        self.retranslateUi(parent)
        QtCore.QMetaObject.connectSlotsByName(parent)
        self.close()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_7.setText(_translate("Form", "No. Struk"))
        self.simpanBtn.setText(_translate("Form", "Simpan"))
        self.hapusProduk.setText(_translate("Form", "Hapus"))
        self.label_5.setText(_translate("Form", "Jumlah"))
        self.label_2.setText(_translate("Form", "Nominal"))
        self.label_4.setText(_translate("Form", "Tanggal"))
        self.label.setText(_translate("Form", "Item"))
        self.label_3.setText(_translate("Form", "Qty"))
        self.tanggal.setDisplayFormat(_translate("Form", "dd/MM/yyyy"))
        self.cariBtn.setText(_translate("Form", "Cari"))
        self.label_6.setText(_translate("Form", "Dari"))
        self.label_8.setText(_translate("Form", "Sampai"))
        self.dari_tanggal.setDisplayFormat(_translate("Form", "dd/MM/yyyy"))
        self.sampai_tanggal.setDisplayFormat(_translate("Form", "dd/MM/yyyy"))
        item = self.tabel_pengeluaran.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID Produk"))
        item = self.tabel_pengeluaran.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nama Produk"))
        item = self.tabel_pengeluaran.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Harga"))
        item = self.tabel_pengeluaran.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Qty"))
        item = self.tabel_pengeluaran.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Diskon %"))
        item = self.tabel_pengeluaran.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Jumlah"))

    def addData(self):
        time = QtCore.QDateTime.currentDateTime().toString("HH:mm:ss")
        tgl = self.tanggal.date().toString("yyyy-MM-dd") + " " + time
        if self.item.text() is "" or self.nominal.text() is "" or self.qty.text() is "" or self.jumlah.text() is "" or self.struk.text() is "":
            self.parent.showDialog("warning", "Harap isi form", "Harap melengkapi form yang tersedia")
            return
        selected = self.tabel_pengeluaran.currentItem()
        if selected is None or not selected.isSelected():
            val = "\"{}\",{},{},{},\"{}\",\"{}\""
            val = val.format(self.item.text(), self.nominal.text(),
                            self.qty.text(), self.jumlah.text(), self.struk.text(), tgl)
            self.parent.mysql.insertTo(
                "pengeluaran", "nama, harga, jumlah, total, struk, waktu", val)
            self.parent.showDialog("information", "Success", "Berhasil menambahkan item")
        elif selected.isSelected:
            val = "nama = \"{}\", harga = {}, jumlah = {}, total = {}, struk = \"{}\", waktu = \"{}\""
            val = val.format(self.item.text(), self.nominal.text(),
                            self.qty.text(), self.jumlah.text(),  self.struk.text(), tgl)
            row = self.tabel_pengeluaran.currentRow()                            
            key = "struk = \"{}\""
            key = key.format(self.tabel_pengeluaran.item(row,0).text())
            self.parent.mysql.update("pengeluaran", val, key)
            self.parent.showDialog("information", "Success", "Berhasil merubah data item")
        self.getData()

    def selectData(self):
        row = self.tabel_pengeluaran.currentRow()
        self.item.setText(self.tabel_pengeluaran.item(row,1).text())
        self.nominal.setText(self.tabel_pengeluaran.item(row,2).text())
        self.qty.setText(self.tabel_pengeluaran.item(row,3).text())
        self.jumlah.setText(self.tabel_pengeluaran.item(row,5).text())

    def hapusData(self):
        prompt = self.parent.showDialog("question", "Hapus Produk", "Apakah anda ingin menghapus produk?")
        if prompt == QtWidgets.QMessageBox.Yes:
            row = self.tabel_pengeluaran.currentRow()
            key = "struk=\"" + self.tabel_pengeluaran.item(row,0).text() + "\""
            self.parent.mysql.delete("pengeluaran", key)
            self.parent.showDialog("information", "Success", "Berhasil menghapus data item")
        self.getData()


    def getData(self):
        key = "waktu >= \"{}\" AND waktu < \"{}\""
        key = key.format(self.dari, self.sampai)
        q = self.parent.mysql.findCol(
            "struk, nama, harga, jumlah, diskon, total", "pengeluaran", key, True, "waktu DESC")
        if q is None:
            return
        self.tabel_pengeluaran.setRowCount(len(q))
        row = 0
        for r in q:
            col = 0
            for data in r:
                data = str(data)
                self.tabel_pengeluaran.setItem(
                    row, col, QtWidgets.QTableWidgetItem(data))
                col += 1
            row += 1

    def ubah_dari(self):
        self.dari = self.dari_tanggal.date().toString("yyyy-MM-dd")
        self.getData()

    def ubah_sampai(self):
        self.sampai = self.sampai_tanggal.date()
        self.sampai = self.sampai_tanggal.date().addDays(1).toString("yyyy-MM-dd")

        self.sampai = self.sampai.toString("yyyy-MM-dd")
        self.getData()

    def sum(self):
        if self.nominal.text() is "" or self.qty.text() is "":
            return
        harga = int(self.nominal.text())
        qty = int(self.qty.text())
        total = harga * qty
        self.jumlah.setText(str(total))

    def show(self):
        self.getData()
        self.daftarPengeluaranWidget.show()

    def close(self):
        self.daftarPengeluaranWidget.close()
