from PyQt5 import QtCore, QtGui, QtWidgets
import xlsxwriter
import os
import sys
from shutil import copyfile
import xlrd
from xlutils.copy import copy
from xlrd import open_workbook

class RekapTransaksi():
    def __init__(self, parent):
        self.parent = parent
        current = QtCore.QDate.currentDate()
        self.rekapTransaksiWidget = QtWidgets.QWidget(parent)
        self.rekapTransaksiWidget.setMinimumSize(QtCore.QSize(350, 0))
        self.rekapTransaksiWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.rekapTransaksiWidget.setStyleSheet("")
        self.rekapTransaksiWidget.setObjectName("rekapTransaksiWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.rekapTransaksiWidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.rekapTransaksiWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_transaksi = QtWidgets.QWidget()
        self.tab_transaksi.setObjectName("tab_transaksi")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_transaksi)
        self.gridLayout.setObjectName("gridLayout")
        self.tabel_transaksi = QtWidgets.QTableWidget(self.tab_transaksi)
        self.tabel_transaksi.setObjectName("tabel_transaksi")
        self.tabel_transaksi.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tabel_transaksi.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tabel_transaksi.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabel_transaksi.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tabel_transaksi.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tabel_transaksi.setColumnCount(4)
        self.tabel_transaksi.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_transaksi.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_transaksi.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_transaksi.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_transaksi.setHorizontalHeaderItem(3, item)
        self.gridLayout.addWidget(self.tabel_transaksi, 3, 0, 1, 5)
        self.label_dari = QtWidgets.QLabel(self.tab_transaksi)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_dari.setFont(font)
        self.label_dari.setObjectName("label_dari")
        self.gridLayout.addWidget(self.label_dari, 1, 0, 1, 1)
        self.cariBtn = QtWidgets.QPushButton(self.tab_transaksi)
        self.cariBtn.setMinimumSize(QtCore.QSize(0, 35))
        self.cariBtn.setMaximumSize(QtCore.QSize(120, 16777215))
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
        self.gridLayout.addWidget(self.cariBtn, 2, 4, 1, 1)
        self.dari_tanggal = QtWidgets.QDateEdit(self.tab_transaksi)
        self.dari_tanggal.setAlignment(QtCore.Qt.AlignCenter)
        self.dari_tanggal.setCalendarPopup(True)
        self.dari_tanggal.setDate(QtCore.QDate(current.year(), current.month(), 1))
        self.dari_tanggal.setObjectName("dari_tanggal")
        self.dari = self.dari_tanggal.date().toString("yyyy-MM-dd")
        self.gridLayout.addWidget(self.dari_tanggal, 2, 0, 1, 2)
        self.sampai_tanggal = QtWidgets.QDateEdit(self.tab_transaksi)
        self.sampai_tanggal.setAlignment(QtCore.Qt.AlignCenter)
        self.sampai_tanggal.setCalendarPopup(True)
        self.sampai_tanggal.setDate(current)
        self.sampai_tanggal.setObjectName("sampai_tanggal")
        self.sampai = self.sampai_tanggal.date().addDays(1).toString("yyyy-MM-dd")

        self.gridLayout.addWidget(self.sampai_tanggal, 2, 2, 1, 2)
        self.label_sampai = QtWidgets.QLabel(self.tab_transaksi)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_sampai.setFont(font)
        self.label_sampai.setObjectName("label_sampai")
        self.gridLayout.addWidget(self.label_sampai, 1, 2, 1, 1)
        self.tabWidget.addTab(self.tab_transaksi, "")
        self.tab_barang = QtWidgets.QWidget()
        self.tab_barang.setObjectName("tab_barang")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_barang)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.cariBtn_2 = QtWidgets.QPushButton(self.tab_barang)
        self.cariBtn_2.setMinimumSize(QtCore.QSize(0, 35))
        self.cariBtn_2.setMaximumSize(QtCore.QSize(120, 16777215))
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
        self.gridLayout_2.addWidget(self.cariBtn_2, 1, 4, 1, 1)
        self.tabel_produk = QtWidgets.QTableWidget(self.tab_barang)
        self.tabel_produk.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tabel_produk.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tabel_produk.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabel_produk.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tabel_produk.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tabel_produk.setObjectName("tabel_produk")
        self.tabel_produk.setColumnCount(6)
        self.tabel_produk.setRowCount(0)
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
        self.gridLayout_2.addWidget(self.tabel_produk, 2, 0, 1, 5)
        self.dari_tanggal_2 = QtWidgets.QDateEdit(self.tab_barang)
        self.dari_tanggal_2.setAlignment(QtCore.Qt.AlignCenter)
        self.dari_tanggal_2.setCalendarPopup(True)
        self.dari_tanggal_2.setObjectName("dari_tanggal_2")
        self.dari_tanggal_2.setDate(QtCore.QDate(current.year(), current.month(), 1))
        self.gridLayout_2.addWidget(self.dari_tanggal_2, 1, 0, 1, 2)
        self.sampai_tanggal_2 = QtWidgets.QDateEdit(self.tab_barang)
        self.sampai_tanggal_2.setAlignment(QtCore.Qt.AlignCenter)
        self.sampai_tanggal_2.setCalendarPopup(True)
        self.sampai_tanggal_2.setObjectName("sampai_tanggal_2")
        self.sampai_tanggal_2.setDate(current)
        self.gridLayout_2.addWidget(self.sampai_tanggal_2, 1, 2, 1, 2)
        self.label_dari_2 = QtWidgets.QLabel(self.tab_barang)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_dari_2.setFont(font)
        self.label_dari_2.setObjectName("label_dari_2")
        self.gridLayout_2.addWidget(self.label_dari_2, 0, 0, 1, 1)
        self.label_sampai_2 = QtWidgets.QLabel(self.tab_barang)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_sampai_2.setFont(font)
        self.label_sampai_2.setObjectName("label_sampai_2")
        self.gridLayout_2.addWidget(self.label_sampai_2, 0, 2, 1, 1)
        self.tabWidget.addTab(self.tab_barang, "")
        self.tab_penjualan = QtWidgets.QWidget()
        self.tab_penjualan.setObjectName("tab_penjualan")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_penjualan)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.cariBtn_3 = QtWidgets.QPushButton(self.tab_penjualan)
        self.cariBtn_3.setMinimumSize(QtCore.QSize(0, 35))
        self.cariBtn_3.setMaximumSize(QtCore.QSize(120, 16777215))
        self.cariBtn_3.setStyleSheet("QPushButton {\n"
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
        self.cariBtn_3.setObjectName("cariBtn_3")
        self.gridLayout_3.addWidget(self.cariBtn_3, 1, 4, 1, 1)
        self.tabel_penjualan = QtWidgets.QTableWidget(self.tab_penjualan)
        self.tabel_penjualan.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tabel_penjualan.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tabel_penjualan.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabel_penjualan.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tabel_penjualan.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tabel_penjualan.setObjectName("tabel_penjualan")
        self.tabel_penjualan.setColumnCount(7)
        self.tabel_penjualan.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_penjualan.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_penjualan.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_penjualan.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_penjualan.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_penjualan.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_penjualan.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_penjualan.setHorizontalHeaderItem(6, item)
        self.gridLayout_3.addWidget(self.tabel_penjualan, 2, 0, 1, 5)
        self.dari_tanggal_3 = QtWidgets.QDateEdit(self.tab_penjualan)
        self.dari_tanggal_3.setAlignment(QtCore.Qt.AlignCenter)
        self.dari_tanggal_3.setCalendarPopup(True)
        self.dari_tanggal_3.setObjectName("dari_tanggal_3")
        self.dari_tanggal_3.setDate(QtCore.QDate(current.year(), current.month(), 1))
        self.gridLayout_3.addWidget(self.dari_tanggal_3, 1, 0, 1, 2)
        self.sampai_tanggal_3 = QtWidgets.QDateEdit(self.tab_penjualan)
        self.sampai_tanggal_3.setAlignment(QtCore.Qt.AlignCenter)
        self.sampai_tanggal_3.setCalendarPopup(True)
        self.sampai_tanggal_3.setObjectName("sampai_tanggal_3")
        self.sampai_tanggal_3.setDate(current)
        self.gridLayout_3.addWidget(self.sampai_tanggal_3, 1, 2, 1, 2)
        self.label_dari_3 = QtWidgets.QLabel(self.tab_penjualan)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_dari_3.setFont(font)
        self.label_dari_3.setObjectName("label_dari_3")
        self.gridLayout_3.addWidget(self.label_dari_3, 0, 0, 1, 1)
        self.label_sampai_3 = QtWidgets.QLabel(self.tab_penjualan)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_sampai_3.setFont(font)
        self.label_sampai_3.setObjectName("label_sampai_3")
        self.gridLayout_3.addWidget(self.label_sampai_3, 0, 2, 1, 1)
        self.tabWidget.addTab(self.tab_penjualan, "")
        self.tab_pengeluaran = QtWidgets.QWidget()
        self.tab_pengeluaran.setObjectName("tab_pengeluaran")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_pengeluaran)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tabel_pengeluaran = QtWidgets.QTableWidget(self.tab_pengeluaran)
        self.tabel_pengeluaran.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tabel_pengeluaran.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tabel_pengeluaran.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabel_pengeluaran.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tabel_pengeluaran.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tabel_pengeluaran.setObjectName("tabel_pengeluaran")
        self.tabel_pengeluaran.setColumnCount(5)
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
        self.gridLayout_4.addWidget(self.tabel_pengeluaran, 2, 0, 1, 5)
        self.cariBtn_4 = QtWidgets.QPushButton(self.tab_pengeluaran)
        self.cariBtn_4.setMinimumSize(QtCore.QSize(0, 35))
        self.cariBtn_4.setMaximumSize(QtCore.QSize(120, 16777215))
        self.cariBtn_4.setStyleSheet("QPushButton {\n"
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
        self.cariBtn_4.setObjectName("cariBtn_4")
        self.gridLayout_4.addWidget(self.cariBtn_4, 1, 4, 1, 1)
        self.dari_tanggal_4 = QtWidgets.QDateEdit(self.tab_pengeluaran)
        self.dari_tanggal_4.setAlignment(QtCore.Qt.AlignCenter)
        self.dari_tanggal_4.setCalendarPopup(True)
        self.dari_tanggal_4.setObjectName("dari_tanggal_4")
        self.dari_tanggal_4.setDate(QtCore.QDate(current.year(), current.month(), 1))
        self.gridLayout_4.addWidget(self.dari_tanggal_4, 1, 0, 1, 2)
        self.sampai_tanggal_4 = QtWidgets.QDateEdit(self.tab_pengeluaran)
        self.sampai_tanggal_4.setAlignment(QtCore.Qt.AlignCenter)
        self.sampai_tanggal_4.setCalendarPopup(True)
        self.sampai_tanggal_4.setObjectName("sampai_tanggal_4")
        self.sampai_tanggal_4.setDate(current)
        self.gridLayout_4.addWidget(self.sampai_tanggal_4, 1, 2, 1, 2)
        self.label_sampai_4 = QtWidgets.QLabel(self.tab_pengeluaran)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_sampai_4.setFont(font)
        self.label_sampai_4.setObjectName("label_sampai_4")
        self.gridLayout_4.addWidget(self.label_sampai_4, 0, 2, 1, 1)
        self.label_dari_4 = QtWidgets.QLabel(self.tab_pengeluaran)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_dari_4.setFont(font)
        self.label_dari_4.setObjectName("label_dari_4")
        self.gridLayout_4.addWidget(self.label_dari_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_pengeluaran, "")
        self.tab_laporan = QtWidgets.QWidget()
        self.tab_laporan.setObjectName("tab_laporan")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_laporan)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.cariBtn_6 = QtWidgets.QPushButton(self.tab_laporan)
        self.cariBtn_6.setMinimumSize(QtCore.QSize(0, 35))
        self.cariBtn_6.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cariBtn_6.setFont(font)
        self.cariBtn_6.setStyleSheet("QPushButton {\n"
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
"}\n"
"")
        self.cariBtn_6.setObjectName("cariBtn_6")
        self.cariBtn_6.clicked.connect(self.print_laporan)
        self.gridLayout_6.addWidget(self.cariBtn_6, 8, 6, 1, 1)
        self.label_omzet = QtWidgets.QLabel(self.tab_laporan)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_omzet.setFont(font)
        self.label_omzet.setObjectName("label_omzet")
        self.gridLayout_6.addWidget(self.label_omzet, 3, 1, 1, 2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_laporan)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("padding:0 20px;")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_6.addWidget(self.lineEdit_2, 4, 3, 1, 4)
        self.label_omzet_3 = QtWidgets.QLabel(self.tab_laporan)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_omzet_3.setFont(font)
        self.label_omzet_3.setObjectName("label_omzet_3")
        self.gridLayout_6.addWidget(self.label_omzet_3, 5, 1, 1, 2)
        self.label_dari_5 = QtWidgets.QLabel(self.tab_laporan)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_dari_5.setFont(font)
        self.label_dari_5.setObjectName("label_dari_5")
        self.gridLayout_6.addWidget(self.label_dari_5, 1, 1, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_laporan)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("padding:0 20px;")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_6.addWidget(self.lineEdit_3, 5, 3, 1, 4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_laporan)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("padding:0 20px;")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_6.addWidget(self.lineEdit_5, 7, 3, 1, 4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_laporan)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("padding:0 20px;")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_6.addWidget(self.lineEdit_4, 6, 3, 1, 4)
        self.label_omzet_2 = QtWidgets.QLabel(self.tab_laporan)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_omzet_2.setFont(font)
        self.label_omzet_2.setObjectName("label_omzet_2")
        self.gridLayout_6.addWidget(self.label_omzet_2, 4, 1, 1, 2)
        self.label_omzet_4 = QtWidgets.QLabel(self.tab_laporan)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_omzet_4.setFont(font)
        self.label_omzet_4.setObjectName("label_omzet_4")
        self.gridLayout_6.addWidget(self.label_omzet_4, 6, 1, 1, 2)
        self.label_omzet_5 = QtWidgets.QLabel(self.tab_laporan)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_omzet_5.setFont(font)
        self.label_omzet_5.setObjectName("label_omzet_5")
        self.gridLayout_6.addWidget(self.label_omzet_5, 7, 1, 1, 2)
        self.lineEdit = QtWidgets.QLineEdit(self.tab_laporan)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("padding:0 20px;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_6.addWidget(self.lineEdit, 3, 3, 1, 4)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem, 9, 5, 1, 1)
        self.dari_tanggal_5 = QtWidgets.QDateEdit(self.tab_laporan)
        self.dari_tanggal_5.setAlignment(QtCore.Qt.AlignCenter)
        self.dari_tanggal_5.setCalendarPopup(True)
        self.dari_tanggal_5.setObjectName("dari_tanggal_5")
        self.dari_tanggal_5.setDate(QtCore.QDate(current.year(), current.month(), 1))
        self.gridLayout_6.addWidget(self.dari_tanggal_5, 2, 1, 1, 2)
        self.sampai_tanggal_5 = QtWidgets.QDateEdit(self.tab_laporan)
        self.sampai_tanggal_5.setAlignment(QtCore.Qt.AlignCenter)
        self.sampai_tanggal_5.setCalendarPopup(True)
        self.sampai_tanggal_5.setObjectName("sampai_tanggal_5")
        self.sampai_tanggal_5.setDate(current)
        self.gridLayout_6.addWidget(self.sampai_tanggal_5, 2, 3, 1, 2)
        self.label_sampai_5 = QtWidgets.QLabel(self.tab_laporan)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_sampai_5.setFont(font)
        self.label_sampai_5.setObjectName("label_sampai_5")
        self.gridLayout_6.addWidget(self.label_sampai_5, 1, 3, 1, 1)
        self.cariBtn_5 = QtWidgets.QPushButton(self.tab_laporan)
        self.cariBtn_5.setMinimumSize(QtCore.QSize(0, 35))
        self.cariBtn_5.setMaximumSize(QtCore.QSize(120, 16777215))
        self.cariBtn_5.setStyleSheet("QPushButton {\n"
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
        self.cariBtn_5.setObjectName("cariBtn_5")
        self.gridLayout_6.addWidget(self.cariBtn_5, 2, 5, 1, 1)
        self.tabWidget.addTab(self.tab_laporan, "")
        self.tabWidget.currentChanged.connect(self.tabChanged)
        self.horizontalLayout_3.addWidget(self.tabWidget)
        self.dari_tanggal.dateChanged.connect(self.ubah_dari)
        self.dari_tanggal_2.dateChanged.connect(self.ubah_dari)
        self.dari_tanggal_3.dateChanged.connect(self.ubah_dari)
        self.dari_tanggal_4.dateChanged.connect(self.ubah_dari)
        self.dari_tanggal_5.dateChanged.connect(self.ubah_dari)
        
        self.sampai_tanggal.dateChanged.connect(self.ubah_sampai)
        self.sampai_tanggal_2.dateChanged.connect(self.ubah_sampai)
        self.sampai_tanggal_3.dateChanged.connect(self.ubah_sampai)
        self.sampai_tanggal_4.dateChanged.connect(self.ubah_sampai)
        self.sampai_tanggal_5.dateChanged.connect(self.ubah_sampai)

        header = self.tabel_transaksi.horizontalHeader()
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

        header = self.tabel_produk.horizontalHeader()
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

        header = self.tabel_penjualan.horizontalHeader()
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

        header = self.tabel_pengeluaran.horizontalHeader()
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

        self.getTransaksi()
        self.getBarang()
        self.getPenjualan()
        self.getPengeluaran()
        self.getLaporan()

        self.retranslateUi(parent)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(parent)
        self.close()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tabel_transaksi.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID Transaksi"))
        item = self.tabel_transaksi.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nama"))
        item = self.tabel_transaksi.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Total"))
        item = self.tabel_transaksi.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Tanggal"))
        self.label_dari.setText(_translate("Form", "Dari:"))
        self.cariBtn.setText(_translate("Form", "Cari"))
        self.dari_tanggal.setDisplayFormat(_translate("Form", "dd/MM/yyyy"))
        self.sampai_tanggal.setDisplayFormat(_translate("Form", "dd/MM/yyyy"))
        self.label_sampai.setText(_translate("Form", "Sampai:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_transaksi), _translate("Form", "Daftar Transaksi"))
        self.cariBtn_2.setText(_translate("Form", "Cari"))
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
        self.dari_tanggal_2.setDisplayFormat(_translate("Form", "dd/MM/yyyy"))
        self.sampai_tanggal_2.setDisplayFormat(_translate("Form", "dd/MM/yyyy"))
        self.label_dari_2.setText(_translate("Form", "Dari:"))
        self.label_sampai_2.setText(_translate("Form", "Sampai:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_barang), _translate("Form", "Daftar Barang Keluar"))
        self.cariBtn_3.setText(_translate("Form", "Cari"))
        item = self.tabel_penjualan.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID Produk"))
        item = self.tabel_penjualan.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nama Produk"))
        item = self.tabel_penjualan.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Kategori"))
        item = self.tabel_penjualan.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Jumlah Penjualan"))
        item = self.tabel_penjualan.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Omzet"))
        item = self.tabel_penjualan.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Modal"))
        item = self.tabel_penjualan.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Profit"))
        self.dari_tanggal_3.setDisplayFormat(_translate("Form", "dd/MM/yyyy"))
        self.sampai_tanggal_3.setDisplayFormat(_translate("Form", "dd/MM/yyyy"))
        self.label_dari_3.setText(_translate("Form", "Dari:"))
        self.label_sampai_3.setText(_translate("Form", "Sampai:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_penjualan), _translate("Form", "Rekap Penjualan"))
        item = self.tabel_pengeluaran.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Nama Item"))
        item = self.tabel_pengeluaran.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nominal"))
        item = self.tabel_pengeluaran.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Qty"))
        item = self.tabel_pengeluaran.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Total"))
        item = self.tabel_pengeluaran.horizontalHeaderItem(4)
        item.setText(_translate("Form", "No Struk"))
        self.cariBtn_4.setText(_translate("Form", "Cari"))
        self.dari_tanggal_4.setDisplayFormat(_translate("Form", "dd/MM/yyyy"))
        self.sampai_tanggal_4.setDisplayFormat(_translate("Form", "dd/MM/yyyy"))
        self.label_sampai_4.setText(_translate("Form", "Sampai:"))
        self.label_dari_4.setText(_translate("Form", "Dari:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_pengeluaran), _translate("Form", "Pengeluaran"))
        self.cariBtn_6.setText(_translate("Form", "Cetak laporan"))
        self.label_omzet.setText(_translate("Form", "Omzet"))
        self.label_omzet_3.setText(_translate("Form", "Profit"))
        self.label_dari_5.setText(_translate("Form", "Dari:"))
        self.label_omzet_2.setText(_translate("Form", "HPP"))
        self.label_omzet_4.setText(_translate("Form", "Pengeluaran"))
        self.label_omzet_5.setText(_translate("Form", "Net Profit"))
        self.dari_tanggal_5.setDisplayFormat(_translate("Form", "dd/MM/yyyy"))
        self.sampai_tanggal_5.setDisplayFormat(_translate("Form", "dd/MM/yyyy"))
        self.label_sampai_5.setText(_translate("Form", "Sampai:"))
        self.cariBtn_5.setText(_translate("Form", "Cari"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_laporan), _translate("Form", "Laporan Penjualan"))

    def ubah_dari(self):
        self.dari = self.dari_tanggal.date().toString("yyyy-MM-dd")
        self.getTransaksi()
        self.getBarang()
        self.getPenjualan()
        self.getPengeluaran
        self.getLaporan()
    
    def ubah_sampai(self):
        self.sampai = self.sampai_tanggal.date()
        self.sampai = self.sampai_tanggal.date().addDays(1).toString("yyyy-MM-dd")
        self.getTransaksi()
        self.getBarang()
        self.getPenjualan()
        self.getPengeluaran()
        self.getLaporan()

    def tabChanged(self):
        self.getTransaksi()
        self.getBarang()
        self.getPenjualan()
        self.getPengeluaran()
        self.getLaporan()

    def show(self):
        self.rekapTransaksiWidget.show()

    def close(self):
        self.rekapTransaksiWidget.close()

    def getTransaksi(self):
        key = "waktu >= \"{}\" AND waktu < \"{}\""
        key = key.format(self.dari, self.sampai)
        rekap_transaksi = self.parent.mysql.findCol("idTransaksi, pelanggan, total, waktu", "transaksi",key, True,"waktu DESC")
        self.data_Transaksi = []
        self.banyak_data_transaksi = len(rekap_transaksi)
        if rekap_transaksi is None:
            return
        banyak_data = len(rekap_transaksi)

        #add data to new array and count it
        done = []
        skip = 0
        flag = False
        row = 0
        for data in rekap_transaksi:
            col = 0
            jumlah = 0
            count = 0
            data_done = len(done)
            if data_done > 0:
                for val in range(data_done):
                    if rekap_transaksi[row][0] == done[val][0]:
                        flag = True
                        skip += 1
                        break
            if flag is False:
                self.data_Transaksi.append([])
            for val in data:
                if flag is True:
                    flag = False
                    break
                if count == 0:
                    for i in range(banyak_data):
                        if rekap_transaksi[row][0] == rekap_transaksi[i][0]: 
                            jumlah += int(rekap_transaksi[i][2])
                    count = 1
                val = str(val)
                if col is 2:
                    val = "Rp " + str(jumlah)
                self.data_Transaksi[row-skip].append(val)
                if col is 3:
                    done.append([])
                    done[row-skip].append(rekap_transaksi[row][0])
                col += 1
            row += 1 
        
        #add to tabel
        self.tabel_transaksi.setRowCount(len(self.data_Transaksi))
        row = 0
        for data in self.data_Transaksi:
            col = 0
            for val in data:
                val = str(val)
                #print(val)
                self.tabel_transaksi.setItem(row,col,QtWidgets.QTableWidgetItem(val))
                col += 1
            row += 1
        #print(self.data_Transaksi)

    def getBarang(self):
        self.sampai = self.sampai_tanggal_2.date().addDays(1).toString("yyyy-MM-dd")
        self.dari = self.dari_tanggal_2.date().toString("yyyy-MM-dd")

        key = "waktu >= \"{}\" AND waktu < \"{}\""
        key = key.format(self.dari, self.sampai)
        data_transaksi = self.parent.mysql.findCol("id, idTransaksi, produk, harga, jumlah, total, idProduk", "transaksi",key,True,"waktu DESC")
        #print(key)
        if data_transaksi is None:
            return
        self.banyak_dataBarangKeluar = len(data_transaksi)
        #print(banyak)
        diskon = []
        for i in range(self.banyak_dataBarangKeluar):
            key = "idProduk = \"{}\""
            key = key.format(data_transaksi[i][6])
            produk = self.parent.mysql.findCol("diskon", "daftarbarang", key, True)
            len1 = len(produk)
            #print(len1)
            if len1 is 0:
                produk = [(0,)] 
            diskon += produk
        #print(diskon)
        self.data_barangKeluar = []
        if data_transaksi is None :
            return
        self.tabel_produk.setRowCount(len(data_transaksi))
        row = 0
        for data in data_transaksi:
            self.data_barangKeluar.append([])
            col = 0
            for val in data:
                val = str(val)
                if col is 3 or col is 5:
                    val = "Rp " + val
                if col  is 5:
                    val_add = val
                    val = diskon[row][0]
                    val = str(val) + "%"
                    #print(val)
                    #self.tabel_produk.setItem(row,col,QtWidgets.QTableWidgetItem(val_add))
                if col is 6:
                    val = val_add
                self.tabel_produk.setItem(row,col,QtWidgets.QTableWidgetItem(val))
                self.data_barangKeluar[row].append(val)
                col += 1
            row += 1

    def getPenjualan(self):
        self.sampai = self.sampai_tanggal_3.date().addDays(1).toString("yyyy-MM-dd")
        self.dari = self.dari_tanggal_3.date().toString("yyyy-MM-dd")
        if self.tabWidget.currentIndex() == 4:
            self.sampai = self.sampai_tanggal_5.date().addDays(1).toString("yyyy-MM-dd")
            self.dari = self.dari_tanggal_5.date().toString("yyyy-MM-dd")

        key = "waktu >= \"{}\" AND waktu < \"{}\""
        key = key.format(self.dari, self.sampai)
        data_transaksi = self.parent.mysql.findCol("idProduk, produk, jumlah, total","transaksi",key,True,"waktu DESC")
        len1 = len(data_transaksi)
        total_data_daftarBarang = []
        for i in range(len1):
            key = "idProduk = \"{}\""
            key = key.format(data_transaksi[i][0])
            data_daftarBarang = self.parent.mysql.findCol("kategori,hpp", "daftarbarang", key ,True)
            len1 = len(data_daftarBarang)
            if len1 is 0:
                data_daftarBarang = [('None',0)] 
            total_data_daftarBarang += data_daftarBarang
 
        #add data to new array and count it
        self.banyak_data_pengeluaran = len(data_transaksi)
        self.omzet = self.hpp = self.profit=0
        self.data_penjualan = []
        done = []
        skip = 0
        flag = False
        row = 0
        for data in data_transaksi:
            col = 0
            data1 = 0
            jumlah = 0
            total = 0
            count = 0
            hpp = 0
            data_done = len(done)
            if data_done > 0:
                for val in range(data_done):
                    if data_transaksi[row][0] == done[val][0]:
                        flag = True
                        skip += 1
                        break
            if flag is False:
                self.data_penjualan.append([])
            for val in data:
                #kalau ada yang sama langsung loncat
                if flag is True:
                    flag = False
                    break
                if count == 0:
                    for i in range(self.banyak_data_pengeluaran):
                        if data_transaksi[row][0] == data_transaksi[i][0]: 
                            jumlah += int(data_transaksi[i][2])
                            total  += int(data_transaksi[i][3])
                            hpp += total_data_daftarBarang[i][1]
                    count = 1
                val = str(val)
                if col is 0:
                    self.data_penjualan[row-skip].append(val)
                if col is 1:
                    self.data_penjualan[row-skip].append(val)
                if col is 2:
                    cols = 3
                    vals = jumlah
                    val = str(total_data_daftarBarang[row][0])
                    self.data_penjualan[row-skip].append(val)
                    data1 = int(vals)
                    self.data_penjualan[row-skip].append(vals)
                if col is 3:
                    col += 1
                    omzet = int(total)
                    self.omzet += omzet
                    val = "Rp "+ str(total)
                    self.data_penjualan[row-skip].append(val)
                    cols = 5
                    hpp = data1 * hpp
                    vals = "Rp "+ str(hpp)
                    data5 = vals 
                    self.hpp += hpp
                
                    self.data_penjualan[row-skip].append(vals)
                    cols = 6
                    profit =  omzet - hpp
                    vals = "Rp "+ str(profit)
                    self.profit += profit
                    self.data_penjualan[row-skip].append(vals)

                    done.append([])
                    done[row-skip].append(data_transaksi[row][0])
                
                col +=1
            row +=1
        #add to table
        self.tabel_penjualan.setRowCount(len(self.data_penjualan))
        row =0
        for data in self.data_penjualan:
            col = 0
            for val in data:
                val = str(val)
                self.tabel_penjualan.setItem(row,col,QtWidgets.QTableWidgetItem(val))
                col += 1
            row += 1

    def getPengeluaran(self):
        self.sampai = self.sampai_tanggal_4.date().addDays(1).toString("yyyy-MM-dd")
        self.dari = self.dari_tanggal_4.date().toString("yyyy-MM-dd")
        key = "waktu >= \"{}\" AND waktu < \"{}\""
        key = key.format(self.dari, self.sampai)
        q = self.parent.mysql.findCol("nama, harga, jumlah, total, struk", "pengeluaran", key, True, "waktu DESC")
        self.q = q
        if q is None:
            return
        self.tabel_pengeluaran.setRowCount(len(q))
        total_pengeluaran=0
        self.banyak_dataPengeluaran = len(q)
        #print(self.banyak_dataPengeluaran)
        self.data_Pengeluaran = []
        row = 0
        for r in q:
            self.data_Pengeluaran.append([])
            col = 0
            for data in r:
                if col is 3:
                    total_pengeluaran += data
                data = str(data)
                self.tabel_pengeluaran.setItem(
                    row, col, QtWidgets.QTableWidgetItem(data))
                self.data_Pengeluaran[row].append(data)
                col += 1
            row += 1
        #print(q)
        self.total_pengeluaran = total_pengeluaran
        #print(self.total_pengeluaran)

    def getLaporan(self):
        self.getPenjualan()
        self.sampai = self.sampai_tanggal_5.date().addDays(1).toString("yyyy-MM-dd")
        self.dari = self.dari_tanggal_5.date().toString("yyyy-MM-dd")
        self.lineEdit.setText("Rp "+str(self.omzet))
        self.lineEdit_2.setText("Rp "+str(self.hpp))
        self.lineEdit_3.setText("Rp "+str(self.profit))
        self.lineEdit_4.setText("Rp "+str(self.total_pengeluaran))
        net_profit = self.profit - self.total_pengeluaran
        self.lineEdit_5.setText("Rp "+str(net_profit))

        self.data_laporanPenjualan =[]
        self.data_laporanPenjualan.append("Rp "+str(self.omzet))
        self.data_laporanPenjualan.append("Rp "+str(self.hpp))
        self.data_laporanPenjualan.append("Rp "+str(self.profit))
        self.data_laporanPenjualan.append("Rp "+str(self.total_pengeluaran))
        self.data_laporanPenjualan.append("Rp "+str(net_profit))
        self.judul_laporanPenjualan =[]
        self.judul_laporanPenjualan.append("Omzet : ")
        self.judul_laporanPenjualan.append("HPP : ")
        self.judul_laporanPenjualan.append("Profit : ")
        self.judul_laporanPenjualan.append("Pengeluaran : ")
        self.judul_laporanPenjualan.append("Net Profit : ")
        #print(self.data_laporanPenjualan)

    def print_laporan(self):
        path = QtCore.QDir.currentPath()
        path = path + '/Data Laporan'
        nama_file = 'Rekap_Laporan_'+str(self.dari)+' sampai '+str(self.sampai)+".xlsx"
        nama_file = path + '/' + nama_file
        
        workbook = xlsxwriter.Workbook(nama_file)

        #merge format khusus laporan penjualan
        merge_format_laporan = workbook.add_format({
            'bold': 1,
            'border': 1,
            'color': 'white',
            'align': 'center',
            'valign': 'vcenter',
            'fg_color': 'black'
            })

        #LaporanPenjualan

        judul_LaporanPenjualan = "Laporan Penjualan"

        LaporanPenjualan = workbook.add_worksheet('Laporan_Penjualan')
        LaporanPenjualan.set_column('A:A',20)
        LaporanPenjualan.set_column('B:B',10)
        LaporanPenjualan.merge_range('A1:B1',judul_LaporanPenjualan,merge_format_laporan)
        LaporanPenjualan.add_table('A2:B6',{'header_row': 0,'style': 'Table Style Medium 8'})
        LaporanPenjualan.write_column('B2',self.data_laporanPenjualan)
        LaporanPenjualan.write_column('A2',self.judul_laporanPenjualan)

        #merge format untuk umum
        merge_format = workbook.add_format({
            'bold': 1,
            'border': 1,
            #'color': 'white',
            'align': 'center',
            'valign': 'vcenter',
            #'fg_color': 'black'
            })


        #DaftarTransaksi
        judul_DaftarTransaksi = "Daftar Transaksi"
        DaftarTransaksi = workbook.add_worksheet('Daftar_transaksi')
        setCol_transaksi = 'A2:D'+str(self.banyak_data_transaksi+2)
        DaftarTransaksi.set_column('A:D',20)
        DaftarTransaksi.merge_range('A1:D1',judul_DaftarTransaksi,merge_format)
        DaftarTransaksi.add_table(setCol_transaksi,{'data':self.data_Transaksi,'style': 'Table Style Medium 8','columns': [{'header': 'ID Transaksi'},
                                           {'header': 'Nama Pelanggan'},
                                           {'header': 'Total'},
                                           {'header': 'Tanggal'}]})
        #DaftarBarangKeluar
        judul_DaftarBarangKeluar = "Daftar Barang Keluar"
        DaftarBarangKeluar = workbook.add_worksheet('Daftar_Barang_Keluar')
        setCol_BarangKeluar = 'A2:G'+str(self.banyak_dataBarangKeluar+2)
        DaftarBarangKeluar.set_column('A:G',20)
        DaftarBarangKeluar.merge_range('A1:G1',judul_DaftarBarangKeluar,merge_format)
        DaftarBarangKeluar.add_table(setCol_BarangKeluar,{'data':self.data_barangKeluar,'style': 'Table Style Medium 8','columns': [{'header': 'ID Barang Keluar'},
                                           {'header': 'ID Transaksi'},
                                           {'header': 'Nama Produk'},
                                           {'header': 'Harga Per satuan'},
                                           {'header': 'QTY'},
                                           {'header': 'Diskon'},
                                           {'header': 'Harga Total'}]})
        #DaftarPenjualan
        judul_DaftarPenjualan = "Daftar Penjualan"
        RekapPenjualan = workbook.add_worksheet('Rekap_Penjualan')
        setCol_penjualan = 'A2:G'+str(self.banyak_dataPengeluaran+2)
        RekapPenjualan.set_column('A:G',20)
        RekapPenjualan.merge_range('A1:G1',judul_DaftarPenjualan,merge_format)
        RekapPenjualan.add_table(setCol_penjualan,{'data':self.data_penjualan,'style': 'Table Style Medium 8','columns': [{'header': 'ID Produk'},
                                           {'header': 'Nama Produk'},
                                           {'header': 'Kategori'},
                                           {'header': 'Jumlah Penjualan'},
                                           {'header': 'Omzet'},
                                           {'header': 'Modal'},
                                           {'header': 'Profit'}]})
        #DaftarPengeluaran
        judul_DaftarPengeluaran = "Daftar Pengeluaran"
        Pengeluaran = workbook.add_worksheet('Pengeluaran')
        setCol_Pengeluaran = 'A2:E'+str(self.banyak_dataPengeluaran+2)
        Pengeluaran.set_column('A:E',20)
        Pengeluaran.merge_range('A1:E1',judul_DaftarPengeluaran,merge_format)
        Pengeluaran.add_table(setCol_Pengeluaran,{'data':self.data_Pengeluaran,'style': 'Table Style Medium 8','columns': [{'header': 'Nama Item'},
                                           {'header': 'Nominal'},
                                           {'header': 'QTY'},
                                           {'header': 'Total'},
                                           {'header': 'No Struk'}]})

        workbook.close()
        copyfile(nama_file, "Laporan.xlsx")
        sys.path[0]
        os.chdir(sys.path[0])
        os.system('start excel.exe "%s\\Laporan.xlsx"' % (sys.path[0], ))