# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'feedback.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1110, 455)
        MainWindow.setStyleSheet(_fromUtf8("font: 16pt \"Berlin Sans FB\";\n"
"color: rgb(0, 0, 0);\n"
"\n"
""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pb_sub = QtGui.QPushButton(self.centralwidget)
        self.pb_sub.setGeometry(QtCore.QRect(811, 330, 151, 34))
        self.pb_sub.setStyleSheet(_fromUtf8("color: rgb(85, 255, 127);\n"
"background-color: rgb(255, 255, 255);"))
        self.pb_sub.setObjectName(_fromUtf8("pb_sub"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(950, 0, 121, 309))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.sb_1 = QtGui.QSpinBox(self.layoutWidget)
        self.sb_1.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.sb_1.setMinimum(1)
        self.sb_1.setMaximum(5)
        self.sb_1.setObjectName(_fromUtf8("sb_1"))
        self.verticalLayout.addWidget(self.sb_1)
        self.sb_4 = QtGui.QSpinBox(self.layoutWidget)
        self.sb_4.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.sb_4.setMinimum(1)
        self.sb_4.setMaximum(5)
        self.sb_4.setObjectName(_fromUtf8("sb_4"))
        self.verticalLayout.addWidget(self.sb_4)
        self.sb_3 = QtGui.QSpinBox(self.layoutWidget)
        self.sb_3.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.sb_3.setMinimum(1)
        self.sb_3.setMaximum(3)
        self.sb_3.setObjectName(_fromUtf8("sb_3"))
        self.verticalLayout.addWidget(self.sb_3)
        self.sb_2 = QtGui.QSpinBox(self.layoutWidget)
        self.sb_2.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.sb_2.setMinimum(1)
        self.sb_2.setMaximum(5)
        self.sb_2.setObjectName(_fromUtf8("sb_2"))
        self.verticalLayout.addWidget(self.sb_2)
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(-10, 0, 2311, 481))
        self.graphicsView.setStyleSheet(_fromUtf8("background-image: url(:/real/background.png);"))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.layoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(0, 20, 938, 301))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_2 = QtGui.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Berlin Sans FB"))
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_3.addWidget(self.label_2)
        self.label_6 = QtGui.QLabel(self.layoutWidget_2)
        self.label_6.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_3.addWidget(self.label_6)
        self.label_7 = QtGui.QLabel(self.layoutWidget_2)
        self.label_7.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_3.addWidget(self.label_7)
        self.label_8 = QtGui.QLabel(self.layoutWidget_2)
        self.label_8.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_3.addWidget(self.label_8)
        self.pb_sel = QtGui.QPushButton(self.centralwidget)
        self.pb_sel.setGeometry(QtCore.QRect(130, 330, 211, 34))
        self.pb_sel.setStyleSheet(_fromUtf8("color: rgb(85, 255, 127);\n"
"background-color: rgb(255, 255, 255);"))
        self.pb_sel.setObjectName(_fromUtf8("pb_sel"))
        self.lbl = QtGui.QLabel(self.centralwidget)
        self.lbl.setGeometry(QtCore.QRect(360, 330, 441, 31))
        self.lbl.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.lbl.setText(_fromUtf8(""))
        self.lbl.setObjectName(_fromUtf8("lbl"))
        self.graphicsView.raise_()
        self.layoutWidget.raise_()
        self.pb_sub.raise_()
        self.layoutWidget_2.raise_()
        self.pb_sel.raise_()
        self.lbl.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1110, 41))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Feedback", None))
        self.pb_sub.setText(_translate("MainWindow", "Submit", None))
        self.label_2.setText(_translate("MainWindow", "Rate the services from 1-5", None))
        self.label_6.setText(_translate("MainWindow", "Rate the workshops from 1-5", None))
        self.label_7.setText(_translate("MainWindow", "Do you see yourself coming to future hackathons?(1-no,2-maybe,3-yes)", None))
        self.label_8.setText(_translate("MainWindow", "Rate your overall experience", None))
        self.pb_sel.setText(_translate("MainWindow", "Select Student", None))

import res_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

