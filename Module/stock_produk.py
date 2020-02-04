from PyQt5 import QtCore, QtGui, QtWidgets
from Module.keypad import *
import threading

w = None

class Stock():
    def __init__(self, parent):
        w = parent
        self.parent = parent
        self.mysql = parent.mysql
        self.stockWidget = QtWidgets.QWidget(parent)
        self.stockWidget.setMinimumSize(QtCore.QSize(350, 0))
        self.stockWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.stockWidget.setStyleSheet("")
        self.stockWidget.setObjectName("stockWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.stockWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.stockWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_stock = QtWidgets.QWidget()
        self.tab_stock.setObjectName("tab_stock")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_stock)
        self.gridLayout.setObjectName("gridLayout")
        self.pencarian = QtWidgets.QLineEdit(self.tab_stock)
        self.pencarian.setMinimumSize(QtCore.QSize(0, 30))
        self.pencarian.setStyleSheet("border: 1px solid #eee;\n"
"border-radius: 6px;")
        self.pencarian.setAlignment(QtCore.Qt.AlignCenter)
        self.pencarian.setObjectName("pencarian")
        self.pencarian.textChanged.connect(self.cariStock)

        self.gridLayout.addWidget(self.pencarian, 6, 0, 1, 3)
        self.id = QtWidgets.QLineEdit(self.tab_stock)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.id.setFont(font)
        self.id.setStyleSheet("padding: 0 10px;")
        self.id.setObjectName("id")
        self.gridLayout.addWidget(self.id, 1, 1, 1, 1)
        self.stock_masuk = QtWidgets.QLineEdit(self.tab_stock)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stock_masuk.setFont(font)
        self.stock_masuk.setStyleSheet("padding: 0 10px;")
        self.stock_masuk.setObjectName("stock_masuk")
        self.gridLayout.addWidget(self.stock_masuk, 3, 1, 1, 1)
        self.restockBtn = QtWidgets.QPushButton(self.tab_stock)
        self.restockBtn.setMinimumSize(QtCore.QSize(0, 35))
        self.restockBtn.setStyleSheet("QPushButton {\n"
"    border-radius: 6px;\n"
"    background: #2962ff;\n"
"    border: none;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 2px solid #2962ff;\n"
"    background: white;\n"
"    color: #2962ff;\n"
"}")
        self.restockBtn.setObjectName("restockBtn")
        self.restockBtn.clicked.connect(self.restocking)

        self.gridLayout.addWidget(self.restockBtn, 9, 3, 1, 1)
        self.tabel_stock = QtWidgets.QTableWidget(self.tab_stock)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabel_stock.sizePolicy().hasHeightForWidth())
        self.tabel_stock.setSizePolicy(sizePolicy)
        self.tabel_stock.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tabel_stock.setStyleSheet("")
        self.tabel_stock.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tabel_stock.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabel_stock.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tabel_stock.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tabel_stock.setObjectName("tabel_stock")
        self.tabel_stock.setColumnCount(5)
        self.tabel_stock.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_stock.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_stock.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_stock.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_stock.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_stock.setHorizontalHeaderItem(4, item)
        self.tabel_stock.horizontalHeader().setCascadingSectionResizes(True)
        header = self.tabel_stock.horizontalHeader()
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tabel_stock.itemClicked.connect(self.selectStock)

        self.gridLayout.addWidget(self.tabel_stock, 7, 0, 2, 4)
        self.label_namaproduk = QtWidgets.QLabel(self.tab_stock)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_namaproduk.setFont(font)
        self.label_namaproduk.setObjectName("label_namaproduk")
        self.gridLayout.addWidget(self.label_namaproduk, 2, 0, 1, 1)
        self.label_title = QtWidgets.QLabel(self.tab_stock)
        self.label_title.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.gridLayout.addWidget(self.label_title, 0, 0, 1, 2)
        self.stock_keluar = QtWidgets.QLineEdit(self.tab_stock)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stock_keluar.setFont(font)
        self.stock_keluar.setStyleSheet("padding: 0 10px;")
        self.stock_keluar.setObjectName("stock_keluar")
        self.gridLayout.addWidget(self.stock_keluar, 4, 1, 1, 1)
        # self.calendarWidget = QtWidgets.QCalendarWidget(self.tab_stock)
        # self.calendarWidget.setObjectName("calendarWidget")
        # self.calendarWidget.setSelectedDate(QtCore.QDate.currentDate())
        # self.calendarWidget.selectionChanged.connect(self.calendarStock)
        # self.waktuStock = self.calendarWidget.selectedDate().toString("yyyy-MM-dd")
        # self.gridLayout.addWidget(self.calendarWidget, 1, 2, 4, 2)
        self.label_id = QtWidgets.QLabel(self.tab_stock)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_id.setFont(font)
        self.label_id.setObjectName("label_id")
        self.gridLayout.addWidget(self.label_id, 1, 0, 1, 1)
        self.label_stockkeluar = QtWidgets.QLabel(self.tab_stock)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_stockkeluar.setFont(font)
        self.label_stockkeluar.setObjectName("label_stockkeluar")
        self.gridLayout.addWidget(self.label_stockkeluar, 4, 0, 1, 1)
        self.label_stockmasuk = QtWidgets.QLabel(self.tab_stock)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_stockmasuk.setFont(font)
        self.label_stockmasuk.setObjectName("label_stockmasuk")
        self.gridLayout.addWidget(self.label_stockmasuk, 3, 0, 1, 1)
        self.nama_produk = QtWidgets.QLineEdit(self.tab_stock)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nama_produk.setFont(font)
        self.nama_produk.setStyleSheet("padding: 0 10px;")
        self.nama_produk.setObjectName("nama_produk")
        self.gridLayout.addWidget(self.nama_produk, 2, 1, 1, 1)
        self.cariBtn = QtWidgets.QPushButton(self.tab_stock)
        self.cariBtn.setMinimumSize(QtCore.QSize(130, 35))
        self.cariBtn.setStyleSheet("QPushButton {\n"
"    border-radius: 6px;\n"
"    background: #555;\n"
"    border: none;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background:#ccc;\n"
"    color: #555;\n"
"}")
        self.cariBtn.setObjectName("cariBtn")
        self.gridLayout.addWidget(self.cariBtn, 6, 3, 1, 1)
        self.tabWidget.addTab(self.tab_stock, "")
        self.tab_restock = QtWidgets.QWidget()
        self.tab_restock.setObjectName("tab_restock")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_restock)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.nama_produk_2 = QtWidgets.QLineEdit(self.tab_restock)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nama_produk_2.setFont(font)
        self.nama_produk_2.setStyleSheet("padding: 0 10px;")
        self.nama_produk_2.setObjectName("nama_produk_2")
        self.nama_produk_2.setReadOnly(True)
        self.gridLayout_2.addWidget(self.nama_produk_2, 2, 2, 1, 1)
        self.jumlah_stockmasuk = MyLineEdit(self.tab_restock)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.jumlah_stockmasuk.setFont(font)
        self.jumlah_stockmasuk.setStyleSheet("padding: 0 10px;")
        self.jumlah_stockmasuk.setObjectName("jumlah_stockmasuk")
        self.gridLayout_2.addWidget(self.jumlah_stockmasuk, 3, 2, 1, 1)
        self.id_2 = QtWidgets.QLineEdit(self.tab_restock)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.id_2.setFont(font)
        self.id_2.setStyleSheet("padding: 0 10px;")
        self.id_2.editingFinished.connect(self.checkItem)
        self.id_2.setObjectName("id_2")
        self.id_2.setReadOnly(True)

        self.gridLayout_2.addWidget(self.id_2, 1, 2, 1, 1)
        self.label_namaproduk_2 = QtWidgets.QLabel(self.tab_restock)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_namaproduk_2.setFont(font)
        self.label_namaproduk_2.setObjectName("label_namaproduk_2")
        self.gridLayout_2.addWidget(self.label_namaproduk_2, 2, 0, 1, 1)
        self.label_id_2 = QtWidgets.QLabel(self.tab_restock)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_id_2.setFont(font)
        self.label_id_2.setObjectName("label_id_2")
        self.gridLayout_2.addWidget(self.label_id_2, 1, 0, 1, 2)
        self.tabel_restock = QtWidgets.QTableWidget(self.tab_restock)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabel_restock.sizePolicy().hasHeightForWidth())
        self.tabel_restock.setSizePolicy(sizePolicy)
        self.tabel_restock.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tabel_restock.setStyleSheet("")
        self.tabel_restock.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tabel_restock.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabel_restock.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tabel_restock.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tabel_restock.setObjectName("tabel_restock")
        self.tabel_restock.setColumnCount(4)
        self.tabel_restock.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_restock.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_restock.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_restock.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_restock.setHorizontalHeaderItem(3, item)
        self.tabel_restock.horizontalHeader().setCascadingSectionResizes(True)
        header = self.tabel_restock.horizontalHeader()
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tabel_restock.itemClicked.connect(self.selectRestock)

        self.gridLayout_2.addWidget(self.tabel_restock, 7, 0, 1, 7)
        self.calendarWidget_2 = QtWidgets.QCalendarWidget(self.tab_restock)
        self.calendarWidget_2.setObjectName("calendarWidget_2")
        self.calendarWidget_2.setSelectedDate(QtCore.QDate.currentDate())
        self.calendarWidget_2.selectionChanged.connect(self.calendarRestock)
        self.waktuRestock = self.calendarWidget_2.selectedDate().toString("yyyy-MM-dd")
        self.gridLayout_2.addWidget(self.calendarWidget_2, 1, 4, 4, 3)
        self.simpanBtn = QtWidgets.QPushButton(self.tab_restock)
        self.simpanBtn.setMinimumSize(QtCore.QSize(0, 35))
        self.simpanBtn.setStyleSheet("QPushButton {\n"
"    border-radius: 6px;\n"
"    background: #2962ff;\n"
"    border: none;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 2px solid #2962ff;\n"
"    background: white;\n"
"    color: #2962ff;\n"
"}")
        self.simpanBtn.setObjectName("simpanBtn")
        self.simpanBtn.clicked.connect(self.addStock)
        self.gridLayout_2.addWidget(self.simpanBtn, 9, 6, 1, 1)
        self.pencarian_2 = QtWidgets.QLineEdit(self.tab_restock)
        self.pencarian_2.setMinimumSize(QtCore.QSize(0, 30))
        self.pencarian_2.setStyleSheet("border: 1px solid #eee;\n"
"border-radius: 6px;")
        self.pencarian_2.setAlignment(QtCore.Qt.AlignCenter)
        self.pencarian_2.setObjectName("pencarian_2")
        self.pencarian_2.textChanged.connect(self.cariRestock)

        self.gridLayout_2.addWidget(self.pencarian_2, 6, 0, 1, 6)
        self.label_title_2 = QtWidgets.QLabel(self.tab_restock)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_title_2.setFont(font)
        self.label_title_2.setObjectName("label_title_2")
        self.gridLayout_2.addWidget(self.label_title_2, 0, 0, 1, 2)
        self.label_jumlahstock = QtWidgets.QLabel(self.tab_restock)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_jumlahstock.setFont(font)
        self.label_jumlahstock.setObjectName("label_jumlahstock")
        self.gridLayout_2.addWidget(self.label_jumlahstock, 3, 0, 1, 1)
        self.hapusBtn = QtWidgets.QPushButton(self.tab_restock)
        self.hapusBtn.setMinimumSize(QtCore.QSize(135, 35))
        self.hapusBtn.setStyleSheet("QPushButton {\n"
"    border-radius: 6px;\n"
"    background: #ff3d00;\n"
"    border: none;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 2px solid #ff3d00;\n"
"    background: white;\n"
"    color: #ff3d00;\n"
"}")
        self.hapusBtn.setObjectName("hapusBtn")
        self.hapusBtn.clicked.connect(self.deleteRestock)
        self.gridLayout_2.addWidget(self.hapusBtn, 9, 5, 1, 1)
        self.cariBtn_2 = QtWidgets.QPushButton(self.tab_restock)
        self.cariBtn_2.setMinimumSize(QtCore.QSize(135, 35))
        self.cariBtn_2.setStyleSheet("QPushButton {\n"
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
        self.cariBtn_2.setObjectName("cariBtn_2")
        self.gridLayout_2.addWidget(self.cariBtn_2, 6, 6, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 3, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem1, 5, 0, 1, 1)
        self.tabWidget.addTab(self.tab_restock, "")
        self.tabWidget.currentChanged.connect(self.tabChanged)
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.getStock("get")
        self.restockBtn.hide()

        self.retranslateUi(parent)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(parent)
        self.close()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pencarian.setPlaceholderText(_translate("Form", "Masukkan id / nama produk"))
        self.restockBtn.setText(_translate("Form", "Restock"))
        item = self.tabel_stock.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID"))
        item = self.tabel_stock.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nama Produk"))
        item = self.tabel_stock.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Stock Masuk"))
        item = self.tabel_stock.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Stock Keluar"))
        item = self.tabel_stock.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Sisa Stock"))
        self.label_namaproduk.setText(_translate("Form", "Nama Produk"))
        self.label_title.setText(_translate("Form", "Data Stock Produk"))
        self.label_id.setText(_translate("Form", "ID Produk"))
        self.label_stockkeluar.setText(_translate("Form", "Stock Keluar"))
        self.label_stockmasuk.setText(_translate("Form", "Stock Masuk"))
        self.cariBtn.setText(_translate("Form", "Cari"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_stock), _translate("Form", "Stock"))
        self.label_namaproduk_2.setText(_translate("Form", "Nama Produk"))
        self.label_id_2.setText(_translate("Form", "ID Produk"))
        item = self.tabel_restock.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID"))
        item = self.tabel_restock.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nama Produk"))
        item = self.tabel_restock.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Jumlah Stock Masuk"))
        item = self.tabel_restock.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Tanggal"))
        self.simpanBtn.setText(_translate("Form", "Simpan"))
        self.pencarian_2.setPlaceholderText(_translate("Form", "Masukkan id / nama produk"))
        self.label_title_2.setText(_translate("Form", "Data Restock"))
        self.label_jumlahstock.setText(_translate("Form", "Jumlah Stock Masuk"))
        self.hapusBtn.setText(_translate("Form", "Hapus"))
        self.cariBtn_2.setText(_translate("Form", "Cari"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_restock), _translate("Form", "Restock"))

    def tabChanged(self):
        self.getStock("get")
        self.getRestock("get")
        self.deselect()

    def calendarStock(self):
        self.waktuStock = self.calendarWidget.selectedDate().toString("yyyy-MM-dd")
        # self.getStock("cari")
    
    def calendarRestock(self):
        self.waktuRestock = self.calendarWidget_2.selectedDate().toString("yyyy-MM-dd")
        self.getRestock("cari")

    def selectStock(self):
        row = self.tabel_stock.currentRow()
        self.id.setText(self.tabel_stock.item(row, 0).text())
        self.nama_produk.setText(self.tabel_stock.item(row,1).text())
        self.stock_masuk.setText(self.tabel_stock.item(row,2).text())
        self.stock_keluar.setText(self.tabel_stock.item(row,3).text())
        sisa = self.tabel_stock.item(row, 4).text()
        self.restockBtn.show()
        # if int(sisa) < 1:
            # self.restockBtn.show()
        #     return
        # self.restockBtn.hide()

    def handler(self):
        print("PING!")

    def selectRestock(self):
        row = self.tabel_restock.currentRow()
        self.id_2.setText(self.tabel_restock.item(row,0).text())
        self.nama_produk_2.setText(self.tabel_restock.item(row,1).text())
        self.jumlah_stockmasuk.setText(self.tabel_restock.item(row,2).text())
        time = self.tabel_restock.item(row,3).text()
        time = time.split('/')
        d = QtCore.QDate()
        d.setDate(int(time[2]),int(time[1]),int(time[0]))
        self.calendarWidget_2.setSelectedDate(d)

    def deleteRestock(self):
        item = self.tabel_restock.currentItem()
        row = self.tabel_restock.currentRow()
        if item is None or not item.isSelected():
            self.parent.showDialog("warning", "Peringatan", "Harap pilih data yang akan dihapus")
            return
        key = "idProduk = \"{}\" AND waktu LIKE \'" + self.waktuRestock + "%\'"
        key = key.format(self.tabel_restock.item(row, 0).text())
        res = self.mysql.findCol("waktu", "stock", key, True, "waktu DESC")

        key = "idProduk = \"{}\" AND waktu LIKE \'" + str(res[row][0]) + "%\'"
        key = key.format(self.tabel_restock.item(row, 0).text())
        self.mysql.delete("stock", key)
        self.getRestock("get")
        self.parent.showDialog("information", "Success", "Data berhasil dihapus")

    def getStock(self, mode):
        if mode == "cari":
            key = "idProduk LIKE \"%{}%\" OR nama LIKE \"%{}%\""
            key = key.format(self.pencarian.text(),self.pencarian.text())
            listProduk = self.mysql.findCol(
                "idProduk,nama,stock", "daftarbarang", key, True, "idProduk ASC")
            # q = "SELECT idProduk,nama,stock FROM daftarbarang "
            # q = q + "WHERE idProduk LIKE \"%" + self.pencarian.text() +"%\" AND waktu LIKE \'%" + self.waktuStock +"%\' ORDER BY waktu DESC"
            # listProduk = self.mysql.fetch(q, True)
        else:
            listProduk = self.mysql.select(
                "idProduk,nama,stock", "daftarbarang", True, "idProduk ASC")
        self.tabel_stock.setRowCount(len(listProduk))
        row = 0
        for data in listProduk:
            col = 0
            key = "idProduk = \"{}\""
            key = key.format(data[0])
            Out = self.mysql.findCol("jumlah", "stock", key+"AND jumlah < 0", "id ASC")
            In = self.mysql.findCol("jumlah", "stock", key+" AND jumlah > 0", "id ASC")
            for val in data:
                val = str(val)
                if col == 2:
                    col = 4
                self.tabel_stock.setItem(
                row, col, QtWidgets.QTableWidgetItem(val))
                col = col + 1
                if col == 5:
                    sumVal = 0
                    for val in In:
                        sumVal = sumVal + val[0]
                    total = sumVal
                    self.tabel_stock.setItem(
                    row, 2, QtWidgets.QTableWidgetItem(str(sumVal)))
                    sumVal = 0
                    for val in Out:
                        sumVal = sumVal + val[0]
                    total = total + sumVal
                    sumVal = abs(sumVal)
                    self.tabel_stock.setItem(
                    row, 3, QtWidgets.QTableWidgetItem(str(sumVal)))
                    self.tabel_stock.setItem(
                    row, 4, QtWidgets.QTableWidgetItem(str(total)))
                    val = "stock = {}"
                    val = val.format(total)
                    self.mysql.update("daftarbarang", val, key)
                    
            row = row + 1

    def getRestock(self, mode):
        if mode == "cari":
            q = "SELECT idProduk,nama,jumlah,DATE_FORMAT(waktu, \'%d/%m/%Y\') FROM stock "
            q = q + "WHERE idProduk LIKE \"%" + self.pencarian_2.text() +"%\" AND jumlah > 0 AND waktu LIKE \'%" + self.waktuRestock +"%\' ORDER BY waktu DESC"
            res = self.mysql.fetch(q, True)
            if len(res) < 1:
                q = "SELECT idProduk,nama,jumlah,DATE_FORMAT(waktu, \'%d/%m/%Y\') FROM stock "
                q = q + "WHERE nama LIKE \"%" + self.pencarian_2.text() +"%\" AND jumlah > 0 AND waktu LIKE \'%" + self.waktuRestock +"%\' ORDER BY waktu DESC"
                res = self.mysql.fetch(q, True)

        else:
            key = "jumlah > 0 AND waktu LIKE \"%" + self.waktuRestock +"%\""
            res = self.mysql.findCol("idProduk,nama,jumlah,DATE_FORMAT(waktu, \'%d/%m/%Y\')","stock", key, True, "waktu DESC")
        self.tabel_restock.setRowCount(len(res))
        row = 0
        for r in res:
            col = 0
            for data in r:
                self.tabel_restock.setItem(row,col,QtWidgets.QTableWidgetItem(str(data)))
                col = col+1

            row = row+1

    def addStock(self):
        idBarang = self.id_2.text()
        namaBarang = self.nama_produk_2.text()
        jumlahBarang = self.jumlah_stockmasuk.text()
        if idBarang is "" or namaBarang is "" or jumlahBarang is "":
            self.parent.showDialog("warning", "Tolong isi form", "Setiap form harus terisi")
            return

        key = "idProduk = \"{}\""        
        key = key.format(self.id_2.text())
        produk = self.mysql.findCol("idProduk", "daftarbarang", key, True)
        if len(produk) < 1:
            self.parent.showDialog("warning", "Tidak ditemukan", "Id Produk tidak cocok")
            return

        current = self.tabel_restock.currentItem()
        if current is None or not current.isSelected():
            val = "\"{}\",\"{}\",{}"
            val = val.format(self.id_2.text(), self.nama_produk_2.text(), self.jumlah_stockmasuk.text())
            self.mysql.insertTo("stock", "idProduk, nama, jumlah", val)
        elif current.isSelected():
            row = self.tabel_restock.currentRow()
            val = "jumlah = {}"
            val = val.format(self.jumlah_stockmasuk.text())
            key = "idProduk = \"{}\" AND waktu LIKE \'" + self.waktuRestock + "%\'"
            key = key.format(self.tabel_restock.item(row, 0).text())
            res = self.mysql.findCol("waktu", "stock", key, True, "waktu DESC")
            key = "idProduk = \"{}\" AND waktu LIKE \'" + str(res[row][0]) + "%\'"
            key = key.format(self.tabel_restock.item(row, 0).text())
            self.mysql.update("stock", val, key)
    
        key = "idProduk = \"{}\""        
        key = key.format(self.id_2.text())
        res = self.mysql.findCol("stock", "daftarbarang", key, False)
        res = int(res[0]) + int(self.jumlah_stockmasuk.text())
        val = "stock = {}"
        val = val.format(res)
        self.mysql.update("daftarbarang", val, key)
        self.getRestock("get")
        self.parent.showDialog("information", "Success", "Berhasil menambahkan stock produk!")
        self.deselect()

    def cariStock(self):
        self.getStock("cari")

    def cariRestock(self):
        self.getRestock("cari")

    def restocking(self):
        current = self.tabel_stock.currentRow()
        ID = self.tabel_stock.item(current, 0).text()
        sisa = self.tabel_stock.item(current, 4).text()
        self.tabWidget.setCurrentIndex(1)
        self.id_2.setText(ID)
        self.checkItem()
        self.jumlah_stockmasuk.setText(sisa)

    def checkItem(self):
        key = "idProduk = \"{}\""
        key = key.format(self.id_2.text())
        res = self.mysql.findCol("idProduk, nama", "daftarbarang", key, False)
        if res is not None:
            self.id_2.setText(res[0])
            self.nama_produk_2.setText(res[1])
            # self.jumlah_stockmasuk.setFocus()

    def deselect(self):
        self.tabel_stock.clearSelection()
        self.tabel_restock.clearSelection()
        self.jumlah_stockmasuk.clearFocus()
    
    def show(self):
        self.stockWidget.show()

    def close(self):
        self.stockWidget.close()        

class MyLineEdit(QtWidgets.QLineEdit):
    def focusInEvent(self, event):
        form = super(MyLineEdit, self)
        current = form.text()
        form.clearFocus()
        key = Keypad(w, 4, "Stock")
        key.value.setText(current)
        key.show()
        form.focusInEvent(event)
        form.setText(key.val)