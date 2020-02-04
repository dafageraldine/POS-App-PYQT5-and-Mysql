from PyQt5 import QtCore, QtGui, QtWidgets
from Module.login import *
from Module.keypad import *

class Settings():
    def __init__(self, parent):
        self.pelanggan = parent.mysql
        self.parent = parent
        self.login = Login(self.parent)
        self.y = 0
        self.forgot = False

        self.settingWidget = QtWidgets.QWidget(parent)
        self.settingWidget.setMinimumSize(QtCore.QSize(350, 0))
        self.settingWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.settingWidget.setStyleSheet("")
        self.settingWidget.setObjectName("settingWidget")
        self.settingWidget.setStyleSheet("")
        self.formLayout = QtWidgets.QFormLayout(self.settingWidget)
        self.formLayout.setObjectName("formLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
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
        self.gridLayout.addWidget(self.cam, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.settingWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.camval = QtWidgets.QLineEdit(self.settingWidget)
        self.camval.setEnabled(False)
        self.camval.setMinimumSize(QtCore.QSize(200, 30))
        self.camval.setObjectName("camval")
        self.horizontalLayout_2.addWidget(self.camval)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 2)
        self.simpan_cam = QtWidgets.QPushButton(self.settingWidget)
        self.simpan_cam.setMinimumSize(QtCore.QSize(0, 35))
        self.simpan_cam.setStyleSheet("QPushButton {\n"
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
        self.simpan_cam.setObjectName("simpan_cam")
        self.simpan_cam.clicked.connect(self.saveCam)
        self.gridLayout.addWidget(self.simpan_cam, 2, 1, 1, 1)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.gridLayout)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label1 = QtWidgets.QLabel(self.settingWidget)
        self.label1.setObjectName("label1")
        self.gridLayout_3.addWidget(self.label1, 1, 0, 1, 1)
        self.pointB = QtWidgets.QLineEdit(self.settingWidget)
        self.pointB.setEnabled(False)
        self.pointB.setMinimumSize(QtCore.QSize(0, 30))
        self.pointB.setObjectName("pointB")
        self.gridLayout_3.addWidget(self.pointB, 2, 0, 1, 1)
        self.label2 = QtWidgets.QLabel(self.settingWidget)
        self.label2.setObjectName("label2")
        self.gridLayout_3.addWidget(self.label2, 3, 0, 1, 1)
        self.pointS = QtWidgets.QLineEdit(self.settingWidget)
        self.pointS.setEnabled(False)
        self.pointS.setMinimumSize(QtCore.QSize(0, 30))
        self.pointS.setObjectName("pointS")
        self.gridLayout_3.addWidget(self.pointS, 4, 0, 1, 1)
        self.label3 = QtWidgets.QLabel(self.settingWidget)
        self.label3.setObjectName("label3")
        self.gridLayout_3.addWidget(self.label3, 5, 0, 1, 1)
        self.simpan_2 = QtWidgets.QPushButton(self.settingWidget)
        self.simpan_2.setMinimumSize(QtCore.QSize(100, 35))
        self.simpan_2.setStyleSheet("QPushButton {\n"
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
        self.simpan_2.setObjectName("simpan_2")
        self.simpan_2.clicked.connect(self.savePoint)
        self.gridLayout_3.addWidget(self.simpan_2, 5, 1, 2, 1)
        self.pointG = QtWidgets.QLineEdit(self.settingWidget)
        self.pointG.setEnabled(False)
        self.pointG.setMinimumSize(QtCore.QSize(0, 30))
        self.pointG.setObjectName("pointG")
        self.gridLayout_3.addWidget(self.pointG, 6, 0, 1, 1)
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
        self.gridLayout_3.addWidget(self.point, 0, 0, 1, 1)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.LabelRole, self.gridLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(614, 199, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_2 = QtWidgets.QLabel(self.settingWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1)
        self.password = QtWidgets.QLineEdit(self.settingWidget)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setEnabled(False)
        self.password.setMinimumSize(QtCore.QSize(0, 30))
        self.password.setObjectName("password")
        self.gridLayout_4.addWidget(self.password, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.settingWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 2, 0, 1, 1)
        self.password_2 = QtWidgets.QLineEdit(self.settingWidget)
        self.password_2.setEnabled(False)
        self.password_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_2.setMinimumSize(QtCore.QSize(0, 30))
        self.password_2.setObjectName("password_2")
        self.gridLayout_4.addWidget(self.password_2, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.settingWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 3, 0, 1, 1)
        self.password_3 = QtWidgets.QLineEdit(self.settingWidget)
        self.password_3.setEnabled(False)
        self.password_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_3.setMinimumSize(QtCore.QSize(0, 30))
        self.password_3.setObjectName("password_3")
        self.gridLayout_4.addWidget(self.password_3, 3, 1, 1, 1)
        self.lupaPassword = QtWidgets.QPushButton(self.settingWidget)
        self.lupaPassword.setMinimumSize(QtCore.QSize(0, 30))
        self.lupaPassword.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lupaPassword.setObjectName("lupaPassword")
        self.lupaPassword.clicked.connect(self.lupaSandi)
        self.gridLayout_4.addWidget(self.lupaPassword, 4, 0, 1, 1)
        self.simpan_password = QtWidgets.QPushButton(self.settingWidget)
        self.simpan_password.setMinimumSize(QtCore.QSize(100, 35))
        self.simpan_password.setStyleSheet("QPushButton {\n"
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
        self.simpan_password.setObjectName("simpan_password")
        self.simpan_password.clicked.connect(self.savePass)
        self.gridLayout_4.addWidget(self.simpan_password, 4, 1, 1, 1)
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
        self.gridLayout_4.addWidget(self.ubahPassword, 0, 0, 1, 1)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.LabelRole, self.gridLayout_4)
        self.close()

        self.retranslateUi(parent)
        QtCore.QMetaObject.connectSlotsByName(parent)

    def retranslateUi(self, parent):
        _translate = QtCore.QCoreApplication.translate
        parent.setWindowTitle(_translate("parent", "parent"))
        self.cam.setText(_translate("parent", "Edit Video Capture Value"))
        self.label.setText(_translate("parent", "Set Camera Value"))
        self.simpan_cam.setText(_translate("parent", "Simpan"))
        self.label1.setText(_translate("parent", "Bronze"))
        self.pointB.setPlaceholderText(_translate("parent", "Masukkan poin maksimum untuk kategori Bronze"))
        self.label2.setText(_translate("parent", "Silver"))
        self.pointS.setPlaceholderText(_translate("parent", "Masukkan poin maksimum untuk kategori Silver"))
        self.label3.setText(_translate("parent", "Gold"))
        self.simpan_2.setText(_translate("parent", "Simpan"))
        self.pointG.setPlaceholderText(_translate("parent", "Masukkan poin maksimum untuk kategori Gold"))
        self.point.setText(_translate("parent", "Edit Point"))
        self.label_2.setText(_translate("parent", "Old Password"))
        self.label_3.setText(_translate("parent", "New Password"))
        self.label_4.setText(_translate("parent", "Confirm Password"))
        self.lupaPassword.setText(_translate("parent", "Lupa Password"))
        self.simpan_password.setText(_translate("parent", "Simpan"))
        self.ubahPassword.setText(_translate("parent", "Edit password"))


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
        self.forgot = True
        self.password.setEnabled(False)
        self.password_2.setEnabled(True)
        self.password_3.setEnabled(True)


    def ubahSandi(self):
        if not self.login.isLogin:
            self.login.show()
            if self.login.isLogin:
                self.password.setEnabled(True)
                self.password_2.setEnabled(True)
                self.password_3.setEnabled(True)


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

    def saveCam(self):
        k = "set-1"
        z = self.camval.text()
        if self.camval.isEnabled()==False:
            self.parent.showDialog("information","Informasi","anda tidak melakukan perubahan")
            return
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

    def savePoint(self):
        k = "set-1"
        if not self.pointB.isEnabled():
            self.parent.showDialog("information","Informasi","anda tidak melakukan perubahan")
            return

        elif self.pointB.isEnabled():
            r = self.pointS.text()
            v = self.pointB.text()
            m = self.pointG.text()
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

    def savePass(self):
        if not self.password_3.isEnabled():
            self.parent.showDialog("information","Informasi","anda tidak melakukan perubahan")
            return

        if not self.forgot and self.password.text() is "" or self.password_2.text() is "" or self.password_3.text() is "":
            self.parent.showDialog("warning","Warning","Harap mengisi semua form")
            return

        if self.forgot and self.password_2.text() is "" or self.password_3.text() is "":
            self.parent.showDialog("warning","Warning","Harap mengisi semua form")
            return

        if not self.forgot:
            password = "password=\""+ self.password.text() +"\""
            res = self.pelanggan.findCol("username", "bulleyearchery.admin", password, False)
            if res is None or res == None:
                self.parent.showDialog("warning","Warning","Password lama yang dimasukkan salah")
                return

        if self.password_2.text() != self.password_3.text():
            self.parent.showDialog("warning","Warning","Password konfirmasi dan password baru tidak cocok")
            return

        setval = "password=\"{}\""
        setval = setval.format(self.password_3.text())
        self.pelanggan.update("bulleyearchery.admin", setval, "username=\"admin\"")
        self.password.setEnabled(False)
        self.password_2.setEnabled(False)
        self.password_3.setEnabled(False)
        self.password.clear()
        self.password_2.clear()
        self.password_3.clear()
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