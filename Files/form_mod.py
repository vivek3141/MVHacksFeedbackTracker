import sys
from form_auto import *
from PyQt4 import QtCore, QtGui, uic 
import sqlite3
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class Form(QtGui.QDialog):
    def __init__(self,parent=None): 
        QtGui.QWidget.__init__(self, parent) 
        self.ui = Ui_Dialog() 
        self.ui.setupUi(self)
        self.get()

    def get(self):
        conn = sqlite3.connect("data.db")
        c = conn.cursor()
        c.execute("select Name from student")
        list = c.fetchall()
        conn.commit()
        print(list)
        for i in list:
            a = i[0]
            self.cbx = QtGui.QCheckBox()
            self.cbx.setGeometry(QtCore.QRect(183, 521, 75, 23))
            self.cbx.setObjectName(_fromUtf8("cbx_"+str(a)))
            self.cbx.setText(a)
         
if __name__=="__main__": 
    app=QtGui.QApplication(sys.argv) 
    myapp=Form()
    myapp.show()
    sys.exit(app.exec_()) 
