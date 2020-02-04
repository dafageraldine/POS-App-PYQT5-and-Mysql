from PyQt5 import QtCore, QtGui, QtWidgets
from Module.sql import *
import os,datetime
#include baru buat printer
import win32print, win32ui, win32con
from PIL import Image, ImageWin

class Topup():
    def __init__(self, w):
        self.w = w 
        self.Dialog = QtWidgets.QDialog(w)
        self.Dialog.setWindowTitle("Top up Saldo")
        self.Dialog.resize(316, 282)
        self.price = QtWidgets.QLineEdit(self.Dialog)
        self.price.setGeometry(QtCore.QRect(50, 100, 211, 29))
        self.price.setPlaceholderText("Masukkan Nominal Top up")
        self.Btn = QtWidgets.QPushButton(self.Dialog)
        self.Btn.setGeometry(QtCore.QRect(100, 160, 101, 29))
        self.Btn.setText("Top up")
        self.Btn.clicked.connect(self.isi)
    
    def isi(self):
        cek = self.price.text()
        if cek == "":
            self.w.pelanggan.parent.showDialog("information", "Informasi","Masukkan nominal top up")
        if cek.isdigit():
            self.idt = self.w.mysql.select("id", "transaksi", False, "id DESC")
            if self.idt != None :
                self.idt = '{:09d}'.format(self.idt[0]+1)
            else:
                self.idt = '{:09d}'.format(1)
            self.idt = "PAY-" + str(self.idt)
            idp = self.w.pelanggan.ID.text()
            saldo = self.w.pelanggan.saldo.text()
            money = saldo[3:]
            lmoney = int(money) + int(self.price.text())
            val = "saldo= {}"
            val = val.format(lmoney)
            key = "idPelanggan = \"{}\""
            key = key.format(self.w.pelanggan.ID.text())
            vals = "\"{}\",{},{},\"{}\",\"{}\",\"{}\",{}"
            vals = vals.format(self.idt,cek,1,idp,self.w.pelanggan.nama.text(),"Top up",cek)
            v = vals
            v = v + ",\"TOP-UP Rp" + self.price.text() +"\""
            self.w.mysql.insertTo("transaksi","idTransaksi,harga,jumlah,idPelanggan,pelanggan,jenisTransaksi,total,produk",v)
            self.records = ["Top Up","x1",cek,cek]
            # print(self.records)
            self.tt = cek 
            self.w.mysql.update("pelanggan",val,key)
            self.print()
            self.Dialog.close()
            self.w.pelanggan.getProduct()
            self.w.pelanggan.parent.showDialog("information", "Informasi","Berhasil melakukan Top up\n sebesar Rp"+ str(self.price.text()))
            self.price.clear()
            self.w.pelanggan.img.setPixmap(self.w.pelanggan.pixmap.scaled(200, 170, QtCore.Qt.KeepAspectRatio))
            self.w.pelanggan.nama.clear()
            self.w.pelanggan.alamat.clear()
            self.w.pelanggan.hp.clear()
            self.w.pelanggan.saldo.clear()
            self.w.pelanggan.point.clear()  
            self.w.pelanggan.ID.clear()
            self.w.pelanggan.radioButton.show()
            self.w.pelanggan.radioButton_2.show()
            self.w.pelanggan.getProduct()
            self.w.pelanggan.tabelPelanggan.clearSelection()
            self.w.pelanggan.ID.hide()
            self.w.pelanggan.labelid.hide()
        else:
            self.w.pelanggan.parent.showDialog("information", "Informasi","input harus berupa angka bukan karakter")

    def show(self):
        self.Dialog.exec_()

    def print(self):
        #value
        p1= ["barang","QTY","harga","total"]

        #variable
        y=0
        x=0

        #open image
        filename = "Module/foto_pada_struck.jpeg"
        img = Image.open(filename, 'r')
        img_width = img.size[0] + 20
        img_height = img.size[1] + 20

        #create enter
        p_tampung_0 = ""
        p_tampung_3 = ""
        flag = False
        data = len(self.records[0])
        for i in range(data):
            if self.records[0][i] == " " or i == 6:
                flag = True
            if flag == True:
                p_tampung_3 += self.records[0][i]
            else:
                p_tampung_0 += self.records[0][i]
            if i == data-1:
                self.records[0] = p_tampung_0
                self.records.append(p_tampung_3)
        
        #initial print
        printer = win32ui.CreateDC()
        printer.CreatePrinterDC(win32print.GetDefaultPrinter())
        print(win32print.GetDefaultPrinter())
        printer.StartDoc("EPPSON")
        printer.StartPage ()

        #print image
        dib = ImageWin.Dib(img)
        dib.draw(printer.GetHandleOutput(), (40, y, img_width, img_height))
        y+=180

        #print tanggal
        t = datetime.datetime.now()
        date = t.strftime("%d/%m/%Y")
        time = t.strftime("%H:%M")
        tanggal = date + " " + time + " " + self.idt
        y += 50
        printer.TextOut(20,y,tanggal)
        
        #print ID pelangan
        id_p=self.w.pelanggan.nama.text() 
        list_p = "List order from " + id_p
        y += 50
        printer.TextOut(30,y,list_p)
        y +=50
  
        #print nama table
        for i in range(4):
            printer.TextOut(x,y,p1[i])
            if i == 1:
                x += 80
            else:
                x += 110
            if i == 3:
                y += 50
                x = 0

        #print data table
        for j in range(4):
            print(self.records)
            printer.TextOut(x,y,str(self.records[j]))
            if j == 0:
                x += 120
            if j == 1:
                x += 50
            if j == 2:
                x += 120
                    
            #reset variable and add if string to much
            if j == 3:
                x = 0
                if self.records[4] != "":
                    y += 30
                    printer.TextOut(x,y,str(self.records[4]))
                y += 50

        #print garis bawah
        garis_bawah = "_______________________________"
        printer.TextOut(0,y,garis_bawah)

        #print total
        total= str(self.tt)
        total_harga = "Total Harga:"
        y += 50
        printer.TextOut(0,y,total_harga)
        printer.TextOut(280,y,total)

        #finish
        printer.EndPage()
        printer.EndDoc()