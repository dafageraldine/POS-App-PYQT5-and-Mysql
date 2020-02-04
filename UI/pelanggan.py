# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pelanggan.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 600)
        Form.setMinimumSize(QtCore.QSize(600, 600))
        Form.setStyleSheet("")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pelangganWidget = QtWidgets.QWidget(Form)
        self.pelangganWidget.setMinimumSize(QtCore.QSize(350, 0))
        self.pelangganWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pelangganWidget.setStyleSheet("")
        self.pelangganWidget.setObjectName("pelangganWidget")
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
        self.gridLayout_2.addWidget(self.rfid, 2, 1, 1, 1)
        self.labelid = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelid.setFont(font)
        self.labelid.setObjectName("labelid")
        self.gridLayout_2.addWidget(self.labelid, 1, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.widget_4)
        self.widget.setMaximumSize(QtCore.QSize(270, 38))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton.setFont(font)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_2.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
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
        font.setWeight(75)
        self.Khusus.setFont(font)
        self.Khusus.setStyleSheet("color: red;")
        self.Khusus.setAlignment(QtCore.Qt.AlignCenter)
        self.Khusus.setObjectName("Khusus")
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
        self.label_jenis = QtWidgets.QLabel(self.widget_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_jenis.setFont(font)
        self.label_jenis.setObjectName("label_jenis")
        self.gridLayout.addWidget(self.label_jenis, 5, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 37, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem1, 4, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 3, 1, 1)
        self.img = QtWidgets.QLabel(self.widget_6)
        self.img.setMinimumSize(QtCore.QSize(180, 230))
        self.img.setStyleSheet("background: lightgrey;")
        self.img.setAlignment(QtCore.Qt.AlignCenter)
        self.img.setObjectName("img")
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
        self.gridLayout.addWidget(self.foto, 2, 0, 1, 3)
        self.data = QtWidgets.QLabel(self.widget_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.data.setFont(font)
        self.data.setStyleSheet("")
        self.data.setAlignment(QtCore.Qt.AlignCenter)
        self.data.setObjectName("data")
        self.gridLayout.addWidget(self.data, 0, 0, 1, 3)
        self.comboBox = QtWidgets.QComboBox(self.widget_6)
        self.comboBox.setMinimumSize(QtCore.QSize(115, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 5, 1, 1, 2)
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
        self.gridLayout_6.addWidget(self.Topup, 3, 3, 1, 1)
        self.tabelPelanggan = QtWidgets.QTableWidget(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabelPelanggan.sizePolicy().hasHeightForWidth())
        self.tabelPelanggan.setSizePolicy(sizePolicy)
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
        self.gridLayout_6.addWidget(self.tabelPelanggan, 0, 0, 1, 4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem3, 3, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_6.addItem(spacerItem4, 4, 2, 1, 1)
        self.verticalLayout_3.addWidget(self.widget_5)
        self.horizontalLayout.addWidget(self.pelangganWidget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

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
        self.labelrfid.setText(_translate("Form", "RFID"))
        self.labelAlamat.setText(_translate("Form", "Alamat"))
        self.Khusus.setText(_translate("Form", "ANDA MENAMBAHKAN PELANGGAN KHUSUS"))
        self.label_jenis.setText(_translate("Form", "Jenis Pelanggan"))
        self.img.setText(_translate("Form", "Image"))
        self.foto.setText(_translate("Form", "CAPTURE"))
        self.data.setText(_translate("Form", "FOTO PELANGGAN"))
        self.comboBox.setItemText(0, _translate("Form", "Regular"))
        self.comboBox.setItemText(1, _translate("Form", "Khusus"))
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
