from PyQt5 import QtCore, QtGui, QtWidgets
from Module.topup_new import *
from Module.sql import *
from Module.login import *
from Module.ui_main_window import *
from datetime import datetime
from barcode.writer import ImageWriter

n = 0

class Pelanggan():
    def __init__(self, parent):
        self.parent = parent
        self.pelanggan = parent.mysql

        self.pelangganWidget = QtWidgets.QWidget(parent)
        self.pelangganWidget.setMinimumSize(QtCore.QSize(350, 0))
        self.pelangganWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pelangganWidget.setStyleSheet("")
        self.pelangganWidget.setObjectName("pelangganWidget")

        self.ui_main_window = Ui_Form(parent)
        self.topup_new = Topup(parent)

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.pelangganWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_4 = QtWidgets.QWidget(self.pelangganWidget)
        self.widget_4.setStyleSheet("")
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget_7 = QtWidgets.QWidget(self.widget_4)
        self.widget_7.setMaximumSize(QtCore.QSize(16777215, 87))
        self.widget_7.setObjectName("widget_7")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_7)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.labelsaldo = QtWidgets.QLabel(self.widget_7)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelsaldo.setFont(font)
        self.labelsaldo.setStyleSheet("color: #00c853;")
        self.labelsaldo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelsaldo.setObjectName("labelsaldo")
        self.gridLayout_4.addWidget(self.labelsaldo, 0, 2, 1, 1)
        self.saldo = QtWidgets.QLineEdit(self.widget_7)
        self.saldo.setMaximumSize(QtCore.QSize(250, 16777215))
        self.saldo.setStyleSheet("background-color: #00c853;\n"
"border: 2px solid #00c853;\n"
"color:white;\n"
"padding: 0 3px;\n"
"font-size: 18pt;")
        self.saldo.setAlignment(QtCore.Qt.AlignCenter)
        self.saldo.setReadOnly(True)
        self.saldo.setObjectName("saldo")
        self.gridLayout_4.addWidget(self.saldo, 1, 2, 1, 1)
        self.labelpoint = QtWidgets.QLabel(self.widget_7)
        self.labelpoint.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelpoint.setFont(font)
        self.labelpoint.setStyleSheet("    color: #ff8f00;")
        self.labelpoint.setAlignment(QtCore.Qt.AlignCenter)
        self.labelpoint.setObjectName("labelpoint")
        self.gridLayout_4.addWidget(self.labelpoint, 0, 1, 1, 1)
        self.point = QtWidgets.QLineEdit(self.widget_7)
        self.point.setMaximumSize(QtCore.QSize(200, 16777215))
        self.point.setStyleSheet("background-color: #ff8f00;\n"
"border: 2px solid #ff8f00;\n"
"color:white;\n"
"font-size: 18pt;")
        self.point.setAlignment(QtCore.Qt.AlignCenter)
        self.point.setReadOnly(True)
        self.point.setObjectName("point")
        self.gridLayout_4.addWidget(self.point, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.widget_7, 8, 1, 1, 1)
        self.alamat = QtWidgets.QLineEdit(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.alamat.setFont(font)
        self.alamat.setClearButtonEnabled(True)
        self.alamat.setObjectName("alamat")
        self.gridLayout_2.addWidget(self.alamat, 6, 1, 1, 1)
        self.labelnama = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelnama.setFont(font)
        self.labelnama.setObjectName("labelnama")
        self.gridLayout_2.addWidget(self.labelnama, 3, 0, 1, 1)
        self.rfid = QtWidgets.QLineEdit(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rfid.setFont(font)
        self.rfid.setObjectName("rfid")
        self.rfid.setPlaceholderText("Tempelkan kartu pada scanner")
        self.rfid.setMaxLength(10)

        self.gridLayout_2.addWidget(self.rfid, 2, 1, 1, 1)
        self.labelid = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelid.setFont(font)
        self.labelid.setObjectName("labelid")
        self.gridLayout_2.addWidget(self.labelid, 1, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.widget_4)
        self.widget.setMaximumSize(QtCore.QSize(270, 35))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton.setFont(font)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.gender = self.radioButton
        self.radioButton.clicked.connect(self.maleGender)
        self.horizontalLayout_2.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.clicked.connect(self.femaleGender)
        self.horizontalLayout_2.addWidget(self.radioButton_2)
        self.gridLayout_2.addWidget(self.widget, 4, 1, 1, 1)
        self.labelhp = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelhp.setFont(font)
        self.labelhp.setObjectName("labelhp")
        self.gridLayout_2.addWidget(self.labelhp, 7, 0, 1, 1)
        self.ID = QtWidgets.QLineEdit(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ID.setFont(font)
        self.ID.setPlaceholderText("")
        self.ID.setClearButtonEnabled(True)
        self.ID.setObjectName("ID")
        self.gridLayout_2.addWidget(self.ID, 1, 1, 1, 1)
        self.hp = QtWidgets.QLineEdit(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.hp.setFont(font)
        self.hp.setClearButtonEnabled(True)
        self.hp.setObjectName("hp")
        self.gridLayout_2.addWidget(self.hp, 7, 1, 1, 1)
        self.nama = QtWidgets.QLineEdit(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nama.setFont(font)
        self.nama.setClearButtonEnabled(True)
        self.nama.setObjectName("nama")
        self.gridLayout_2.addWidget(self.nama, 3, 1, 1, 1)
        self.labelgender = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelgender.setFont(font)
        self.labelgender.setObjectName("labelgender")
        self.gridLayout_2.addWidget(self.labelgender, 4, 0, 1, 1)
        self.labelrfid = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelrfid.setFont(font)
        self.labelrfid.setObjectName("labelrfid")
        self.gridLayout_2.addWidget(self.labelrfid, 2, 0, 1, 1)
        self.labelAlamat = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelAlamat.setFont(font)
        self.labelAlamat.setObjectName("labelAlamat")
        self.gridLayout_2.addWidget(self.labelAlamat, 6, 0, 1, 1)
        self.Khusus = QtWidgets.QLabel(self.widget_4)
        self.Khusus.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(12)
        font.setWeight(75)
        self.Khusus.setFont(font)
        self.Khusus.setStyleSheet("color: red;")
        self.Khusus.setAlignment(QtCore.Qt.AlignCenter)
        self.Khusus.setObjectName("Khusus")
        self.Khusus.hide()
        self.gridLayout_2.addWidget(self.Khusus, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.widget_4)
        self.line_3.setStyleSheet("")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_3.addWidget(self.line_3, 3, 0, 1, 2)
        self.widget_6 = QtWidgets.QWidget(self.widget_4)
        self.widget_6.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_6.setStyleSheet("")
        self.widget_6.setObjectName("widget_6")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_6)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 37, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem1, 4, 2, 1, 1)
        self.label_jenis = QtWidgets.QLabel(self.widget_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_jenis.setFont(font)
        self.label_jenis.setObjectName("label_jenis")
        self.gridLayout.addWidget(self.label_jenis, 5, 0, 1, 1)        
        self.comboBox = QtWidgets.QComboBox(self.widget_6)
        self.comboBox.setMinimumSize(QtCore.QSize(115, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.currentTextChanged.connect(self.change)
        self.gridLayout.addWidget(self.comboBox, 5, 1, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 3, 1, 1)
        self.img = QtWidgets.QLabel(self.widget_6)
        self.img.setMinimumSize(QtCore.QSize(180, 230))
        self.img.setAlignment(QtCore.Qt.AlignCenter)
        self.img.setObjectName("img")
        self.pixmap = QtGui.QPixmap("placeholder.jpg")
        self.img.setPixmap(self.pixmap.scaled(200, 170, QtCore.Qt.KeepAspectRatio))
        self.gridLayout.addWidget(self.img, 1, 0, 1, 3)
        self.foto = QtWidgets.QPushButton(self.widget_6)
        self.foto.setMinimumSize(QtCore.QSize(0, 35))
        self.foto.setStyleSheet("QPushButton {\n"
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
        self.foto.setObjectName("foto")
        self.foto.clicked.connect(self.takephoto)

        self.gridLayout.addWidget(self.foto, 2, 0, 1, 3)
        self.data = QtWidgets.QLabel(self.widget_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.data.setFont(font)
        self.data.setStyleSheet("")
        self.data.setAlignment(QtCore.Qt.AlignCenter)
        self.data.setObjectName("data")
        self.gridLayout.addWidget(self.data, 0, 0, 1, 3)
        self.gridLayout_3.addWidget(self.widget_6, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cari = QtWidgets.QLineEdit(self.widget_4)
        self.cari.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cari.setFont(font)
        self.cari.setStyleSheet("border-radius: 10px;\n"
"padding-left: 10px;")
        self.cari.setAlignment(QtCore.Qt.AlignCenter)
        self.cari.setObjectName("cari")
        self.horizontalLayout_3.addWidget(self.cari)
        self.cariBtn_2 = QtWidgets.QPushButton(self.widget_4)
        self.cariBtn_2.setMinimumSize(QtCore.QSize(120, 35))
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
        self.cariBtn_2.clicked.connect(self.findProduct)

        self.horizontalLayout_3.addWidget(self.cariBtn_2)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 1, 0, 1, 2)
        self.verticalLayout_3.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.pelangganWidget)
        self.widget_5.setStyleSheet("")
        self.widget_5.setObjectName("widget_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.widget_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.hapus = QtWidgets.QPushButton(self.widget_5)
        self.hapus.setMinimumSize(QtCore.QSize(120, 35))
        self.hapus.setStyleSheet("QPushButton {\n"
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
        self.hapus.setObjectName("hapus")
        self.hapus.clicked.connect(self.deleteProduct)

        self.gridLayout_6.addWidget(self.hapus, 3, 1, 1, 1)
        self.simpan = QtWidgets.QPushButton(self.widget_5)
        self.simpan.setMinimumSize(QtCore.QSize(120, 35))
        self.simpan.setStyleSheet("QPushButton {\n"
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
        self.simpan.setObjectName("simpan")
        self.simpan.clicked.connect(self.flag)

        self.gridLayout_6.addWidget(self.simpan, 3, 0, 1, 1)
        self.Topup = QtWidgets.QPushButton(self.widget_5)
        self.Topup.setMinimumSize(QtCore.QSize(160, 35))
        self.Topup.setStyleSheet("QPushButton {\n"
"    background: #00c853;\n"
"    border-radius: 6px;\n"
"    border: none;\n"
"    color: white;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 2px solid #00c853;\n"
"    background: white;\n"
"    color: #00c853;\n"
"}")
        self.Topup.setObjectName("Topup")
        self.Topup.clicked.connect(self.Topupedit)

        self.gridLayout_6.addWidget(self.Topup, 3, 3, 1, 1)
        self.tabelPelanggan = QtWidgets.QTableWidget(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabelPelanggan.sizePolicy().hasHeightForWidth())
        self.tabelPelanggan.setSizePolicy(sizePolicy)
        self.tabelPelanggan.verticalHeader().setDefaultSectionSize(38)
        self.tabelPelanggan.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tabelPelanggan.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tabelPelanggan.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabelPelanggan.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tabelPelanggan.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tabelPelanggan.setObjectName("tabelPelanggan")
        self.tabelPelanggan.setColumnCount(11)
        self.tabelPelanggan.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabelPelanggan.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelPelanggan.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelPelanggan.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelPelanggan.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelPelanggan.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelPelanggan.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelPelanggan.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelPelanggan.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelPelanggan.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelPelanggan.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelPelanggan.setHorizontalHeaderItem(10, item)
        self.tabelPelanggan.horizontalHeader().setCascadingSectionResizes(True)
        self.tabelPelanggan.itemClicked.connect(self.selectProduct)
        self.getProduct()

        self.gridLayout_6.addWidget(self.tabelPelanggan, 0, 0, 1, 4)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem4, 3, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_6.addItem(spacerItem5, 4, 2, 1, 1)
        self.verticalLayout_3.addWidget(self.widget_5)

        self.retranslateUi(parent)
        QtCore.QMetaObject.connectSlotsByName(parent)
        self.close()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.labelsaldo.setText(_translate("Form", "Saldo"))
        self.labelpoint.setText(_translate("Form", "Point"))
        self.labelnama.setText(_translate("Form", "Nama"))
        self.labelid.setText(_translate("Form", "ID"))
        self.radioButton.setText(_translate("Form", "Laki-laki"))
        self.radioButton_2.setText(_translate("Form", "Perempuan"))
        self.labelhp.setText(_translate("Form", "No. HP"))
        self.labelgender.setText(_translate("Form", "Gender"))
        self.label_jenis.setText(_translate("Form", "Jenis Pelanggan"))
        self.labelrfid.setText(_translate("Form", "RFID"))
        self.labelAlamat.setText(_translate("Form", "Alamat"))
        self.Khusus.setText(_translate("Form", "ANDA MENAMBAHKAN PELANGGAN KHUSUS"))
        self.comboBox.setItemText(0, _translate("Form", "Regular"))
        self.comboBox.setItemText(1, _translate("Form", "Khusus"))
        self.img.setText(_translate("Form", "Image"))
        self.foto.setText(_translate("Form", "CAPTURE"))
        self.data.setText(_translate("Form", "FOTO PELANGGAN"))
        self.cari.setPlaceholderText(_translate("Form", "Masukkan id pelanggan/scan kartu"))
        self.cariBtn_2.setText(_translate("Form", "Cari"))
        self.hapus.setText(_translate("Form", "Hapus"))
        self.simpan.setText(_translate("Form", "Simpan"))
        self.Topup.setText(_translate("Form", "Top Up"))
        item = self.tabelPelanggan.horizontalHeaderItem(0)
        item.setText(_translate("Form", "id"))
        item = self.tabelPelanggan.horizontalHeaderItem(1)
        item.setText(_translate("Form", "idPelanggan"))
        item = self.tabelPelanggan.horizontalHeaderItem(2)
        item.setText(_translate("Form", "nama"))
        item = self.tabelPelanggan.horizontalHeaderItem(3)
        item.setText(_translate("Form", "gender"))
        item = self.tabelPelanggan.horizontalHeaderItem(4)
        item.setText(_translate("Form", "member"))
        item = self.tabelPelanggan.horizontalHeaderItem(5)
        item.setText(_translate("Form", "alamat"))
        item = self.tabelPelanggan.horizontalHeaderItem(6)
        item.setText(_translate("Form", "kontak"))
        item = self.tabelPelanggan.horizontalHeaderItem(7)
        item.setText(_translate("Form", "foto"))
        item = self.tabelPelanggan.horizontalHeaderItem(8)
        item.setText(_translate("Form", "saldo"))
        item = self.tabelPelanggan.horizontalHeaderItem(9)
        item.setText(_translate("Form", "point"))
        item = self.tabelPelanggan.horizontalHeaderItem(10)
        item.setText(_translate("Form", "rfid"))

    def maleGender(self):
        self.gender = self.radioButton

    def femaleGender(self):
        self.gender = self.radioButton_2
        
    def Topupedit(self):
            i = 0
            tt = self.tabelPelanggan.selectedItems()
            if len(tt) < 1:
                self.parent.showDialog("information", "Informasi","Tolong pilih pelanggan yang hendak Topup")
                return
            else:
                self.hapus.setEnabled(False)
                self.login = Login(self.parent)
                self.login.show()
                if self.login.isLogin:
                    self.topup_new.show()

    def change(self):
        if (self.comboBox.currentText() == "Khusus"):            
            self.tabelPelanggan.clearSelection()
            self.Khusus.show()
            self.nama.clear()
            self.alamat.clear()
            self.hp.clear()
            self.saldo.clear()
            self.ID.hide()
            self.ID.clear()
            self.labelid.hide()
            self.rfid.clear()
            self.radioButton.show()
            self.radioButton_2.show()
            self.point.clear()
            self.point.setReadOnly(False)
            self.point2 = self.point
            self.img.setPixmap(self.pixmap.scaled(200, 170, QtCore.Qt.KeepAspectRatio))
            self.hapus.setEnabled(True)
            self.tabelPelanggan.clearSelection()

        elif(self.comboBox.currentText() == "Regular"):
            self.Khusus.hide()
            self.tabelPelanggan.clearSelection()
            self.nama.clear()
            self.rfid.clear()
            self.alamat.clear()
            self.hp.clear()
            self.saldo.clear()
            self.ID.hide()
            self.labelid.hide()
            self.ID.clear()
            self.point.clear()
            self.point.setReadOnly(True)
            self.point2 = None
            self.radioButton.show()
            self.radioButton_2.show()
            self.img.setPixmap(self.pixmap.scaled(200, 170, QtCore.Qt.KeepAspectRatio))
            self.hapus.setEnabled(True)
            self.tabelPelanggan.clearSelection()

    def flag(self):

        if self.radioButton.isChecked():
            self.gender = self.radioButton
        elif self.radioButton_2.isChecked():
            self.gender = self.radioButton_2

        selected = self.tabelPelanggan.currentItem()
        if(selected is not None and selected.isSelected()):
            print("hai")
            self.register2()
        else:
            if (self.comboBox.currentText() == "Regular"):
                if (self.radioButton.isChecked() or self.radioButton_2.isChecked()):
                    if(self.nama.text() and self.alamat.text() and self.hp.text() and self.rfid.text() != ""):
                        if(self.ui_main_window.n >= 1):
                            self.ui_main_window.n = 0
                            self.register()
                        else:
                            self.parent.showDialog("warning", "Gagal","data tidak boleh kosong")
                            return
                    else:
                        self.parent.showDialog("warning", "Gagal","data tidak boleh kosong")
                        return
                else:
                        self.parent.showDialog("warning", "Gagal","data tidak boleh kosong")
                        return

            if (self.comboBox.currentText() == "Khusus"):
                if (self.radioButton.isChecked() or self.radioButton_2.isChecked()):
                    if(self.nama.text() and self.alamat.text() and self.hp.text() and self.point2.text() and self.rfid.text() != ""):
                        if(self.ui_main_window.n >= 1):
                            self.ui_main_window.n = 0
                            self.register()
                        else:
                            self.parent.showDialog("warning", "Gagal","data tidak boleh kosong")
                            return
                    else:
                        self.parent.showDialog("warning", "Gagal","data tidak boleh kosong")
                        return
                else:
                    self.parent.showDialog("warning", "Gagal","data tidak boleh kosong")
                    return

    def register(self):
        idp = self.ui_main_window.filename[:-4]
        self.code = self.ui_main_window.filename[:-4]
        setpoint = self.pelanggan.find("batasbawah,batastengah,batasatas","setting","idSettings","set-1","False")
        
        if (self.comboBox.currentText() == "Regular"):
            if (self.radioButton.isChecked()):
                point = 0
                if (point < setpoint[0][0]):
                    member = "Bronze"
                if (point >= setpoint[0][0] and point < setpoint[0][1]):
                    member = "Silver"
                if (point > setpoint[0][1] and point < setpoint[0][2]):
                    member = "Gold"
                if (point > setpoint[0][2]):
                    member = "Platinum" 

                val = "\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",{},{}"
                val = val.format(idp,self.rfid.text(),self.nama.text(),"Laki-laki",member, self.alamat.text(),self.hp.text(),self.ui_main_window.filename,0,0)
                err = self.pelanggan.insertTo(
                        "pelanggan", "idPelanggan,rfid,nama,gender,pelanggan.member,alamat,kontak,foto,saldo,point", val)
                self.parent.showDialog("information","success","data berhasil di input")
                self.getProduct()
                self.nama.clear()
                self.alamat.clear()
                self.hp.clear()
                self.ID.clear()
                self.ID.hide()
                self.labelid.hide()
                self.rfid.clear()
                self.saldo.clear()
                self.img.setPixmap(self.pixmap.scaled(200, 170, QtCore.Qt.KeepAspectRatio))
                self.tabelPelanggan.clearSelection()
                self.hapus.setEnabled(True)

            if (self.radioButton_2.isChecked()):
                point = 0
                if (point < setpoint[0][0]):
                    member = "Bronze"
                if (point >= setpoint[0][0] and point < setpoint[0][1]):
                    member = "Silver"
                if (point > setpoint[0][1] and point < setpoint[0][2]):
                    member = "Gold"
                if (point > setpoint[0][2]):
                    member = "Platinum"

                val = "\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",{},{}"
                val = val.format(idp,self.rfid.text(),self.nama.text(),"Perempuan",member, self.alamat.text(),self.hp.text(),self.ui_main_window.filename,0,0)
                err = self.pelanggan.insertTo(
                    "pelanggan", "idPelanggan,rfid,nama,gender,pelanggan.member,alamat,kontak,foto,saldo,point", val)
                self.parent.showDialog("information","success","data berhasil di input")
                self.getProduct()
                self.nama.clear()
                self.alamat.clear()
                self.hp.clear()
                self.rfid.clear()
                self.ID.hide()
                self.labelid.hide()
                self.ID.clear()
                self.saldo.clear()
                self.img.setPixmap(self.pixmap.scaled(200, 170, QtCore.Qt.KeepAspectRatio))
                self.tabelPelanggan.clearSelection()
                self.hapus.setEnabled(True)

        if (self.comboBox.currentText() == "Khusus"):
            if (self.radioButton.isChecked()):
                points = int(self.point2.text())
                if (points < setpoint[0][0]):
                    member = "Bronze"
                if (points >= setpoint[0][0] and points < setpoint[0][1]):
                    member = "Silver"
                if (points > setpoint[0][1] and points < setpoint[0][2]):
                    member = "Gold"
                if (points > setpoint[0][2]):
                    member = "Platinum"

                val = "\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",{},{}"
                val = val.format(idp,self.rfid.text(),self.nama.text(),"Laki-laki",member, self.alamat.text(),self.hp.text(),self.ui_main_window.filename,0,self.point2.text())
                err = self.pelanggan.insertTo(
                        "pelanggan", "idPelanggan,rfid,nama,gender,pelanggan.member,alamat,kontak,foto,saldo,point", val)
                self.parent.showDialog("information","success","data berhasil di input")
                self.getProduct()
                self.nama.clear()
                self.alamat.clear()
                self.hp.clear()
                self.point.clear()
                self.point2.clear()
                self.rfid.clear()
                self.ID.hide()
                self.labelid.hide()
                self.ID.clear()
                self.img.setPixmap(self.pixmap.scaled(200, 170, QtCore.Qt.KeepAspectRatio))
                self.tabelPelanggan.clearSelection()
                self.hapus.setEnabled(True)

            if (self.radioButton_2.isChecked()):
                points = int(self.point2.text())
                if (points < setpoint[0][0]):
                    member = "Bronze"
                if (points >= setpoint[0][0] and points < setpoint[0][1]):
                    member = "Silver"
                if (points > setpoint[0][1] and points < setpoint[0][2]):
                    member = "Gold"
                if (points > setpoint[0][2]):
                    member = "Platinum"

                val = "\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",{},{}"
                val = val.format(idp,self.rfid.text(),self.nama.text(),"Perempuan",member, self.alamat.text(),self.hp.text(),self.ui_main_window.filename,0,self.point2.text())
                err = self.pelanggan.insertTo(
                    "pelanggan", "idPelanggan,rfid,nama,gender,pelanggan.member,alamat,kontak,foto,saldo,point", val)
                self.parent.showDialog("information","success","data berhasil di input")
                self.getProduct()
                self.nama.clear()
                self.alamat.clear()
                self.hp.clear()
                self.point.clear()
                self.point2.clear()
                self.ID.hide()
                self.labelid.hide()
                self.ID.clear()
                self.rfid.clear()
                self.img.setPixmap(self.pixmap.scaled(200, 170, QtCore.Qt.KeepAspectRatio))
                self.tabelPelanggan.clearSelection()
                self.hapus.setEnabled(True)

    def register2(self):
        filename = self.ID.text() + str(".jpg")
        idp = filename[:-4]
        key = "idPelanggan = \"{}\",rfid = \"{}\", nama = \"{}\",gender = \"{}\",alamat= \"{}\",kontak= \"{}\",foto= \"{}\""
        key = key.format(idp,self.rfid.text(),self.nama.text(),self.gender.text(),self.alamat.text(),self.hp.text(),filename)
        ids = "idPelanggan = \"{}\""
        ids = ids.format(idp)
        self.pelanggan.update("pelanggan",key,ids)
                
        self.parent.showDialog("information","success","data berhasil di input")
        self.getProduct()
        self.nama.clear()
        self.alamat.clear()
        self.hp.clear()
        self.saldo.clear()
        self.rfid.clear()
        self.radioButton.show()
        self.radioButton_2.show()
        self.point.clear()
        self.img.setPixmap(self.pixmap.scaled(200, 170, QtCore.Qt.KeepAspectRatio))
        if self.point2 is not None:
            self.point2.clear()
        self.ID.hide()
        self.labelid.hide()
        self.ID.clear()
        self.tabelPelanggan.clearSelection()
        self.hapus.setEnabled(True)

    def takephoto(self):
        self.ui_main_window.show()
        self.ui_main_window.timer.stop()
        self.ui_main_window.cap.release()
        self.ui_main_window.image_label.setText("\t\t\t\tArahkan Wajah Anda\n \t\t\t\tKe Dalam Box Hijau")
        self.ui_main_window.close()

    def getProduct(self):
        listPelanggan = self.pelanggan.select("id,idPelanggan,nama,gender,pelanggan.member,alamat,kontak,foto,saldo,point,rfid", "pelanggan", True)
        self.tabelPelanggan.setRowCount(len(listPelanggan))
        row = 0
        for data in listPelanggan:
            col = 0
            for val in data:
                if col is 0:
                    val = str(val)
                if col is 8:
                    val = "Rp " + str(val)
                if col is 9:
                    val = str(val)
                self.tabelPelanggan.setItem(
                    row, col, QtWidgets.QTableWidgetItem(val))
                col = col + 1
            row = row + 1

    def deleteProduct(self):
        i = 0
        tt = self.tabelPelanggan.selectedItems()
        if len(tt) < 1:
            self.parent.showDialog("information", "Informasi","Tolong pilih pelanggan yang hendak dihapus")
            return
        prompt = self.parent.showDialog("question", "Hapus Pelanggan", "Apakah anda ingin menghapus data pelanggan?")
        if prompt == QtWidgets.QMessageBox.Yes:
            for col in tt:
                if i is 0 or i % 10 is 0:
                    key = "id = \"{}\""
                    self.pelanggan.delete("pelanggan", key.format(col.text()))

                i = i+1
            self.img.setPixmap(self.pixmap.scaled(200, 170, QtCore.Qt.KeepAspectRatio))
            self.nama.clear()
            self.alamat.clear()
            self.hp.clear()
            self.saldo.clear()
            self.point.clear()
            self.ID.clear()
            self.rfid.clear()
            self.radioButton.show()
            self.radioButton_2.show()
            self.getProduct()
            self.tabelPelanggan.clearSelection()

    def findProduct(self):
        listPelanggan = self.pelanggan.find(
            "id,idPelanggan,nama,gender,pelanggan.member,alamat,kontak,foto,saldo,point,rfid", "pelanggan",
            "idPelanggan", self.cari.text(), True,
            "idPelanggan ASC")
        if len(listPelanggan) < 1:
            listPelanggan = self.pelanggan.find(
                "id,idPelanggan,nama,gender,pelanggan.member,alamat,kontak,foto,saldo,point,rfid", "pelanggan",
                "RFID", self.cari.text(), True,
                "idPelanggan ASC")

        self.tabelPelanggan.setRowCount(len(listPelanggan))
        row = 0
        for data in listPelanggan:
            col = 0
            for val in data:
                if col is 0:
                    val = str(val)
                    # print(val)
                if col is 8:
                    val = "Rp " + str(val)
                if col is 9:
                    val = str(val)
                self.tabelPelanggan.setItem(
                    row, col, QtWidgets.QTableWidgetItem(val))
                col = col + 1
            row = row + 1
        self.tabelPelanggan.clearSelection()

    def selectProduct(self):
        row = self.tabelPelanggan.currentRow()
        self.labelid.show()
        self.ID.show()
        self.ID.setEnabled(False)
        self.Khusus.hide()
        self.rfid.setText(self.tabelPelanggan.item(row, 10).text())
        self.ID.setText(self.tabelPelanggan.item(row, 1).text())
        self.nama.setText(self.tabelPelanggan.item(row, 2).text())
        if self.tabelPelanggan.item(row, 3).text() == "Laki-laki":
            self.radioButton.setChecked(True)
        else:
            self.radioButton_2.setChecked(True)
        self.alamat.setText(self.tabelPelanggan.item(row, 5).text())
        self.hp.setText(self.tabelPelanggan.item(row, 6).text())
        self.saldo.setText(self.tabelPelanggan.item(row, 8).text())
        self.point.setText(self.tabelPelanggan.item(row, 9).text())
        path = QtCore.QDir.currentPath()
        path = path + '/Module/static'
        imagepath = path + '/' + self.tabelPelanggan.item(row,7).text()
        imagess = QtGui.QPixmap(imagepath)	
        self.img.setPixmap(imagess.scaled(200,250,QtCore.Qt.KeepAspectRatio))

    def show(self):
        self.pelangganWidget.show()
    
    def close(self):
        self.pelangganWidget.close()