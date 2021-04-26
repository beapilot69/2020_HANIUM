import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

## font : groupbox의 타이틀 폰트 정보
## in_font : 표시될 정보 텍스트의 폰트 정보
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1000, 850)
        Dialog.setMaximumSize(QSize(1000, 16777215))
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")


        self.TITLE = QLabel(Dialog)
        font = QFont()
        font.setFamily("에스코어 드림 8 Heavy")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.TITLE.setFont(font)
        self.TITLE.setLayoutDirection(Qt.LeftToRight)
        self.TITLE.setObjectName("TITLE")
        self.gridLayout.addWidget(self.TITLE, 0, 1, 1, 1)


        self.groupBox_1 = QGroupBox(Dialog)
        font = QFont()
        font.setFamily("에스코어 드림 6 Bold")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_1.setFont(font)
        self.groupBox_1.setObjectName("groupBox_1")
        self.textBrowser_1 = QTextBrowser(self.groupBox_1)
        self.textBrowser_1.setGeometry(QRect(10, 31, 951, 141))
        in_font = QFont()
        in_font.setFamily("에스코어 드림 6 Bold")
        in_font.setPointSize(20)
        in_font.setBold(True)
        in_font.setWeight(75)
        self.textBrowser_1.setFont(in_font)
        self.textBrowser_1.setObjectName("textBrowser_1")
        self.gridLayout.addWidget(self.groupBox_1, 1, 0, 1, 3)


        self.groupBox_2 = QGroupBox(Dialog)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily("에스코어 드림 6 Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.textBrowser_2 = QTextBrowser(self.groupBox_2)
        self.textBrowser_2.setGeometry(QRect(10, 30, 301, 141))
        in_font = QFont()
        in_font.setFamily("에스코어 드림 6 Bold")
        in_font.setPointSize(18)
        in_font.setBold(True)
        in_font.setWeight(75)
        self.textBrowser_2.setFont(in_font)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.gridLayout.addWidget(self.groupBox_2, 2, 0, 1, 1)


        self.groupBox_3 = QGroupBox(Dialog)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily("에스코어 드림 6 Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.textBrowser_3 = QTextBrowser(self.groupBox_3)
        self.textBrowser_3.setGeometry(QRect(10, 30, 301, 141))
        in_font = QFont()
        in_font.setFamily("에스코어 드림 6 Bold")
        in_font.setPointSize(18)
        in_font.setBold(True)
        in_font.setWeight(75)
        self.textBrowser_3.setFont(in_font)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.gridLayout.addWidget(self.groupBox_3, 2, 1, 1, 1)


        self.groupBox_4 = QGroupBox(Dialog)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily("에스코어 드림 6 Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.textBrowser_4 = QTextBrowser(self.groupBox_4)
        self.textBrowser_4.setGeometry(QRect(10, 30, 301, 141))
        in_font = QFont()
        in_font.setFamily("에스코어 드림 6 Bold")
        in_font.setPointSize(18)
        in_font.setBold(True)
        in_font.setWeight(75)
        self.textBrowser_4.setFont(in_font)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.gridLayout.addWidget(self.groupBox_4, 2, 2, 1, 1)


        self.groupBox_5 = QGroupBox(Dialog)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily("에스코어 드림 6 Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.textBrowser_5 = QTextBrowser(self.groupBox_5)
        self.textBrowser_5.setGeometry(QRect(10, 30, 301, 141))
        in_font = QFont()
        in_font.setFamily("에스코어 드림 6 Bold")
        in_font.setPointSize(18)
        in_font.setBold(True)
        in_font.setWeight(75)
        self.textBrowser_5.setFont(in_font)
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.gridLayout.addWidget(self.groupBox_5, 3, 0, 1, 1)


        self.groupBox_6 = QGroupBox(Dialog)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily("에스코어 드림 6 Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName("groupBox_6")
        self.textBrowser_6 = QTextBrowser(self.groupBox_6)
        self.textBrowser_6.setGeometry(QRect(10, 30, 301, 141))
        in_font = QFont()
        in_font.setFamily("에스코어 드림 6 Bold")
        in_font.setPointSize(18)
        in_font.setBold(True)
        in_font.setWeight(75)
        self.textBrowser_6.setFont(in_font)
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.gridLayout.addWidget(self.groupBox_6, 3, 1, 1, 1)


        self.groupBox_7 = QGroupBox(Dialog)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily("에스코어 드림 6 Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setObjectName("groupBox_7")
        self.textBrowser_7 = QTextBrowser(self.groupBox_7)
        self.textBrowser_7.setGeometry(QRect(10, 30, 301, 141))
        in_font = QFont()
        in_font.setFamily("에스코어 드림 6 Bold")
        in_font.setPointSize(18)
        in_font.setBold(True)
        in_font.setWeight(75)
        self.textBrowser_7.setFont(in_font)
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.gridLayout.addWidget(self.groupBox_7, 3, 2, 1, 1)


        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 3)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox_2.setTitle(_translate("Dialog", "연   무   동"))
        self.groupBox_3.setTitle(_translate("Dialog", "우   만   동"))
        self.groupBox_4.setTitle(_translate("Dialog", "이   의   동"))
        self.groupBox_5.setTitle(_translate("Dialog", "인   계   동"))
        self.groupBox_6.setTitle(_translate("Dialog", "지         동"))
        self.groupBox_7.setTitle(_translate("Dialog", "하         동"))
        self.TITLE.setText(_translate("Dialog", "  분류 현황"))
        self.groupBox_1.setTitle(_translate("Dialog", "현재 분류중인 물류 정보"))
    
    def report(self,bar_data,number):
        self.textBrowser_1.setText(" ")
        self.textBrowser_1.setAlignment(Qt.AlignCenter)
        self.textBrowser_1.append("현재 물품의 집하구역은 " + bar_data + "입니다.")
        self.textBrowser_1.setAlignment(Qt.AlignCenter)

    def ym(self,num):
        num = str(num)
        self.textBrowser_2.setText(" ")
        self.textBrowser_2.setAlignment(Qt.AlignCenter)
        self.textBrowser_2.append(num + " 개")
        self.textBrowser_2.setAlignment(Qt.AlignCenter)

    def um(self,num):
        num = str(num)
        self.textBrowser_3.setText(" ")
        self.textBrowser_3.setAlignment(Qt.AlignCenter)
        self.textBrowser_3.append(num + " 개")
        self.textBrowser_3.setAlignment(Qt.AlignCenter)


    def ii(self,num):
        num = str(num)
        self.textBrowser_4.setText(" ")
        self.textBrowser_4.setAlignment(Qt.AlignCenter)
        self.textBrowser_4.append(num + " 개")
        self.textBrowser_4.setAlignment(Qt.AlignCenter)


    def ig(self,num):
        num = str(num)
        self.textBrowser_5.setText(" ")
        self.textBrowser_5.setAlignment(Qt.AlignCenter)
        self.textBrowser_5.append(num + " 개")
        self.textBrowser_5.setAlignment(Qt.AlignCenter)


    def ji(self,num):
        num = str(num)
        self.textBrowser_6.setText(" ")
        self.textBrowser_6.setAlignment(Qt.AlignCenter)
        self.textBrowser_6.append(num + " 개")
        self.textBrowser_6.setAlignment(Qt.AlignCenter)


    def ha(self,num):
        num = str(num)
        self.textBrowser_7.setText(" ")
        self.textBrowser_7.setAlignment(Qt.AlignCenter)
        self.textBrowser_7.append(num + " 개")
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
