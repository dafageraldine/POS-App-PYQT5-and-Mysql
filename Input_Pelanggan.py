from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QLineEdit,QWidget,QApplication,QMessageBox)
import sys,cv2,pymysql
from PyQt5.QtGui import QPixmap
import numpy as np
from datetime import datetime

class input(QWidget):
	def takephoto(self):
		window =  QtWidgets.QMessageBox()
		window.setWindowTitle("success")
		window.setText("Foto Berhasil Disimpan")
		cap = cv2.VideoCapture(1)
		global c
		global filename
		while True:
			check,frame = cap.read()
			cv2.imshow("camera",frame)
			cv2.namedWindow('camera',cv2.WINDOW_NORMAL)
			cv2.resizeWindow("camera",300,300)
			key = cv2.waitKey(1)
			if key == ord('q'):
				c = c+1
				filename = "user" + str(c) + ".jpg"
				cv2.imwrite(filename,frame)
				break
		cap.release()
		cv2.destroyAllWindows()
		window.exec_()

	def messagebox(self,title,message):
		mess = QtWidgets.QMessageBox()
		mess.setWindowTitle(title)
		mess.setText(message)
		mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
		mess.exec_()

	def flag(self):
		ID = self.ID.text()
		nama = self.nama.text()
		alamat = self.alamat.text()
		hp = self.hp.text()
		if (ID == "" or nama == "" or alamat =="" or hp ==""):
			self.tryagain()
		else:
			self.register()

	def tryagain(self):
		win = QtWidgets.QMessageBox()
		win.setWindowTitle("GAGAL")
		win.setText("Data Tidak Boleh Kosong")
		win.setStandardButtons(QtWidgets.QMessageBox.Ok)
		win.exec_()

	def register(self):
		ID = self.ID.text()
		nama = self.nama.text()
		alamat = self.alamat.text()
		hp = self.hp.text()
		now = datetime.now()
		time = now.strftime("%d/%m/%Y %H:%M:%S")
		conn = pymysql.connect(host="localhost",user="root",password="1234",database="inputpelanggan")
		cur = conn.cursor()
		query= ("insert into register(ID,nama,alamat,hp,Time) values(%s,%s,%s,%s,%s)")
		data =cur.execute(query,(ID,nama,alamat,hp,time))
		conn.commit()
		if (data):
			self.messagebox("success","data berhasil di input")
			self.ID.clear()
			self.nama.clear()
			self.alamat.clear()
			self.hp.clear()

	def __init__(self):
		super().__init__()
		self.setWindowTitle("Input Pelanggan")
		self.setGeometry(500,100,640,480)

		self.label = QtWidgets.QLabel(self)
		self.label.setGeometry(QtCore.QRect(30, 100, 71, 16))
		self.label.setText("ID Pelanggan")

		self.label_2 = QtWidgets.QLabel(self)
		self.label_2.setText("Nama")	
		self.label_2.setGeometry(30, 140, 47, 13)

		self.label_3 = QtWidgets.QLabel(self)
		self.label_3.setText("Alamat")
		self.label_3.setGeometry(QtCore.QRect(30, 180, 47, 13))

		self.label_4 = QtWidgets.QLabel(self)
		self.label_4.setText("No Hp")
		self.label_4.setGeometry(QtCore.QRect(30, 220, 47, 13))

		self.label_5 = QtWidgets.QLabel(self)
		self.label_5.setText("Foto")
		self.label_5.setGeometry(QtCore.QRect(300, 100, 47, 13))
		# global c
		# global filename
		# if (c > 0):
		# 	self.label_6 = QLabel(self)
		# 	self.label_6.setPixmap(QPixmap(filename))
		# 	self.label_6.setGeometry(QtCore.QRect(300, 130,300, 260))
		# else:
		# 	False

		self.pushbutton = QtWidgets.QPushButton(self)
		self.pushbutton.setText("Input")
		self.pushbutton.setGeometry(QtCore.QRect(140, 410, 75, 23))
		self.pushbutton.clicked.connect(self.flag)

		self.pushbutton2 = QtWidgets.QPushButton(self)
		self.pushbutton2.setText("Ambil gambar")
		self.pushbutton2.setGeometry(QtCore.QRect(280, 410, 75, 23))
		self.pushbutton2.clicked.connect(self.takephoto)

		self.ID = QLineEdit(self)
		self.ID.move(100,100)
		self.ID.setPlaceholderText("masukkan ID Anda")
		self.ID.setObjectName("ID")

		self.nama = QLineEdit(self)
		self.nama.move(100,140)
		self.nama.setPlaceholderText("masukkan Nama Anda")
		self.nama.setObjectName("nama")

		self.alamat = QLineEdit(self)
		self.alamat.move(100,180)
		self.alamat.setPlaceholderText("masukkan Alamat Anda")
		self.alamat.setObjectName("alamat")

		self.hp = QLineEdit(self)
		self.hp.move(100,220)
		self.hp.setPlaceholderText("masukkan No HP Anda")
		self.hp.setObjectName("hp")

c=0
if __name__ == '__main__':
	app = QApplication(sys.argv)
	inputpelanggan = input()
	inputpelanggan.show()
	sys.exit(app.exec_())
