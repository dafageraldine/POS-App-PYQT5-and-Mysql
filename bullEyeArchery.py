from PyQt5 import QtWidgets, uic, QtGui, QtCore
from Module.webservice import app as application
from Module.daftar_pengeluaran import *
from Module.display_informasi import *
from Module.daftar_transaksi import *
from Module.rekap_transaksi import *
from Module.stock_produk import *
from Module.pelanggan import *
from Module.transaksi import *
from Module.Setting import *
from Module.diskon import *
from Module.login import *
from Module.sql import *
from Module.qty import *
from time import sleep
from threading import *
import shutil
import socket
import sys

class Ui(QtWidgets.QWidget):
    
    mysql = db('localhost', 'root', '12345678', 'bullEyeArchery')

    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('inputProduk.ui', self)
        self.widget = self.findChild(QtWidgets.QHBoxLayout, 'horizontalLayout')
        self.filePath = None

        self.socketThread = Websocket()
        self.socketThread.start()

        #ditambahkan untuk webservice
        self.serviceThread = Webservice()
        self.serviceThread.start()

        self.daftar_pengeluaran = DaftarPengeluaran(self)
        self.daftar_transaksi = DaftarTransaksi(self)
        self.rekap_transaksi = RekapTransaksi(self)
        self.displayInfo = DisplayInfo(self)
        self.pelanggan = Pelanggan(self)
        self.transaksi = Transaksi(self)
        self.Setting = Settings(self)
        self.login = Login(self)
        self.stock = Stock(self)

        self.widget.addWidget(self.daftar_pengeluaran.daftarPengeluaranWidget)
        self.widget.addWidget(self.rekap_transaksi.rekapTransaksiWidget)
        self.widget.addWidget(self.daftar_transaksi.daftarTransaksiWidget)
        self.widget.addWidget(self.displayInfo.displayInfo)
        self.widget.addWidget(self.pelanggan.pelangganWidget)
        self.widget.addWidget(self.transaksi.transaksiWidget)
        self.widget.addWidget(self.Setting.settingWidget)
        self.widget.addWidget(self.stock.stockWidget)

        self.menu = self.findChild(QtWidgets.QListView, 'sideMenu')
        self.menu.item(3).setFlags(QtCore.Qt.NoItemFlags)
        self.menu.item(8).setFlags(QtCore.Qt.NoItemFlags)
        self.menu.itemClicked.connect(self.navigation)
        self.menu.setCurrentRow(0)
        self.navigation()

        self.label_login = self.findChild(QtWidgets.QLabel, 'login_label')

        self.img2 = self.menu.item(0)
        ic_tra = QtGui.QIcon()
        ic_tra.addPixmap(QtGui.QPixmap("icon_Transaksi.png"))
        self.img2.setIcon(ic_tra)

        self.img3 = self.menu.item(1)
        ic_pel = QtGui.QIcon()
        ic_pel.addPixmap(QtGui.QPixmap("icon_Pelanggan.png"))
        self.img3.setIcon(ic_pel)

        self.img4 = self.menu.item(2)
        ic_pro = QtGui.QIcon()
        ic_pro.addPixmap(QtGui.QPixmap("icon_Produk.png"))
        self.img4.setIcon(ic_pro)

        self.img5 = self.menu.item(4)
        ic_repro = QtGui.QIcon()
        ic_repro.addPixmap(QtGui.QPixmap("icon_Stock Produk.png"))
        self.img5.setIcon(ic_repro)

        self.img6 = self.menu.item(5)
        ic_DT = QtGui.QIcon()
        ic_DT.addPixmap(QtGui.QPixmap("icon_Daftar Transaksi.png"))
        self.img6.setIcon(ic_DT)

        self.img7 = self.menu.item(6)
        ic_DP = QtGui.QIcon()
        ic_DP.addPixmap(QtGui.QPixmap("icon_Pengeluaran.png"))
        self.img7.setIcon(ic_DP)

        self.img8 = self.menu.item(7)
        ic_RT = QtGui.QIcon()
        ic_RT.addPixmap(QtGui.QPixmap("icon_Rekap Transaksi.png"))
        self.img8.setIcon(ic_RT)

        self.img9 = self.menu.item(9)
        ic_DI = QtGui.QIcon()
        ic_DI.addPixmap(QtGui.QPixmap("icon_Display Informasi.png"))
        self.img9.setIcon(ic_DI)

        self.img10 = self.menu.item(10)
        ic_S = QtGui.QIcon()
        ic_S.addPixmap(QtGui.QPixmap("icon_Pengaturan.png"))
        self.img10.setIcon(ic_S)

        self.input = self.findChild(QtWidgets.QPushButton, 'inputProduk')
        self.input.clicked.connect(self.updateProduct)
        self.delete = self.findChild(QtWidgets.QPushButton, 'hapusProduk')
        self.delete.clicked.connect(self.deleteProduct)
        self.delete.hide()

        cari = self.findChild(QtWidgets.QPushButton, 'cariBtn')
        cari.clicked.connect(self.findProduct)

        self.form_cari = self.findChild(QtWidgets.QLineEdit, 'pencarian')
        self.form_cari.textChanged.connect(self.findProduct)

        self.id = self.findChild(QtWidgets.QLineEdit, 'id_produk')
        self.nama = self.findChild(QtWidgets.QLineEdit, 'nama_produk')
        self.harga = self.findChild(QtWidgets.QLineEdit, 'harga_produk')
        self.kategori = self.findChild(QtWidgets.QComboBox, 'kategori_produk')
        self.hpp = self.findChild(QtWidgets.QLineEdit, 'hpp_produk')
        self.hpp_label = self.findChild(QtWidgets.QLabel, 'label_hpp')

        self.exit = self.findChild(QtWidgets.QPushButton, 'exitBtn')
        self.exit.clicked.connect(self.quitApplication)

        self.id.setReadOnly(True)
        self.nama.setReadOnly(True)
        self.harga.setReadOnly(True)
        self.hpp.hide()
        self.hpp_label.hide()

        self.tabelProduk = self.findChild(
            QtWidgets.QTableWidget, 'tabelProduk')
        header = self.tabelProduk.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tabelProduk.itemClicked.connect(self.selectProduct)
        self.tabelProduk.itemDoubleClicked.connect(self.addToChart)

        self.img = self.findChild(QtWidgets.QLabel, 'img')
        img = QtGui.QPixmap("placeholder.jpg")
        self.img.setPixmap(img.scaled(300,400,QtCore.Qt.KeepAspectRatio))

        self.upload = self.findChild(QtWidgets.QPushButton, "uploadBtn")
        self.upload.clicked.connect(self.uploadImage)

        self.getProduct()
        self.displayInfo.getList()
        self.displayInfo.getAds()
        self.refreshPingisDone = True
        self.displayInfo.refreshPing()

    def mousePressEvent(self, event):
        self.deselect()

    def addToChart(self):
        qty = Quantity(self)
        qty.show()
        if qty.jumlah is None or qty.jumlah is "":
            return
        jumlah = qty.jumlah
        row = self.transaksi.tabelTransaksi.rowCount()
        selected = self.tabelProduk.selectedItems()
        r = 0
        exist = False
        while r < row:
            idproduk = self.transaksi.tabelTransaksi.item(r, 0).text()
            if idproduk == selected[0].text():
                row = r
                exist = True
                break
            r = r + 1
        if not exist:
            self.transaksi.tabelTransaksi.insertRow(row)
        else:
            jumlah = int(qty.jumlah) + int(self.transaksi.tabelTransaksi.item(row, 3).text())

        diskon = selected[4].text()

        self.transaksi.tabelTransaksi.setItem(row,0,QtWidgets.QTableWidgetItem(self.id.text()))
        self.transaksi.tabelTransaksi.setItem(row,1,QtWidgets.QTableWidgetItem(self.nama.text()))
        self.transaksi.tabelTransaksi.setItem(row,2,QtWidgets.QTableWidgetItem(self.harga.text()))
        self.transaksi.tabelTransaksi.setItem(row,3,QtWidgets.QTableWidgetItem(str(jumlah)))
        self.transaksi.tabelTransaksi.setItem(row,4,QtWidgets.QTableWidgetItem(diskon))

        harga = int(self.harga.text())
        total = int((harga - (harga*(int(diskon)/100))) * int(jumlah))
        self.transaksi.tabelTransaksi.setItem(row,5,QtWidgets.QTableWidgetItem(str(total)))

    def deselect(self):
        if not self.id.hasFocus() and not self.nama.hasFocus() and not self.harga.hasFocus() and not self.hpp.hasFocus():
            self.tabelProduk.clearSelection()
            self.filePath = None
            self.input.setText("Tambah Produk")
            img = QtGui.QPixmap("placeholder.jpg")
            self.img.setPixmap(img.scaled(300,400,QtCore.Qt.KeepAspectRatio))
            if not self.login.isLogin:
                self.input.setText("Login")

    def findProduct(self):
        listProduk = self.mysql.find(
            "idProduk,nama,kategori,harga", "daftarbarang",
            "idProduk", self.form_cari.text(), True,
            "idProduk ASC")
        if len(listProduk) < 1:
            listProduk = self.mysql.find(
                "idProduk,nama,kategori,harga", "daftarbarang",
                "nama", self.form_cari.text(), True,
                "idProduk ASC")
        self.tabelProduk.setRowCount(len(listProduk))
        row = 0
        for data in listProduk:
            col = 0
            for val in data:
                if col is 3:
                    val = "Rp " + str(val)
                self.tabelProduk.setItem(
                    row, col, QtWidgets.QTableWidgetItem(val))
                col = col + 1
            row = row + 1

    def auth(self):
        self.login.show()
        if self.login.isLogin:
            self.label_login.hide()
            self.id.setReadOnly(False)
            self.id.setFocus()
            self.nama.setReadOnly(False)
            self.harga.setReadOnly(False)
            self.hpp.show()
            self.hpp_label.show()
            self.delete.show()
            current = self.tabelProduk.currentItem()
            if current == None or not current.isSelected():
                self.input.setText("Tambah Produk")
            elif current.isSelected():
                self.input.setText("Simpan Produk")

    def updateProduct(self):
        if not self.login.isLogin:
            self.auth()
            return

        if (self.id.text() or self.nama.text() or self.harga.text() or self.hpp.text()) is "":
            self.showDialog("warning", "Tolong isi form",
                            "Pastikan setiap form telah terisi")
            return
        elif self.filePath is None:
            self.showDialog("warning", "Tambahkan foto produk",
                            "Harap tambahkan foto produk")
            return

        current = self.tabelProduk.currentItem()

        if current == None or not current.isSelected():
            key = "idProduk = \"{}\" OR nama = \"{}\""
            key = key.format(self.id.text(), self.nama.text())
            check = self.mysql.findCol("idProduk, nama", "daftarbarang", key, False)
            if check is not None and len(check) > 0:
                self.showDialog("warning", "Gagal menambah produk", "ID atau Nama produk yang ditambahkan sudah terpakai")
                return
            destination = QtCore.QDir.currentPath() + "/Module/static/" + self.id.text() + ".jpeg"
            val = "\"{}\",\"{}\",{},\"{}\",{},\"{}\""
            val = val.format(self.id.text(), self.nama.text(), self.harga.text(),
                             self.kategori.currentText(), self.hpp.text(), destination)
            err = self.mysql.insertTo(
                "daftarbarang", "idProduk,nama,harga,kategori,hpp,foto", val)
            if err:
                self.showDialog("warning", "Query Error", str(err.msg))
                return
            shutil.copyfile(self.filePath, destination)
            self.getProduct()
            self.showDialog("information", "Success",
                            "Berhasil menambahkan item")
        elif current.isSelected():
            destination = QtCore.QDir.currentPath() + "/Module/static/" + self.id.text() + ".jpeg"
            val = "idProduk = \"{}\",nama = \"{}\",harga = {},kategori = \"{}\",hpp = {}, foto = \"{}\""
            val = val.format(self.id.text(), self.nama.text(), self.harga.text(),
                             self.kategori.currentText(), self.hpp.text(), destination)
            key = "idProduk = \"{}\""
            ID = self.tabelProduk.selectedItems()
            key = key.format(ID[0].text())
            err = self.mysql.update("daftarbarang", val, key)
            if err:
                self.showDialog("warning", "Query Error", str(err.msg))
                return
            shutil.copyfile(self.filePath, destination)
            self.getProduct()
            self.showDialog("information", "Success",
                            "Berhasil melakukan perubahan")

        self.harga.clear()
        self.nama.clear()
        self.hpp.clear()
        self.id.clear()
        self.deselect()

    def uploadImage(self):
        if not self.login.isLogin:
            self.auth()
            return

        browse = QtWidgets.QFileDialog(self)
        browse.setFileMode(browse.ExistingFile)
        path = browse.getOpenFileName(self, "Browser Image", QtCore.QDir.currentPath(), "Image File(PNG,JPG,JPEG) (*.jpg *.jpeg *.png)")
        self.filePath = path[0]
        img = QtGui.QPixmap(self.filePath)
        self.img.setPixmap(img.scaled(300,400,QtCore.Qt.KeepAspectRatio))

    def selectProduct(self):
        if self.login.isLogin:
            self.input.setText("Simpan Produk")
        row = self.tabelProduk.currentRow()
        self.id.setText(self.tabelProduk.item(row, 0).text())
        self.nama.setText(self.tabelProduk.item(row, 1).text())
        v = self.kategori.findText(self.tabelProduk.item(row, 2).text())
        self.kategori.setCurrentIndex(v)
        data = self.mysql.find("hpp,foto","daftarbarang","idProduk",self.tabelProduk.item(row, 0).text(),False)
        self.hpp.setText(str(data[0]))
        harga = self.tabelProduk.item(row, 3).text()
        self.harga.setText(harga[2:].strip())
        img = QtGui.QPixmap(data[1])
        self.filePath = data[1]

        if data[1] is None:
            img = QtGui.QPixmap("placeholder.jpg")
        self.img.setPixmap(img.scaled(300,400,QtCore.Qt.KeepAspectRatio))

        if self.tabelProduk.currentColumn() == 4:
            if not self.login.isLogin:
                self.auth()
                return
            diskon = Diskon(self)
            diskon.show()
            val = "diskon = {}"
            val = val.format(int(diskon.val))
            key = "idProduk = \"{}\""
            key = key.format(self.tabelProduk.item(row, 0).text())
            self.mysql.update("daftarbarang",val,key)
            self.tabelProduk.item(row, 4).setText(diskon.val)

    def getProduct(self):
        listProduk = self.mysql.select(
            "idProduk,nama,kategori,harga,diskon", "daftarbarang", True, "idProduk ASC")
        self.tabelProduk.setRowCount(len(listProduk))
        row = 0
        for data in listProduk:
            col = 0
            for val in data:
                val = str(val)
                if col is 3:
                    val = "Rp " + val
                self.tabelProduk.setItem(
                    row, col, QtWidgets.QTableWidgetItem(val))
                col = col + 1
            row = row + 1

    def deleteProduct(self):
        i = 0
        ID = self.tabelProduk.selectedItems()
        if len(ID) < 1:
            self.showDialog("warning", "Informasi",
                            "Tolong pilih produk yang hendak dihapus")
            return
        prompt = self.showDialog(
            "question", "Hapus Produk", "Apakah anda ingin menghapus produk?")
        if prompt == QtWidgets.QMessageBox.Yes:
            for col in ID:
                if i is 0 or i % 5 is 0:
                    key = "idProduk = \"{}\""
                    self.mysql.delete("daftarbarang", key.format(col.text()))

                i = i+1
            self.getProduct()

    def showDialog(self, msgType: str, title: str, message: str, action1=None, action2=None):
        msgBox = QtWidgets.QMessageBox()
        if msgType is "critical":
            msgBox.critical(self, title, message)
        elif msgType is "warning":
            msgBox.warning(self, title, message)
        elif msgType is "information":
            msgBox.information(self, title, message)
        elif msgType is "question":
            return msgBox.question(self, title, message)
    
    def closeEvent(self, event):
        prompt = self.showDialog("question", "Keluar dari aplikasi", "Apakah ingin keluar dari aplikasi?")
        if prompt == QtWidgets.QMessageBox.No:
            event.ignore()

    def quitApplication(self):
        self.close()


    def navigation(self):
        section = self.findChild(QtWidgets.QWidget, "productWidget")

        if self.menu.currentRow() == 0:
            self.transaksi.show()
            self.transaksi.undo()
            self.transaksi.count()
        else:
            self.transaksi.transaksiWidget.close()
        if self.menu.currentRow() == 1:
            self.pelanggan.show()
            self.pelanggan.getProduct()
            self.pelanggan.change()
        else:
            self.pelanggan.close()
        if self.menu.currentRow() == 2:
            section.show()
        else:
            section.close()
        if self.menu.currentRow() == 4:
            self.stock.show()
        else:
            self.stock.close()
        if self.menu.currentRow() == 5:
            self.daftar_transaksi.show()
        else:
            self.daftar_transaksi.close()
        if self.menu.currentRow() == 6:
            self.daftar_pengeluaran.show()
        else:
            self.daftar_pengeluaran.close()
        if self.menu.currentRow() == 7:
            self.rekap_transaksi.show()
        else:
            self.rekap_transaksi.close()
        if self.menu.currentRow() == 9:
            self.displayInfo.show()
        else:
            self.displayInfo.close()
        if self.menu.currentRow() == 10:
            self.Setting.show()
        else:
            self.Setting.close()

        self.stock.getStock("get")
        self.getProduct()

