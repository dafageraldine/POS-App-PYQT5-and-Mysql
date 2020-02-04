# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'transaksi.ui'
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
        self.transaksiWidget = QtWidgets.QWidget(Form)
        self.transaksiWidget.setMinimumSize(QtCore.QSize(350, 0))
        self.transaksiWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.transaksiWidget.setStyleSheet("")
        self.transaksiWidget.setObjectName("transaksiWidget")
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
        self.id.setReadOnly(True)
        self.id.setPlaceholderText("")
        self.id.setClearButtonEnabled(True)
        self.id.setObjectName("id")
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
        self.gridLayout_6.addWidget(self.tabelTransaksi, 0, 0, 1, 2)
        self.widget = QtWidgets.QWidget(self.widget_5)
        self.widget.setMinimumSize(QtCore.QSize(0, 46))
        self.widget.setObjectName("widget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_5.addWidget(self.comboBox, 1, 0, 1, 1)
        self.total = QtWidgets.QLineEdit(self.widget)
        self.total.setMaximumSize(QtCore.QSize(300, 16777215))
        self.total.setStyleSheet("font-size: 14pt;\n"
"padding: 0 10px;")
        self.total.setAlignment(QtCore.Qt.AlignCenter)
        self.total.setReadOnly(True)
        self.total.setObjectName("total")
        self.gridLayout_5.addWidget(self.total, 1, 4, 1, 1)
        self.cancel = QtWidgets.QPushButton(self.widget)
        self.cancel.setMinimumSize(QtCore.QSize(200, 35))
        self.cancel.setStyleSheet("QPushButton {\n"
"    background: #ff3d00;\n"
"    border-radius: 6px;\n"
"    border: none;\n"
"    color: white;\n"
"    transition: .4s;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 2px solid #ff3d00;\n"
"    background: white;\n"
"    color: #ff3d00;\n"
"}")
        self.cancel.setObjectName("cancel")
        self.gridLayout_5.addWidget(self.cancel, 2, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(485, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem3, 2, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_5.addItem(spacerItem4, 3, 1, 1, 1)
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
"    transition: .4s;\n"
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
        self.horizontalLayout_2.addWidget(self.hapusBtn)
        self.prosesBtn = QtWidgets.QPushButton(self.widget)
        self.prosesBtn.setMinimumSize(QtCore.QSize(0, 35))
        self.prosesBtn.setStyleSheet("QPushButton {\n"
"    background: #2962ff;\n"
"    border-radius: 6px;\n"
"    border: none;\n"
"    color: white;\n"
"    transition: .4s;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 2px solid #2962ff;\n"
"    background: white;\n"
"    color: #2962ff;\n"
"}")
        self.prosesBtn.setObjectName("prosesBtn")
        self.horizontalLayout_2.addWidget(self.prosesBtn)
        self.gridLayout_5.addLayout(self.horizontalLayout_2, 2, 4, 1, 1)
        self.line_game = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.line_game.setFont(font)
        self.line_game.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.line_game.setObjectName("line_game")
        self.gridLayout_5.addWidget(self.line_game, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.widget, 1, 0, 1, 2)
        self.verticalLayout_3.addWidget(self.widget_5)
        self.horizontalLayout.addWidget(self.transaksiWidget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

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
        self.total.setText(_translate("Form", "Rp 0"))
        self.cancel.setText(_translate("Form", "Cancel"))
        self.hapusBtn.setText(_translate("Form", "Hapus"))
        self.prosesBtn.setText(_translate("Form", "Proses"))
        self.line_game.setText(_translate("Form", "Line Game"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
