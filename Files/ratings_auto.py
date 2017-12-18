# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ratings.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(771, 452)
        Dialog.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 16pt \"Berlin Sans FB\";\n"
"background-color: rgb(118, 118, 118);"))
        self.p_1 = QtGui.QProgressBar(Dialog)
        self.p_1.setGeometry(QtCore.QRect(290, 120, 471, 31))
        self.p_1.setProperty("value", 24)
        self.p_1.setObjectName(_fromUtf8("p_1"))
        self.p_2 = QtGui.QProgressBar(Dialog)
        self.p_2.setGeometry(QtCore.QRect(290, 200, 471, 31))
        self.p_2.setProperty("value", 24)
        self.p_2.setObjectName(_fromUtf8("p_2"))
        self.p_3 = QtGui.QProgressBar(Dialog)
        self.p_3.setGeometry(QtCore.QRect(290, 290, 471, 31))
        self.p_3.setProperty("value", 24)
        self.p_3.setObjectName(_fromUtf8("p_3"))
        self.p_4 = QtGui.QProgressBar(Dialog)
        self.p_4.setGeometry(QtCore.QRect(290, 380, 471, 31))
        self.p_4.setProperty("value", 24)
        self.p_4.setObjectName(_fromUtf8("p_4"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 120, 181, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 200, 191, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 290, 261, 41))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 370, 251, 41))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(300, 20, 431, 51))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Ratings", None))
        self.label.setText(_translate("Dialog", "Services", None))
        self.label_2.setText(_translate("Dialog", "Workshops", None))
        self.label_3.setText(_translate("Dialog", "Future hackathons", None))
        self.label_4.setText(_translate("Dialog", "Overall experience", None))
        self.label_5.setText(_translate("Dialog", "Ratings ", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