#Line Webservice
class Webservice(QtCore.QThread):
    def __init__(self, parent=None):
        super(Webservice, self).__init__(parent=parent)

    def run(self):
        application.run(host='0.0.0.0',debug=False)
 
class Websocket(QtCore.QThread):
    def __init__(self,parent = None):
        super(Websocket, self).__init__(parent)
        host = ''
        port = 8080
        w, h = 2, 1000
        self.get_ip = [[0 for x in range(w)] for y in range(h)] 
        self.getreturn = [[0 for x in range(w)] for y in range(h)] 
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind((host,port))
        self.s.listen(1000)
        print("Server Started!")

        self.createconn = Thread(target = self.get_connection, args=())
        self.createconn.daemon = True
        self.createconn.start()

    def get_connection(self):
        i = 0
        while 1:
            conn, addr = self.s.accept() #Ketika terdapat koneksi server menerima client
            ip, port = addr
            self.get_ip[i][0] = ip
            self.get_ip[i][1] = conn
            print("Server: Got connection from ", addr)
            print(addr)
            self.startclient = Thread(target = self.clientthread, args=(conn,i ))
            self.startclient.daemon = True
            self.startclient.start()
            i = i+1

    def clientthread(self, conn, i):
        self.getreturn[i][0] = self.get_ip[i][0]
        self.getreturn[i][1] = False
        while True:
            data = conn.recv(1024)
            print("Get Data from connection")
            data =  data.decode('utf-8')
            print(data)
            if data == '':
                break
            else:
                self.getreturn[i][0] = self.get_ip[i][0]
                self.getreturn[i][1] = True
            
        self.get_ip[i][0] = None
        self.get_ip[i][1] = None
        self.getreturn[i][0] = None
        self.getreturn[i][1] = None
        conn.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    app.exec_()
