import sys

from PyQt5.QtCore import *

from PyQt5.QtGui import *

from PyQt5.QtWidgets import *

 

class Ui_Dialog(object):

    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")

        Dialog.resize(1680, 1030)

        self.groupBox = QGroupBox(Dialog)

        self.groupBox.setGeometry(QRect(20, 45, 800, 945))

        font = QFont()

        font.setFamily("에스코어 드림 9 Black")

        font.setPointSize(45)

        font.setBold(True)

        font.setWeight(75)

        self.groupBox.setFont(font)

        self.groupBox.setObjectName("groupBox")

        

        self.TITLE = QLabel(Dialog)

        self.TITLE.setGeometry(QRect(845, 45, 810, 100))

        font = QFont()

        font.setFamily("에스코어 드림 9 Black")

        font.setPointSize(45)

        font.setBold(True)

        font.setWeight(75)

        self.TITLE.setFont(font)

        self.TITLE.setCursor(QCursor(Qt.ArrowCursor))

        self.TITLE.setAlignment(Qt.AlignCenter)

        self.TITLE.setObjectName("TITLE")

        

        self.groupBox_1 = QGroupBox(Dialog)

        self.groupBox_1.setGeometry(QRect(845, 170, 810, 270))

        font = QFont()

        font.setFamily("에스코어 드림 9 Black")

        font.setPointSize(20)

        font.setBold(True)

        font.setWeight(75)

        self.groupBox_1.setFont(font)

        self.groupBox_1.setObjectName("groupBox_1")

        self.textBrowser_1 = QTextBrowser(self.groupBox_1)

        self.textBrowser_1.setGeometry(QRect(10, 40, 791, 221))

        in_font = QFont()

        in_font.setFamily("에스코어 드림 6 Bold")

        in_font.setPointSize(33)

        in_font.setBold(True)

        in_font.setWeight(75)

        self.textBrowser_1.setFont(in_font)

        self.textBrowser_1.setObjectName("textBrowser_1")

        

        self.groupBox_2 = QGroupBox(Dialog)

        self.groupBox_2.setGeometry(QRect(845, 440, 260, 260))

        font = QFont()

        font.setFamily("에스코어 드림 9 Black")

        font.setPointSize(23)

        font.setBold(True)

        font.setWeight(75)

        self.groupBox_2.setFont(font)

        self.groupBox_2.setObjectName("groupBox_2")

        self.textBrowser_2 = QTextBrowser(self.groupBox_2)

        self.textBrowser_2.setGeometry(QRect(10, 40, 241, 211))

        in_font = QFont()

        in_font.setFamily("에스코어 드림 6 Bold")

        in_font.setPointSize(45)

        in_font.setBold(True)

        in_font.setWeight(75)

        self.textBrowser_2.setFont(in_font)

        self.textBrowser_2.setObjectName("textBrowser_2")

        

        self.groupBox_3 = QGroupBox(Dialog)

        self.groupBox_3.setGeometry(QRect(1125, 440, 260, 260))

        font = QFont()

        font.setFamily("에스코어 드림 9 Black")

        font.setPointSize(23)

        font.setBold(True)

        font.setWeight(75)

        self.groupBox_3.setFont(font)

        self.groupBox_3.setObjectName("groupBox_3")

        self.textBrowser_3 = QTextBrowser(self.groupBox_3)

        self.textBrowser_3.setGeometry(QRect(10, 40, 241, 211))

        in_font = QFont()

        in_font.setFamily("에스코어 드림 6 Bold")

        in_font.setPointSize(45)

        in_font.setBold(True)

        in_font.setWeight(75)

        self.textBrowser_3.setFont(in_font)

        self.textBrowser_3.setObjectName("textBrowser_3")

        

        self.groupBox_4 = QGroupBox(Dialog)

        self.groupBox_4.setGeometry(QRect(1400, 440, 260, 260))

        font = QFont()

        font.setFamily("에스코어 드림 9 Black")

        font.setPointSize(23)

        font.setBold(True)

        font.setWeight(75)

        self.groupBox_4.setFont(font)

        self.groupBox_4.setObjectName("groupBox_4")

        self.textBrowser_4 = QTextBrowser(self.groupBox_4)

        self.textBrowser_4.setGeometry(QRect(10, 40, 241, 211))

        in_font = QFont()

        in_font.setFamily("에스코어 드림 6 Bold")

        in_font.setPointSize(45)

        in_font.setBold(True)

        in_font.setWeight(75)

        self.textBrowser_4.setFont(in_font)

        self.textBrowser_4.setObjectName("textBrowser_4")

        

        self.groupBox_5 = QGroupBox(Dialog)

        self.groupBox_5.setGeometry(QRect(845, 720, 260, 260))

        font = QFont()

        font.setFamily("에스코어 드림 9 Black")

        font.setPointSize(23)

        font.setBold(True)

        font.setWeight(75)

        self.groupBox_5.setFont(font)

        self.groupBox_5.setObjectName("groupBox_5")

        self.textBrowser_5 = QTextBrowser(self.groupBox_5)

        self.textBrowser_5.setGeometry(QRect(10, 40, 241, 211))

        in_font = QFont()

        in_font.setFamily("에스코어 드림 6 Bold")

        in_font.setPointSize(45)

        in_font.setBold(True)

        in_font.setWeight(75)

        self.textBrowser_5.setFont(in_font)

        self.textBrowser_5.setObjectName("textBrowser_5")

        

        self.groupBox_6 = QGroupBox(Dialog)

        self.groupBox_6.setGeometry(QRect(1125, 720, 260, 260))

        font = QFont()

        font.setFamily("에스코어 드림 9 Black")

        font.setPointSize(23)

        font.setBold(True)

        font.setWeight(75)

        self.groupBox_6.setFont(font)

        self.groupBox_6.setObjectName("groupBox_6")

        self.textBrowser_6 = QTextBrowser(self.groupBox_6)

        self.textBrowser_6.setGeometry(QRect(10, 40, 241, 211))

        in_font = QFont()

        in_font.setFamily("에스코어 드림 6 Bold")

        in_font.setPointSize(45)

        in_font.setBold(True)

        in_font.setWeight(75)

        self.textBrowser_6.setFont(in_font)

        self.textBrowser_6.setObjectName("textBrowser_6")

        

        self.groupBox_7 = QGroupBox(Dialog)

        self.groupBox_7.setGeometry(QRect(1400, 720, 260, 260))

        font = QFont()

        font.setFamily("에스코어 드림 9 Black")

        font.setPointSize(23)

        font.setBold(True)

        font.setWeight(75)

        self.groupBox_7.setFont(font)

        self.groupBox_7.setObjectName("groupBox_7")

        self.textBrowser_7 = QTextBrowser(self.groupBox_7)

        self.textBrowser_7.setGeometry(QRect(10, 40, 241, 211))

        in_font = QFont()

        in_font.setFamily("에스코어 드림 6 Bold")

        in_font.setPointSize(45)

        in_font.setBold(True)

        in_font.setWeight(75)

        self.textBrowser_7.setFont(in_font)

        self.textBrowser_7.setObjectName("textBrowser_7")

 

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

        

        self.textBrowser_2.append(" \n0")

        self.textBrowser_2.setAlignment(Qt.AlignCenter)

        self.textBrowser_3.append(" \n0")

        self.textBrowser_3.setAlignment(Qt.AlignCenter)

        self.textBrowser_4.append(" \n0")

        self.textBrowser_4.setAlignment(Qt.AlignCenter)

        self.textBrowser_5.append(" \n0")

        self.textBrowser_5.setAlignment(Qt.AlignCenter)

        self.textBrowser_6.append(" \n0")

        self.textBrowser_6.setAlignment(Qt.AlignCenter)

        self.textBrowser_7.append(" \n0")

        self.textBrowser_7.setAlignment(Qt.AlignCenter)

 

    def retranslateUi(self, Dialog):

        _translate = QCoreApplication.translate

        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

        self.groupBox.setTitle(_translate("Dialog", "       바코드 인식 화면"))

        self.TITLE.setText(_translate("Dialog", "분 류 현 황"))

        self.groupBox_1.setTitle(_translate("Dialog", " 현재 분류중인 물류 정보"))

        self.groupBox_2.setTitle(_translate("Dialog", " 하         동"))

        self.groupBox_3.setTitle(_translate("Dialog", " 지         동"))

        self.groupBox_4.setTitle(_translate("Dialog", " 인   계   동"))

        self.groupBox_5.setTitle(_translate("Dialog", " 우   만   동"))

        self.groupBox_6.setTitle(_translate("Dialog", " 연   무   동"))

        self.groupBox_7.setTitle(_translate("Dialog", " 이   의   동"))

        

 

    def report(self,bar_data):

        self.textBrowser_1.setText(" ")

        self.textBrowser_1.setAlignment(Qt.AlignCenter)

        self.textBrowser_1.append("현재 물품의 집하구역은\n" + bar_data + "입니다.")

        self.textBrowser_1.setAlignment(Qt.AlignCenter)

        

 

    def hadong(self,num):

        num = str(num)

        self.textBrowser_2.setText(" ")

        self.textBrowser_2.setAlignment(Qt.AlignCenter)

        self.textBrowser_2.append(num)

        self.textBrowser_2.setAlignment(Qt.AlignCenter)

 

    def jidong(self,num):

        num = str(num)

        self.textBrowser_3.setText(" ")

        self.textBrowser_3.setAlignment(Qt.AlignCenter)

        self.textBrowser_3.append(num)

        self.textBrowser_3.setAlignment(Qt.AlignCenter)

 

 

    def ingyedong(self,num):

        num = str(num)

        self.textBrowser_4.setText(" ")

        self.textBrowser_4.setAlignment(Qt.AlignCenter)

        self.textBrowser_4.append(num)

        self.textBrowser_4.setAlignment(Qt.AlignCenter)

 

 

    def umandong(self,num):

        num = str(num)

        self.textBrowser_5.setText(" ")

        self.textBrowser_5.setAlignment(Qt.AlignCenter)

        self.textBrowser_5.append(num)

        self.textBrowser_5.setAlignment(Qt.AlignCenter)

 

 

    def yeonmudong(self,num):

        num = str(num)

        self.textBrowser_6.setText(" ")

        self.textBrowser_6.setAlignment(Qt.AlignCenter)

        self.textBrowser_6.append(num)

        self.textBrowser_6.setAlignment(Qt.AlignCenter)

 

 

    def iuidong(self,num):

        num = str(num)

        self.textBrowser_7.setText(" ")

        self.textBrowser_7.setAlignment(Qt.AlignCenter)

        self.textBrowser_7.append(num)

        self.textBrowser_7.setAlignment(Qt.AlignCenter)

 

 

    def error(self):

        self.textBrowser_1.setText(" ")

        self.textBrowser_1.setAlignment(Qt.AlignCenter)

        self.textBrowser_1.append("ERROR")

        self.textBrowser_1.append("잘못된 바코드 정보입니다. 지정된 지역 바코드를 인식시켜주세요.")

 

 

if __name__ == "__main__":

    import sys

    app = QApplication(sys.argv)

    Dialog = QDialog()

    ui = Ui_Dialog()

    ui.setupUi(Dialog)

    Dialog.show()

    sys.exit(app.exec_())