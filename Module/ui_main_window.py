import sys,os
import numpy as np
# import some PyQt5 modules
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
# import Opencv module
import cv2

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def __init__(self, w):
        self.w = w
        self.Form = QtWidgets.QDialog(w)
        self.Form.setObjectName("Form")
        self.Form.resize(525, 386)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.image_label = QtWidgets.QLabel(self.Form)
        self.image_label.setObjectName("image_label")
        self.verticalLayout.addWidget(self.image_label)
        self.control_bt = QtWidgets.QPushButton(self.Form)
        self.control_bt.setObjectName("control_bt") 
        self.control_bt.clicked.connect(self.controlTimer)
        self.control_bt.setGeometry(QtCore.QRect(15, 15,150, 50))
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.n = 0

        ##mycode
        self.timer = QTimer()
        self.timer.timeout.connect(self.viewCam)
        self.retranslateUi(self.Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Camera"))
        self.image_label.setText(_translate("Form", "\t\t\tArahkan Wajah Anda\n \t\t\tKe Dalam Box Hijau"))
        self.control_bt.setText(_translate("Form", "Start"))

    def viewCam(self):
        check,frame = self.cap.read()
        if frame is None:
            self.w.showDialog("warning", "Gagal","Tidak ada kamera yang terdeteksi")
            self.timer.stop()
            self.cap.release()
            return
            
        data = frame.copy()
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frameh = 400
        framew = 267
        start_x = 175
        start_y = 45
        start_point = (start_x, start_y)
        end_point = (start_x + framew, start_y + frameh)
        thickness = 3
        color = (0,255,0)
        images = cv2.rectangle(image, start_point, end_point,color ,thickness)
        self.crop_img = data[start_y:start_y+frameh, start_x:start_x+framew]
        height, width, channel = image.shape
        step = channel * width
        height += 1
        qImg = QImage(images.data,width,height,step,QImage.Format_RGB888)
        self.image_label.setPixmap(QPixmap.fromImage(qImg))

    def controlTimer(self):
        setval = self.w.mysql.find("camera","setting","idSettings","set-1","False")
        # print(setval)
        if not self.timer.isActive():
            self.cap = cv2.VideoCapture(setval[0][0])
            self.timer.start(20)
            self.control_bt.setText("Capture")
            
        else:
            self.timer.stop()
            self.cap.release()
            if (self.w.pelanggan.ID.text() != ""):
                self.filename = self.w.pelanggan.ID.text() + str(".jpg")
                path = QtCore.QDir.currentPath()
                path = path + '/Module/static'
                imagepath = path + '/' + self.filename
                cv2.imwrite(os.path.join(path , self.filename), self.crop_img)
            elif (self.w.pelanggan.ID.text() == "") : 
                self.filename = self.w.mysql.select("id", "pelanggan", False, "id DESC")
                if self.filename != None :
                    self.filename = '{:04d}'.format(self.filename[0]+1)
                else:
                    self.filename = '{:04d}'.format(1)
                self.filename = "BEA-" + str(self.filename)+ ".jpg"
                path = QtCore.QDir.currentPath()
                path = path + '/Module/static'
                imagepath = path + '/' + self.filename
                cv2.imwrite(os.path.join(path , self.filename), self.crop_img)
            imagess = QtGui.QPixmap(imagepath)
            self.w.pelanggan.img.setPixmap(imagess.scaled(200,250,QtCore.Qt.KeepAspectRatio))
            self.n = 1
            self.w.pelanggan.hapus.setEnabled(True)
            self.image_label.setText("\t\t\t\tArahkan Wajah Anda\n \t\t\t\tKe Dalam Box Hijau")
            self.close()
    
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

    def close(self):
        self.Form.close()     

    def show(self):
        self.Form.exec_()
