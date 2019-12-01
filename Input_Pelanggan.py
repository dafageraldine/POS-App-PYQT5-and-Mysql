from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QLineEdit,QWidget,QApplication)
import sys
import pymysql
import cv2
import numpy as np

class input(QWidget):
	def takephoto(self):
		cap = cv2.VideoCapture(0)
		if cap.isOpened():
			ret,frame = cap.read()
		else:
			ret = False
		while True:
			cv2.imshow('camera',frame)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
		cap.release()

	def register(self):
		ID = self.ID.text()
		nama = self.nama.text()
		alamat = self.alamat.text()
		hp = self.hp.text()
		conn = pymysql.connect(host="localhost",user="root",password="1234",database="inputpelanggan")
		cur = conn.cursor()
		query= ("insert into register(ID,nama,alamat,hp) values(%s,%s,%s,%s)")
		data =cur.execute(query,(ID,nama,alamat,hp)) 

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
		self.label_5.setGeometry(QtCore.QRect(30, 280, 47, 13))

		self.pushbutton = QtWidgets.QPushButton(self)
		self.pushbutton.setText("Input")
		self.pushbutton.setGeometry(QtCore.QRect(140, 410, 75, 23))
		self.pushbutton.clicked.connect(self.register)

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


if __name__ == '__main__':
	app = QApplication(sys.argv)
	inputpelanggan = input()
	inputpelanggan.show()
	sys.exit(app.exec_())