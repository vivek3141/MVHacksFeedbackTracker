# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
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
        MainWindow.resize(788, 428)
        MainWindow.setMaximumSize(QtCore.QSize(794, 428))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(-10, 0, 821, 381))
        self.graphicsView.setStyleSheet(_fromUtf8("background-image: url(:/real/snip.PNG);"))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 788, 31))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFeedback = QtGui.QMenu(self.menubar)
        self.menuFeedback.setObjectName(_fromUtf8("menuFeedback"))
        self.menuStudent = QtGui.QMenu(self.menubar)
        self.menuStudent.setObjectName(_fromUtf8("menuStudent"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionGive_Feedback = QtGui.QAction(MainWindow)
        self.actionGive_Feedback.setObjectName(_fromUtf8("actionGive_Feedback"))
        self.actionAdd_Student = QtGui.QAction(MainWindow)
        self.actionAdd_Student.setObjectName(_fromUtf8("actionAdd_Student"))
        self.actionV = QtGui.QAction(MainWindow)
        self.actionV.setObjectName(_fromUtf8("actionV"))
        self.actionCheck_in = QtGui.QAction(MainWindow)
        self.actionCheck_in.setObjectName(_fromUtf8("actionCheck_in"))
        self.actionView_Feedback = QtGui.QAction(MainWindow)
        self.actionView_Feedback.setObjectName(_fromUtf8("actionView_Feedback"))
        self.actionFull_Report = QtGui.QAction(MainWindow)
        self.actionFull_Report.setObjectName(_fromUtf8("actionFull_Report"))
        self.menuFeedback.addAction(self.actionGive_Feedback)
        self.menuFeedback.addAction(self.actionView_Feedback)
        self.menuFeedback.addAction(self.actionFull_Report)
        self.menuStudent.addAction(self.actionAdd_Student)
        self.menuStudent.addAction(self.actionV)
        self.menuStudent.addAction(self.actionCheck_in)
        self.menubar.addAction(self.menuFeedback.menuAction())
        self.menubar.addAction(self.menuStudent.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MVHacks", None))
        self.menuFeedback.setTitle(_translate("MainWindow", "Feedback", None))
        self.menuStudent.setTitle(_translate("MainWindow", "Student", None))
        self.actionGive_Feedback.setText(_translate("MainWindow", "Give Feedback", None))
        self.actionAdd_Student.setText(_translate("MainWindow", "Add Student", None))
        self.actionV.setText(_translate("MainWindow", "View Students", None))
        self.actionCheck_in.setText(_translate("MainWindow", "Check in", None))
        self.actionView_Feedback.setText(_translate("MainWindow", "View Feedback", None))
        self.actionFull_Report.setText(_translate("MainWindow", "Full Report", None))

import res_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

