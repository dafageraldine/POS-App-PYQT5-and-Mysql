from PyQt5 import QtCore, QtGui, QtWidgets
from Module.keypad import *
import socket
from threading import *

import platform    # For getting the operating system name
import subprocess  # For executing a shell command

class DisplayInfo():

    def __init__(self, parent):
        self.parent = parent
        self.state = True

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.displayInfo = QtWidgets.QWidget(parent)
        self.displayInfo.setMinimumSize(QtCore.QSize(350, 0))
        self.displayInfo.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.displayInfo.setStyleSheet("")
        self.displayInfo.setObjectName("displayInfoWidget")
        self.displayInfo.setSizePolicy(sizePolicy)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.displayInfo)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.displayInfo)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_broadcast = QtWidgets.QWidget()
        self.tab_broadcast.setObjectName("tab_broadcast")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_broadcast)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 1, 1, 1)
        self.broadcastBtn = QtWidgets.QPushButton(self.tab_broadcast)
        self.broadcastBtn.setMinimumSize(QtCore.QSize(100, 100))
        self.broadcastBtn.setStyleSheet("")
        path = QtCore.QDir.currentPath()
        path = path + "/UI/Caution.png"
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.broadcastBtn.setIcon(icon)
        self.broadcastBtn.setIconSize(QtCore.QSize(40, 40))
        self.broadcastBtn.setObjectName("broadcastBtn")
        self.broadcastBtn.clicked.connect(self.BroadcastButton)
        self.gridLayout.addWidget(self.broadcastBtn, 1, 2, 1, 1)
        self.refreshBtn = QtWidgets.QPushButton(self.tab_broadcast)
        self.refreshBtn.setMinimumSize(QtCore.QSize(0, 35))
        self.refreshBtn.setStyleSheet("QPushButton {\n"
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
        self.refreshBtn.setObjectName("refreshBtn")
        self.refreshBtn.clicked.connect(self.getConnected)
        self.gridLayout.addWidget(self.refreshBtn, 2, 2, 1, 1)
        self.tabel_conn = QtWidgets.QTableWidget(self.tab_broadcast)
        self.tabel_conn.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabel_conn.setObjectName("tabel_conn")
        self.tabel_conn.setColumnCount(3)
        self.tabel_conn.setRowCount(0)
        header = self.tabel_conn.horizontalHeader()
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        
        item = QtWidgets.QTableWidgetItem()
        self.tabel_conn.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_conn.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_conn.setHorizontalHeaderItem(2, item)
        headerconn = self.tabel_conn.horizontalHeader()
        headerconn.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        headerconn.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        headerconn.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.gridLayout.addWidget(self.tabel_conn, 1, 1, 2, 1)

        self.tabWidget.addTab(self.tab_broadcast, "")
        self.tab_konektivitas = QtWidgets.QWidget()
        self.tab_konektivitas.setObjectName("tab_konektivitas")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_konektivitas)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.updateBtn = QtWidgets.QPushButton(self.tab_konektivitas)
        self.updateBtn.setMinimumSize(QtCore.QSize(85, 35))
        self.updateBtn.setStyleSheet("QPushButton {\n"
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
        self.updateBtn.setObjectName("updateBtn")
        self.updateBtn.clicked.connect(self.UpdateList)
        self.gridLayout_2.addWidget(self.updateBtn, 0, 2, 3, 1)
        self.ip = QtWidgets.QLineEdit(self.tab_konektivitas)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ip.setFont(font)
        self.ip.setStyleSheet("padding: 0 10px;")
        self.ip.setObjectName("ip")
        self.gridLayout_2.addWidget(self.ip, 2, 1, 1, 1)
        self.refresh = QtWidgets.QPushButton(self.tab_konektivitas)
        self.refresh.setMinimumSize(QtCore.QSize(0, 35))
        self.refresh.setStyleSheet("QPushButton {\n"
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
        self.refresh.setObjectName("refresh")
        self.refresh.clicked.connect(self.refreshPing)
        self.gridLayout_2.addWidget(self.refresh, 3, 3, 1, 1)
        self.label_line = QtWidgets.QLabel(self.tab_konektivitas)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_line.setFont(font)
        self.label_line.setObjectName("label_line")
        self.gridLayout_2.addWidget(self.label_line, 0, 0, 1, 1)
        self.line = QtWidgets.QComboBox(self.tab_konektivitas)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.line.setFont(font)
        self.line.setStyleSheet("padding: 0 10px;")
        self.line.setObjectName("line")
        self.createList()
        self.line.currentIndexChanged.connect(self.findLineIp)

        self.gridLayout_2.addWidget(self.line, 0, 1, 2, 1)
        self.hapusBtn = QtWidgets.QPushButton(self.tab_konektivitas)
        self.hapusBtn.setMinimumSize(QtCore.QSize(85, 35))
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
        self.hapusBtn.setObjectName("hapusBtn")
        self.hapusBtn.clicked.connect(self.deleteList)
        self.gridLayout_2.addWidget(self.hapusBtn, 0, 3, 3, 1)
        self.label_ip = QtWidgets.QLabel(self.tab_konektivitas)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_ip.setFont(font)
        self.label_ip.setObjectName("label_ip")
        self.gridLayout_2.addWidget(self.label_ip, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 4, 3, 1, 1)
        self.tabel_ip = QtWidgets.QTableWidget(self.tab_konektivitas)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabel_ip.sizePolicy().hasHeightForWidth())
        self.tabel_ip.setSizePolicy(sizePolicy)
        self.tabel_ip.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tabel_ip.setStyleSheet("")
        self.tabel_ip.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tabel_ip.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabel_ip.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tabel_ip.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tabel_ip.setObjectName("tabel_ip")
        self.tabel_ip.setColumnCount(3)
        self.tabel_ip.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_ip.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_ip.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabel_ip.setHorizontalHeaderItem(2, item)
        self.tabel_ip.horizontalHeader().setCascadingSectionResizes(True)
        header = self.tabel_ip.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tabel_ip.itemClicked.connect(self.selectList)
        self.gridLayout_2.addWidget(self.tabel_ip, 3, 0, 2, 3)

        self.tabWidget.addTab(self.tab_konektivitas, "")
        self.tab_ads = QtWidgets.QWidget()
        self.tab_ads.setObjectName("tab_ads")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_ads)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.tab_ads)
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label.setStyleSheet("font-size: 12pt;")
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.img = QtWidgets.QLabel(self.tab_ads)
        self.img.setMinimumSize(QtCore.QSize(0, 321))
        self.img.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.img.setStyleSheet("")
        self.img.setAlignment(QtCore.Qt.AlignCenter)
        self.img.setObjectName("img")
        self.gridLayout_3.addWidget(self.img, 2, 3, 1, 2)
        self.file_list = QtWidgets.QTableWidget(self.tab_ads)
        self.file_list.setObjectName("file_list")
        self.file_list.setColumnCount(1)
        self.file_list.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.file_list.setHorizontalHeaderItem(0, item)
        self.file_list.itemClicked.connect(self.selectFile)
        header = self.file_list.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.gridLayout_3.addWidget(self.file_list, 2, 0, 5, 3)
        self.line_2 = QtWidgets.QFrame(self.tab_ads)
        self.line_2.setStyleSheet("border-color: red;")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_3.addWidget(self.line_2, 1, 0, 1, 5)
        self.browseBtn = QtWidgets.QPushButton(self.tab_ads)
        self.browseBtn.setMinimumSize(QtCore.QSize(0, 35))
        self.browseBtn.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.browseBtn.setFont(font)
        self.browseBtn.setStyleSheet("QPushButton {\n"
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
        self.browseBtn.setObjectName("browseBtn")
        self.browseBtn.clicked.connect(self.uploadImage)
        self.gridLayout_3.addWidget(self.browseBtn, 0, 3, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.tab_ads)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_3.addWidget(self.lineEdit, 0, 1, 1, 2)
        self.kirimAds = QtWidgets.QPushButton(self.tab_ads)
        self.kirimAds.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.kirimAds.setFont(font)
        self.kirimAds.setStyleSheet("QPushButton {\n"
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
        self.kirimAds.setObjectName("kirimAds")
        self.kirimAds.clicked.connect(self.sendAds)
        self.gridLayout_3.addWidget(self.kirimAds, 4, 3, 1, 1)
        self.hapusBtn_2 = QtWidgets.QPushButton(self.tab_ads)
        self.hapusBtn_2.setMinimumSize(QtCore.QSize(0, 35))
        self.hapusBtn_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.hapusBtn_2.setFont(font)
        self.hapusBtn_2.setStyleSheet("QPushButton {\n"
"    background-color: #ff3d00;\n"
"    border:none;\n"
"    color:white;\n"
"    border-radius: 6px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: white;\n"
"    border: 2px solid #ff3d00;\n"
"    color: #ff3d00;\n"
"}")
        self.hapusBtn_2.setObjectName("hapusBtn_2")
        self.hapusBtn_2.clicked.connect(self.deleteAds)
        self.gridLayout_3.addWidget(self.hapusBtn_2, 5, 3, 1, 1)
        self.tabWidget.addTab(self.tab_ads, "")
        self.horizontalLayout_3.addWidget(self.tabWidget)
        self.close()

        self.retranslateUi(parent)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(parent)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.broadcastBtn.setText(_translate("Form", "Broadcast"))
        self.refreshBtn.setText(_translate("Form", "Refresh"))
        item = self.tabel_conn.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Line"))
        item = self.tabel_conn.horizontalHeaderItem(1)
        item.setText(_translate("Form", "IP"))
        item = self.tabel_conn.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Status"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_broadcast), _translate("Form", "Broadcast"))
        self.updateBtn.setText(_translate("Form", "Update"))
        self.refresh.setText(_translate("Form", "Refresh"))
        self.label_line.setText(_translate("Form", "Line"))
        self.hapusBtn.setText(_translate("Form", "Hapus"))
        self.label_ip.setText(_translate("Form", "IP"))
        item = self.tabel_ip.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Line"))
        item = self.tabel_ip.horizontalHeaderItem(1)
        item.setText(_translate("Form", "IP"))
        item = self.tabel_ip.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Status"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_konektivitas), _translate("Form", "Konektivitas"))
        self.label.setText(_translate("Form", "Input Ads"))
        self.img.setText(_translate("Form", "ads"))
        item = self.file_list.horizontalHeaderItem(0)
        item.setText(_translate("Form", "File"))
        self.browseBtn.setText(_translate("Form", "Browse"))
        self.kirimAds.setText(_translate("Form", "Send Ads"))
        self.hapusBtn_2.setText(_translate("Form", "Hapus"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_ads), _translate("Form", "Ads slide"))

    def BroadcastButton(self):
        if self.state is True:
            self.broadcastBtn.setStyleSheet("QPushButton {\n"
                                     "    background: #ffff00;\n"
                                     "    border-radius: 6px;\n"
                                     "    border: none;\n"
                                     "    color: white;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:pressed {\n"
                                     "    background: white;\n"
                                     "    color: #2962ff;\n"
                                     "    border: 2px solid #2962ff;\n"
                                     "}")
            setmessage = '#2,1*'
            self.statusBC = "Clear!"
            self.state = False
        else:
            self.broadcastBtn.setStyleSheet("QPushButton {\n"
                                     "    background: #00ff00;\n"
                                     "    border-radius: 6px;\n"
                                     "    border: none;\n"
                                     "    color: white;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:pressed {\n"
                                     "    background: white;\n"
                                     "    color: #2962ff;\n"
                                     "    border: 2px solid #2962ff;\n"
                                     "}")
            setmessage = '#2,0*'
            self.statusBC = "Set"
            self.state = True
        
        IPlist = self.parent.mysql.select("ipAddress", "IPline", True, "id ASC")
        for data in IPlist:
            for setip in data:
                self.sendBroadcast(setip, setmessage)

    def sendBroadcast(self, setip, setmessage):
        getip = self.parent.socketThread.get_ip
        for myip in getip:
            addr,conn = myip
            if addr == setip:
                getconn = conn
                send = True
                break
            send = False

        if send == True:
            getconn.send(bytes(setmessage + "\r\n", 'UTF-8'))
            self.getConnected()
        else : 
            send = False

    def show(self):
        self.displayInfo.show()

    def close(self):
        self.displayInfo.close()

    def deleteList(self):
        val = "ipAddress = \"{}\",line = \"{}\""
        val = val.format("", self.line.currentText())
        key = "line = \"{}\""
        ID = self.line.currentText()
        key = key.format(ID)
        err = self.parent.mysql.update("IPline", val, key)
        if err:
            self.parent.showDialog("warning", "Query Error", str(err.msg))
            return
        self.ip.clear()
        self.getList()

    def selectList(self):
        self.updateBtn.setText("Update")
        row = self.tabel_ip.currentRow()
        getline = self.line.findText(self.tabel_ip.item(row, 0).text())
        self.line.setCurrentIndex(getline)
        self.ip.setText(self.tabel_ip.item(row, 1).text())

    def editText(self):
        masterKey = Keypad(self.parent, 15)
        masterKey.show()
        self.ip.setText(masterKey.val)

    def UpdateList(self):
        self.editText()
        if (self.ip.text() or self.line.currentText()) is "":
            self.parent.showDialog("warning", "Tolong isi form",
                            "Pastikan setiap form telah terisi")
            return

        val = "ipAddress = \"{}\",line = \"{}\""
        val = val.format(self.ip.text(), self.line.currentText())
        key = "line = \"{}\""
        ID = self.line.currentText()
        key = key.format(ID)
        err = self.parent.mysql.update("IPline", val, key)
        if err:
            self.parent.showDialog("warning", "Query Error", str(err.msg))
            return
        self.getList()

        self.ip.clear()
        self.deselect()

    def deselect(self):
        if not self.line.hasFocus() and not self.ip.hasFocus():
            self.tabel_ip.clearSelection()
            self.ip.clear()
            self.current = None
            
    
    def findLineIp(self,i):
        getLine = self.line.itemText(i)
        IPlist = self.parent.mysql.select("line,ipAddress", "IPline", True, "id ASC")
        row = 0
        getIP = None
        for data in IPlist:
            col = 0
            for val in data:
                if col == 0:
                    if getLine == val:
                        col = col + 1
                elif col == 1:
                    getIP = val
            row = row + 1
        if getIP == None:
            self.ip.setText("")
        else:
            self.ip.setText(getIP)
            
    def getList(self):
        IPlist = self.parent.mysql.select(
            "line,ipAddress", "IPline", True, "id ASC")
        self.tabel_ip.setRowCount(len(IPlist))
        row = 0
        for data in IPlist:
            col = 0
            for val in data:
                self.tabel_ip.setItem(row, col, QtWidgets.QTableWidgetItem(val))
                col = col + 1
            row = row + 1
        # self.tabel_ip.setUpdatesEnabled(False)
        # self.tabel_ip.setUpdatesEnabled(True)

    def refreshPing(self):
        if self.parent.refreshPingisDone == True:
            self.parent.refreshPingisDone = False
            self.listIPConnected = []
            self.ping = Thread(target=self.pingList, args=())
            self.ping.daemon = True
            self.ping.start()
        else:
            self.parent.showDialog("warning", "Process","Proses Cek Koneksi belum selesai!")

    def pingList(self):
        IPlist = self.parent.mysql.select("ipAddress", "IPline", True, "id ASC")
        row = 0

        ro = 0
        # self.tabel_ip.setUpdatesEnabled(False)
        for data in IPlist:
            self.tabel_ip.setItem(ro, 2, QtWidgets.QTableWidgetItem("ready to check."))
            ro = ro+1
        # self.tabel_ip.setUpdatesEnabled(True)
        
        for data in IPlist:
            for ip in data:
                param = '-n' if platform.system().lower()=='windows' else '-c'
                command = ['ping', param, '1', ip]
                # self.tabel_ip.setUpdatesEnabled(False)
                self.tabel_ip.setItem(row, 2, QtWidgets.QTableWidgetItem('checking...'))
                # self.tabel_ip.setUpdatesEnabled(True)
                if subprocess.call(command) == 0 and not ip == '':
                    status = 'Connected'
                    val = "available = {}"
                    val = val.format(False)
                    key = "ipAddress = \"{}\""
                    key = key.format(ip)
                    err = self.parent.mysql.update("IPline", val, key)
                    self.listIPConnected.append(ip)
                else:
                    status = 'Disconnected'
                    val = "available = {}"
                    val = val.format(False)
                    key = "ipAddress = \"{}\""
                    key = key.format(ip)
                # self.tabel_ip.setUpdatesEnabled(False)
                self.tabel_ip.setItem(row, 2, QtWidgets.QTableWidgetItem(status))
                # self.tabel_ip.setUpdatesEnabled(True)
            row = row+1
        self.parent.refreshPingisDone = True
        self.parent.transaksi.availableLine()
    
    def getConnected(self):
        if self.parent.refreshPingisDone == True:
            IPlist = self.parent.mysql.select("ipAddress,line", "IPline", True, "id ASC")
            self.tabel_conn.setRowCount(len(self.listIPConnected))
            getip = self.parent.socketThread.get_ip
            statip = self.parent.socketThread.getreturn
            row = 0

            for myip in getip:
                addr,conn = myip
                for listip in self.listIPConnected:
                    if addr == listip:
                        for data in IPlist:
                            col = 1
                            for ip in data:
                                if col == 1:
                                    if listip == ip:
                                        self.tabel_conn.setItem(row, col, QtWidgets.QTableWidgetItem(ip))
                                        val = "available = {}"
                                        val = val.format(True)
                                        key = "ipAddress = \"{}\""
                                        print(ip)
                                        key = key.format(ip)
                                        err = self.parent.mysql.update("IPline", val, key)
                                        for statusIP in statip:
                                            mip,stat = statusIP
                                            if mip == ip:
                                                if stat == True:
                                                    self.status = self.statusBC
                                                else:
                                                    self.status = "Set"

                                        col = col - 1
                                    else:
                                        col = col
                                elif col == 0:
                                    self.tabel_conn.setItem(row, col, QtWidgets.QTableWidgetItem(ip))
                                    self.tabel_conn.setItem(row, 2, QtWidgets.QTableWidgetItem(self.status))
                                    row = row + 1
                    else:
                        for data in IPlist:
                            col = 1
                            for ip in data:
                                if col == 1:
                                    self.tabel_conn.setItem(row, col, QtWidgets.QTableWidgetItem(""))
                                    col = col - 1
                                elif col == 0:
                                    self.tabel_conn.setItem(row, col, QtWidgets.QTableWidgetItem(""))
                                    self.tabel_conn.setItem(row, 2, QtWidgets.QTableWidgetItem(""))
        else:
            self.parent.showDialog("warning", "Process","Proses Cek Koneksi belum selesai!")

        self.parent.transaksi.availableLine()
        
    def createList(self):
        lineList = self.parent.mysql.select("line", "IPline", True, "id ASC")

        self.ro = 1
        # self.tabel_ip.setUpdatesEnabled(False)
        for data in lineList:
            mline = "Line " + str(self.ro)
            self.line.addItem(mline)
            self.ro = self.ro+1
        # self.tabel_ip.setUpdatesEnabled(True)

    def uploadImage(self):
        browse = QtWidgets.QFileDialog(self.parent)
        browse.setFileMode(browse.ExistingFile)
        path = browse.getOpenFileName(self.parent,"Browser Image",QtCore.QDir.currentPath(), "Image File(PNG,JPG,JPEG) (*.jpg *.jpeg *.png)")
        self.filePath = path[0]
        img = QtGui.QPixmap(self.filePath)
        self.img.setPixmap(img.scaled(300,400,QtCore.Qt.KeepAspectRatio))

        pathdir = QtCore.QDir.currentPath()
        pathdir = pathdir + "/Module/static/" + str(self.endData + 1) + ".jpg"

        with open(self.filePath, 'rb') as f:
            data = f.read()

        with open(pathdir, 'wb') as f:
            f.write(data)

        val = "{}"
        val = val.format(self.endData + 1)
        err = self.parent.mysql.insertTo("ads", "image_id", val)
        self.getAds()

    def getAds(self):
        self.endData = 0
        ads = self.parent.mysql.select(
            "image_id", "ads", True, "id ASC")
        self.file_list.setRowCount(len(ads))
        row = 0
        for data in ads:
            col = 0
            for val in data:
                ads = "Iklan " + str(val)
                self.file_list.setItem(row, col, QtWidgets.QTableWidgetItem(ads))
                self.endData = val
            row = row + 1
        # self.file_list.setUpdatesEnabled(False)
        # self.file_list.setUpdatesEnabled(True)

    def selectFile(self):
        row = self.file_list.currentRow()
        self.lineEdit.setText(self.file_list.item(row, 0).text())
        id = self.lineEdit.text()
        image_id = id[6:]

        pathdir = QtCore.QDir.currentPath()
        pathdir = pathdir + "/Module/static/" + image_id + ".jpg"
        img = QtGui.QPixmap(pathdir)
        print(img)
        self.img.setPixmap(img.scaled(300,400,QtCore.Qt.KeepAspectRatio))

    def deleteAds(self):

        row = self.file_list.currentRow()
        self.lineEdit.setText(self.file_list.item(row, 0).text())
        id = self.lineEdit.text()
        image_id = int(id[6:])

        key = "image_id = {}"
        self.parent.mysql.delete("ads", key.format(image_id))
        self.lineEdit.clear()
        self.getAds()

    def sendAds(self):
        setmessage = "#3,"
        getval = ""
        ads = self.parent.mysql.select(
            "image_id", "ads", True, "id ASC")
        row = 0
        for data in ads:
            col = 0
            for val in data:
                getval = getval + "," + str(val) 
            row = row + 1

        setmessage = setmessage + str(row) + getval + "*"

        print(setmessage)
        
        IPlist = self.parent.mysql.select("ipAddress", "IPline", True, "id ASC")
        for data in IPlist:
            for setip in data:
                self.sendBroadcast(setip, setmessage)


        


    
