from __future__ import division

import sys

import pyzbar.pyzbar as pyzbar

import cv2

import barbar_2

from PyQt5.QtCore import *

from PyQt5.QtGui import *

from PyQt5.QtWidgets import *

from GUI_edit_ver_2 import *

import time

import Adafruit_PCA9685

import con_A

import con_B

import serial

 

 

a = 0

b = 0

c = 0

d = 0

e = 0

f = 0

 

app = QApplication(sys.argv)

Dialog = QDialog()

ui = Ui_Dialog()

ui.setupUi(Dialog)

Dialog.show()

BAR = barbar_2.Baread()

MO_a = con_A.CON_A()

MO_b = con_B.CON_B()

#getChar[] = None

def barcode_read():

    global a,b,c,d,e,f

    if __name__ == '__main__':

        ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

        ser.flush()

        

    while True:

        BAR = barbar_2.Baread()

        

        bar_data = BAR.baread()       

 

            

    

    #while True:

        if bar_data == "hadong":               

            ser.write(b'hadong')

            if ser.in_waiting > 0:

                line = ser.readline().decode('utf-8').rstrip()

                #print(line)

            a += 1

            ui.report('[ 하  동 ]')

            ui.hadong(a)

            MO_a.hadong()

            

        elif bar_data == "jidong":

            ser.write(b'jidong')

            if ser.in_waiting > 0:

                line = ser.readline().decode('utf-8').rstrip()

                #print(line)

            b += 1

            ui.report('[ 지  동 ]')

            ui.jidong(b)

            MO_a.jidong()

            

        elif bar_data == "ingyedong":

            c += 1

            ui.report('[ 인 계 동 ]')

            ui.ingyedong(c)

            MO_a.ingyedong()

            

        elif bar_data == "umandong":            

            d += 1

            ui.report('[ 우 만 동 ]')

            ui.umandong(d)

            MO_b.umandong()

            

        elif bar_data == "yeonmudong":

            ser.write(b'yeonmudong')

            if ser.in_waiting > 0:

                line = ser.readline().decode('utf-8').rstrip()

                #print(line)            

            e += 1

            ui.report('[ 연 무 동 ]')

            ui.yeonmudong(e)

            MO_b.yeonmudong()

            

        elif bar_data == "iuidong":

            ser.write(b'iuidong')

            if ser.in_waiting > 0:

                line = ser.readline().decode('utf-8').rstrip()

                #print(line)            

            f += 1

            ui.report('[ 이 의 동 ]')

            ui.iuidong(f)

            MO_b.iuidong()

            

        else:

            ui.error()

    

 

barcode_read()

 

sys.exit(app.exec_())