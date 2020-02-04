from PyQt5 import QtCore, QtGui, QtWidgets
from Module.login import *
from Module.keypad import *

class Settings():
    def __init__(self, parent):
        self.pelanggan = parent.mysql
        self.parent = parent
        self.login = Login(self.parent)
        self.y = 0

        self.settingWidget = QtWidgets.QWidget(parent)
        self.settingWidget.setMinimumSize(QtCore.QSize(350, 0))
        self.settingWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.settingWidget.setStyleSheet("")
        self.settingWidget.setObjectName("settingWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.settingWidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label1 = QtWidgets.QLabel(self.settingWidget)
        self.label1.setObjectName("label1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label1)
        self.point = QtWidgets.QPushButton(self.settingWidget)
        self.point.setMinimumSize(QtCore.QSize(200, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.point.setFont(font)
        self.point.setStyleSheet("QPushButton {\n"
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
        self.point.setObjectName("point")
        self.point.clicked.connect(self.log)


        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.point)
        self.pointB = QtWidgets.QLineEdit(self.settingWidget)
        self.pointB.setEnabled(False)
        self.pointB.setObjectName("pointB")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pointB)
        self.label2 = QtWidgets.QLabel(self.settingWidget)
        self.label2.setObjectName("label2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label2)
        self.pointS = QtWidgets.QLineEdit(self.settingWidget)
        self.pointS.setEnabled(False)
        self.pointS.setObjectName("pointS")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.pointS)
        self.label3 = QtWidgets.QLabel(self.settingWidget)
        self.label3.setObjectName("label3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.label3)
        self.pointG = QtWidgets.QLineEdit(self.settingWidget)
        self.pointG.setEnabled(False)
        self.pointG.setObjectName("pointG")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.pointG)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setItem(7, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.ubahPassword = QtWidgets.QPushButton(self.settingWidget)
        self.ubahPassword.setMinimumSize(QtCore.QSize(200, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ubahPassword.setFont(font)
        self.ubahPassword.setStyleSheet("QPushButton {\n"
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
        self.ubahPassword.setObjectName("ubahPassword")
        self.ubahPassword.clicked.connect(self.ubahSandi)
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.ubahPassword)
        self.password = QtWidgets.QLineEdit(self.settingWidget)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setEnabled(False)
        self.password.setObjectName("password")
        self.password.setMaxLength(4)
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.password)
        self.lupaPassword = QtWidgets.QPushButton(self.settingWidget)
        self.lupaPassword.setObjectName("lupaPassword")
        self.lupaPassword.clicked.connect(self.lupaSandi)
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.lupaPassword)
        self.gridLayout.addLayout(self.formLayout, 3, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)
        self.cam = QtWidgets.QPushButton(self.settingWidget)
        self.cam.setMinimumSize(QtCore.QSize(200, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cam.setFont(font)
        self.cam.setStyleSheet("QPushButton {\n"
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
    "}\n"
    "")
        self.cam.setObjectName("cam")
        self.cam.clicked.connect(self.picture)

        self.gridLayout.addWidget(self.cam, 1, 0, 1, 1)
        self.camval = QtWidgets.QLineEdit(self.settingWidget)
        self.camval.setEnabled(False)
        self.camval.setObjectName("camval")
        self.gridLayout.addWidget(self.camval, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 2, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(-1, 0, 0, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.simpan = QtWidgets.QPushButton(self.settingWidget)
        self.simpan.setMinimumSize(QtCore.QSize(160, 35))
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
        self.simpan.clicked.connect(self.save)


        self.gridLayout_2.addWidget(self.simpan, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 0, 2, 1, 1)
        self.cancel = QtWidgets.QPushButton(self.settingWidget)
        self.cancel.setMinimumSize(QtCore.QSize(160, 35))
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

        self.gridLayout_2.addWidget(self.cancel, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_2.addItem(spacerItem4, 1, 2, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 4, 0, 1, 2)
        self.horizontalLayout_3.addLayout(self.gridLayout)
        # self.verticalLayout.addWidget(self.settingWidget)

        self.retranslateUi(parent)
        QtCore.QMetaObject.connectSlotsByName(parent)
        self.close()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label1.setText(_translate("Form", "Bronze"))
        self.point.setText(_translate("Form", "Edit Point"))
        self.pointB.setPlaceholderText(_translate("Form", "Masukkan poin maksimum untuk kategori Bronze"))
        self.label2.setText(_translate("Form", "Silver"))
        self.pointS.setPlaceholderText(_translate("Form", "Masukkan poin maksimum untuk kategori Silver"))
        self.label3.setText(_translate("Form", "Gold"))
        self.pointG.setPlaceholderText(_translate("Form", "Masukkan poin maksimum untuk kategori Gold"))
        self.ubahPassword.setText(_translate("Form", "Ubah password"))
        self.lupaPassword.setText(_translate("Form", "Lupa Password"))
        self.cam.setText(_translate("Form", "Edit Video Capture Value"))
        self.simpan.setText(_translate("Form", "Simpan"))
        self.cancel.setText(_translate("Form", "cancel"))

    def lupaSandi(self):
        masterKey = Keypad(self.parent, 4)
        masterKey.value.setEchoMode(QtWidgets.QLineEdit.Password)
        masterKey.show()
        k = "username=\"master\" AND password=\"{}\""
        k = k.format(masterKey.val)
        query = self.pelanggan.findCol("password","bulleyearchery.admin",k, False)
        if query is None:
            self.parent.showDialog("warning","Warning","Maaf password salah")
            return
        self.login.isLogin = True
        self.password.setEnabled(True)


    def ubahSandi(self):
        if not self.login.isLogin:
            self.login.show()
            self.password.setEnabled(True)
            return


    def dont(self):
        font = QtGui.QFont()
        font.setPointSize(12)
        self.camval.setFont(font)
        self.camval.clear()
        self.camval.setPlaceholderText("")
        self.camval.setEnabled(False)
        self.cam.setEnabled(True)
        self.pointB.clear()
        self.pointS.clear()
        self.pointG.clear()
        self.pointB.setPlaceholderText("    Masukkan Nilai Maksimum")
        self.pointS.setPlaceholderText("    Masukkan Nilai Maksimum")
        self.pointG.setPlaceholderText("    Masukkan Nilai Maksimum")
        self.pointB.setEnabled(False)
        self.pointS.setEnabled(False)
        self.pointG.setEnabled(False)
        self.point.setEnabled(True)

    def picture(self):
        self.camval.setEnabled(True)
        self.cam.setEnabled(False)
        self.x = self.pelanggan.select("camera","setting",True)
        self.camval.setPlaceholderText("current value " + str(self.x[0][0]))

    def log(self):
        self.login = Login(self.parent)
        self.login.show()
        if self.login.isLogin:
            self.point.setEnabled(True)
            x = self.pelanggan.select("batasbawah,batastengah,batasatas","setting",True)
            self.pointB.setPlaceholderText("current value " + str(x[0][0]))
            self.pointS.setPlaceholderText("current value " + str(x[0][1]))
            self.pointG.setPlaceholderText("current value " + str(x[0][2]))
            self.pointB.setEnabled(True)
            self.pointS.setEnabled(True)
            self.pointG.setEnabled(True)
            self.point.setEnabled(False)

    def save(self):
        k = "set-1"
        z = self.camval.text()
        r = self.pointS.text()
        v = self.pointB.text()
        m = self.pointG.text()
        if self.pointB.isEnabled()==False and self.camval.isEnabled()==False and not self.ubahPassword.isEnabled():
            self.parent.showDialog("information","Informasi","anda tidak melakukan perubahan")
            return
        if self.pointB.isEnabled()==False and self.camval.isEnabled()==True:
            if z != "" :
                val = "camera = {}"
                val = val.format(self.camval.text())
                key = "idSettings = \"{}\""
                key = key.format(k)
                self.pelanggan.update("setting",val,key)
                self.camval.clear()
                self.camval.setEnabled(False)
                self.cam.setEnabled(True)
                x = self.pelanggan.select("camera","setting",True)
                self.camval.setPlaceholderText("current value " + str(x[0][0]))
                self.parent.showDialog("information", "Informasi","berhasil melakukan perubahan")
                return
            if z == "":
                self.parent.showDialog("information", "Informasi","tidak boleh ada kolom yang kosong")
                return
        if self.pointB.isEnabled()==True and self.camval.isEnabled()==False:
            if r =="" or v=="" or m == "":
                self.parent.showDialog("information", "Informasi","tidak boleh ada kolom yang kosong")
                return
            else:
                val = "batasbawah = {}, batastengah = {},batasatas = {}"
                val = val.format(self.pointB.text(),self.pointS.text(),self.pointG.text())
                key = "idSettings = \"{}\""
                key = key.format(k)
                self.pelanggan.update("setting",val,key)
                self.parent.showDialog("information", "Informasi","berhasil melakukan perubahan")
                self.member_()
                self.pointB.setPlaceholderText("Masukkan Nilai Maksimum")
                self.pointB.clear()
                self.pointB.setEnabled(False)
                self.pointS.setPlaceholderText("Masukkan Nilai Maksimum")
                self.pointS.clear()
                self.pointS.setEnabled(False)
                self.pointG.setPlaceholderText("Masukkan Nilai Maksimum")
                self.pointG.clear()
                self.pointG.setEnabled(False)
                self.point.setEnabled(True)
                return
        if self.pointB.isEnabled()==True and self.camval.isEnabled()==True:
            if r =="" or v=="" or z =="" or m =="":
                self.parent.showDialog("information", "Informasi","tidak boleh ada kolom yang kosong")
                return
            else: 
                val = "camera = {}, batasbawah = {}, batastengah = {}, batasatas = {}"
                val = val.format(self.camval.text(),self.pointB.text(),self.pointS.text(),self.pointG.text())
                key = "idSettings = \"{}\""
                key = key.format(k)
                self.pelanggan.update("setting",val,key)
                self.parent.showDialog("information", "Informasi","berhasil melakukan perubahan")
                x = self.pelanggan.select("camera","setting",True)
                self.camval.setPlaceholderText("current value " + str(x[0][0]))
                self.member_()
                self.camval.clear()
                self.camval.setEnabled(False)
                self.cam.setEnabled(True)
                self.pointB.setPlaceholderText("Masukkan Nilai Maksimum")
                self.pointB.clear()
                self.pointB.setEnabled(False)
                self.pointS.setPlaceholderText("Masukkan Nilai Maksimum")
                self.pointS.clear()
                self.pointS.setEnabled(False)
                self.pointG.setPlaceholderText("Masukkan Nilai Maksimum")
                self.pointG.clear()
                self.pointG.setEnabled(False)
                self.point.setEnabled(True)
                return

        if self.ubahPassword.isEnabled():
            if self.password.text() is "":
                self.parent.showDialog("warning","Warning","Harap masukkan password baru")
                return
            setval = "password=\"{}\""
            setval = setval.format(self.password.text())                
            self.pelanggan.update("bulleyearchery.admin", setval, "username=\"admin\"")
            self.password.setEnabled(False)
            self.parent.showDialog("information","Berhasil","Berhasil mengubah password")
            self.login = Login(self.parent)                
                
    def member_(self):
        listPelanggan = self.pelanggan.select("idPelanggan,point","pelanggan",True)
        setpoint = self.pelanggan.find("batasbawah,batastengah,batasatas","setting","idSettings","set-1","False")
        ins = len(listPelanggan)
        for i in range (ins):
            vals = "pelanggan.member = \"{}\""
            keyz = "idPelanggan = \"{}\""
            k = listPelanggan[i][0]
            keyz =keyz.format(k)
            pointN = listPelanggan[i][1]
            if (pointN < setpoint[0][0]):
                member = "Bronze"
            if (pointN >= setpoint[0][0] and pointN < setpoint[0][1]):
                member = "Silver"
            if (pointN >= setpoint[0][1] and pointN < setpoint[0][2]):
                member = "Gold"
            if (pointN >= setpoint[0][2]):
                member = "Platinum"
            vals = vals.format(member)
            self.pelanggan.update("pelanggan",vals,keyz)

    def show(self):
        self.settingWidget.show()

    def close(self):
        self.settingWidget.close()