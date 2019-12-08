import sys, json,barcode,random,cv2,pymysql
import numpy as np
from PyQt5 import QtWidgets, uic, QtGui, QtCore, QtNetwork
from PyQt5.QtWidgets import (QLineEdit,QWidget,QApplication,QMessageBox,QLabel,QComboBox)
from Module.sql import *
from datetime import datetime
from barcode.writer import ImageWriter

class Ui(QtWidgets.QWidget):
    pelanggan = MySQL("localhost", "root", "1234", "inputpelanggan")

    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('pelanggan.ui', self)

        getBtn = self.findChild(QtWidgets.QPushButton, 'getBtn')
        updateBtn = self.findChild(QtWidgets.QPushButton, 'updateBtn')
        self.form_id = self.findChild(QtWidgets.QLineEdit, 'form_id')
        self.form_nama = self.findChild(QtWidgets.QLineEdit, 'form_nama')
        self.form_alamat = self.findChild(QtWidgets.QLineEdit, 'form_alamat')
        self.form_kontak = self.findChild(QtWidgets.QLineEdit, 'form_kontak')
        self.nama = self.findChild(QtWidgets.QLineEdit, 'nama')
        self.alamat = self.findChild(QtWidgets.QLineEdit,'alamat')
        self.hp = self.findChild(QtWidgets.QLineEdit,'hp')
        self.score = self.findChild(QtWidgets.QLineEdit,'score')
        self.score.setEnabled(False)
        self.pria = self.findChild(QtWidgets.QRadioButton,' pria')
        self.wanita = self.findChild(QtWidgets.QRadioButton,'wanita')

        self.img = self.findChild(QtWidgets.QLabel,'label_11')

        self.inputr = self.findChild(QtWidgets.QPushButton, 'input')
        self.inputr.clicked.connect(self.flag)
        self.inputr.setEnabled(False)

        self.inputpk = self.findChild(QtWidgets.QPushButton,'inputpk')
        self.inputpk.setEnabled(False)
        self.inputpk.clicked.connect(self.flag2)

        self.ambilgambar = self.findChild(QtWidgets.QPushButton,'ambilgambar')
        self.ambilgambar.clicked.connect(self.takephoto)

        self.pk = self.findChild(QtWidgets.QPushButton,'pk')
        self.pk.clicked.connect(self.settings)

        self.ambilgambarpk = self.findChild(QtWidgets.QPushButton,'ambilgambarpk')
        self.ambilgambarpk.clicked.connect(self.takephoto2)
        self.ambilgambarpk.setEnabled(False)

        getBtn.clicked.connect(self.getData)
        updateBtn.clicked.connect(self.updateData)

        self.show()

    def takephoto(self):
        window =  QtWidgets.QMessageBox()
        window.setWindowTitle("success")
        window.setText("Foto Berhasil Disimpan")
        cap = cv2.VideoCapture(0)
        global c
        while True:
            check,frame = cap.read()
            cv2.imshow("camera",frame)
            cv2.namedWindow('camera',cv2.WINDOW_NORMAL)
            cv2.resizeWindow("camera",640,480)
            key = cv2.waitKey(1)
            if key == ord('q'):
                c = c+1
                filename = "user" + str(c) + ".jpg"
                cv2.imwrite(filename,frame)
                break
        cap.release()
        cv2.destroyAllWindows()
        image = QtGui.QPixmap(filename)
        self.img.setPixmap(image)
        window.exec_()
        self.inputr.setEnabled(True)

    def takephoto2(self):
        window =  QtWidgets.QMessageBox()
        window.setWindowTitle("success")
        window.setText("Foto Berhasil Disimpan")
        cap = cv2.VideoCapture(0)
        global c
        while True:
            check,frame = cap.read()
            cv2.imshow("camera",frame)
            cv2.namedWindow('camera',cv2.WINDOW_NORMAL)
            cv2.resizeWindow("camera",300,260)
            key = cv2.waitKey(1)
            if key == ord('q'):
                c = c+1
                filename = "user" + str(c) + ".jpg"
                cv2.imwrite(filename,frame)
                break
        cap.release()
        cv2.destroyAllWindows()
        image = QtGui.QPixmap(filename)
        self.img.setPixmap(image)
        window.exec_()
        self.inputpk.setEnabled(True)

    def flag(self):
        nama = self.nama.text()
        alamat = self.alamat.text()
        hp = self.hp.text()
        if(nama == "" or alamat =="" or hp ==""):
            self.tryagain()
        else:
            self.register()

    def flag2(self):
        nama = self.nama.text()
        alamat = self.alamat.text()
        hp = self.hp.text()
        score = self.score.text()
        if(nama == "" or alamat =="" or hp =="" or score == ""):
            self.tryagain()
        else:
            self.register2()

    def tryagain(self):
        win = QtWidgets.QMessageBox()
        win.setWindowTitle("GAGAL")
        win.setText("Data Tidak Boleh Kosong")
        win.setStandardButtons(QtWidgets.QMessageBox.Ok)
        win.exec_()

    def settings(self):
        self.score.setEnabled(True)
        self.ambilgambar.setEnabled(False)
        self.ambilgambarpk.setEnabled(True)

    def register(self):
        nama = self.nama.text()
        alamat = self.alamat.text()
        hp = self.hp.text()
        now = datetime.now()
        Saldo = 0
        score = 0
        global d

        bar = self.pelanggan.select("ID", "register", True)
        bar = '{:04d}'.format(len(bar)+1)
        bar = "BEA-" + str(bar)
        EAN = barcode.get_barcode_class('code39')
        ean = EAN(str(bar),writer=ImageWriter())
        d = d+1
        png = "barcode" + str(d)
        ean.save(png)

        time = now.strftime("%d/%m/%Y %H:%M:%S")
        data = "\"{}\",\"{}\",{},\"{}\",{},{},\"{}\""
        data = data.format(nama,alamat,hp,time,Saldo,score,bar)
        self.pelanggan.insertTo("register", "nama,alamat,hp,Time,saldo,score,bar", data)
        # conn.commit()
        if (data):
            self.messagebox("success","data berhasil di input")
            self.nama.clear()
            self.alamat.clear()
            self.hp.clear()
            self.img.clear()
            self.inputr.setEnabled(False)

    def register2(self):
        nama = self.nama.text()
        alamat = self.alamat.text()
        hp = self.hp.text()
        now = datetime.now()
        Saldo = 0
        score = self.score.text()
        
        global d
        bar = random.randrange(1,10000000000000)
        EAN = barcode.get_barcode_class('ean13')
        ean = EAN(str(bar),writer=ImageWriter())
        d = d+1
        png = "barcode" + str(d)
        ean.save(png)

        time = now.strftime("%d/%m/%Y %H:%M:%S")
        conn = pymysql.connect(host="localhost",user="root",password="1234",database="inputpelanggan")
        cur = conn.cursor()
        query= ("insert into register(nama,alamat,hp,Time,Saldo,score,bar) values(,%s,%s,%s,%s,%s,%s,%s)")
        data =cur.execute(query,(nama,alamat,hp,time,Saldo,score,code))
        conn.commit()
        if (data):
            self.messagebox("success","data berhasil di input")
            self.nama.clear()
            self.alamat.clear()
            self.hp.clear()
            self.img.clear()
            self.score.clear()
            self.ambilgambarpk.setEnabled(False)
            self.ambilgambar.setEnabled(True)
            self.inputpk.setEnabled(False)

    def messagebox(self,title,message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

    def showDialog(self, msgType:str, title:str, message:str, action1 = None, action2 = None):
        msgBox = QtWidgets.QMessageBox()
        if msgType is "critical":
            msgBox.critical(self, title, message)
        elif msgType is "warning":
            msgBox.warning(self, title, message)
        elif msgType is "information":
            msgBox.information(self, title, message)
        elif msgType is "question":
            msgBox.question(self, title, message)

    def getData(self):
        # val = "\"{}\",\"{}\",\"{}\",\"{}\""
        # val = val.format(self.form_id.text(), self.form_nama.text(), self.form_alamat.text(),
        #                  self.form_kontak.text())
        self.key = "nama = \"{}\""
        self.key = self.key.format(self.form_nama.text())
        data = self.pelanggan.find("ID, nama, alamat, hp", "register", self.key, False)

        self.form_id.setText(str(data[0]))
        self.form_nama.setText(str(data[1]))
        self.form_alamat.setText(str(data[2]))
        self.form_kontak.setText(str(data[3]))
        self.doRequest()

    def doRequest(self):   
    
        url = "http://192.168.100.65:5000/api/pelanggan"
        req = QtNetwork.QNetworkRequest(QtCore.QUrl(url))
        
        self.nam = QtNetwork.QNetworkAccessManager()
        self.nam.finished.connect(self.handleResponse)
        self.nam.get(req)
             
    def handleResponse(self, reply):

        er = reply.error()
        
        if er == QtNetwork.QNetworkReply.NoError:
    
            bytes_string = reply.readAll()
            data = json.loads(str(bytes_string, 'utf-8'))
            print(data[0]['nama'])
        else:
            print(er)

    def updateData(self):
        setValue = "ID = \"{}\", nama = \"{}\", alamat = \"{}\", hp = \"{}\""
        setValue = setValue.format(self.form_id.text(), self.form_nama.text(), self.form_alamat.text(), self.form_kontak.text())
        self.pelanggan.update("register", setValue, self.key)
        self.showDialog("information", "Update Data", "Data has been updated!")

c=0
d=0
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
