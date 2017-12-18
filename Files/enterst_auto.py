# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'enterst.ui'
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
        Dialog.resize(875, 588)
        Dialog.setStyleSheet(_fromUtf8("font: 12pt \"Berlin Sans FB\";\n"
"background-color: rgb(85, 255, 255);"))
        self.tableView = QtGui.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(30, 80, 381, 471))
        self.tableView.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(420, 310, 121, 93))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(430, 110, 61, 127))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(440, 400, 71, 111))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(440, 240, 61, 61))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(350, 30, 371, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(630, 540, 112, 34))
        self.pushButton.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(540, 100, 271, 431))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.li_1 = QtGui.QLineEdit(self.widget)
        self.li_1.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.li_1.setObjectName(_fromUtf8("li_1"))
        self.verticalLayout.addWidget(self.li_1)
        self.li_2 = QtGui.QLineEdit(self.widget)
        self.li_2.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.li_2.setObjectName(_fromUtf8("li_2"))
        self.verticalLayout.addWidget(self.li_2)
        self.li_3 = QtGui.QLineEdit(self.widget)
        self.li_3.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.li_3.setObjectName(_fromUtf8("li_3"))
        self.verticalLayout.addWidget(self.li_3)
        self.li_4 = QtGui.QLineEdit(self.widget)
        self.li_4.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.li_4.setObjectName(_fromUtf8("li_4"))
        self.verticalLayout.addWidget(self.li_4)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Student ID:", None))
        self.label_2.setText(_translate("Dialog", "Name", None))
        self.label_3.setText(_translate("Dialog", "School", None))
        self.label_4.setText(_translate("Dialog", "Grade", None))
        self.label_5.setText(_translate("Dialog", "Enter Student", None))
        self.pushButton.setText(_translate("Dialog", "Submit", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

