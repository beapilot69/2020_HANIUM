import sys
import pyzbar.pyzbar as pyzbar
import cv2
import barcode
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from GUI_2 import *

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
BAR = barcode.Baread()
while True:
    
    bar_data = BAR.baread()
    if bar_data == "yeonmudong":
        a += 1
        ui.report('[ 연 무 동 ]',a)
        ui.ym(a)
    elif bar_data == "umandong":
        b += 1
        ui.report('[ 우 만 동 ]',b)
        ui.um(b)
    elif bar_data == "iuidong":
        c += 1
        ui.report('[ 이 의 동 ]',c)
        ui.ii(c)
    elif bar_data == "ingyedong":
        d += 1
        ui.report('[ 인 계 동 ]',d)
        ui.ig(d)
    elif bar_data == "jidong":
        e += 1
        ui.report('[ 지 동 ]',e)
        ui.ji(e)
    elif bar_data == "hadong":
        f += 1
        ui.report('[ 하 동 ]',f)
        ui.ha(f)    
    else:
        ui.error()

sys.exit(app.exec_())