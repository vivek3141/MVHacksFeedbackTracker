import sys
from PyQt4 import QtCore, QtGui, uic 
import sqlite3
from feedback_auto import *
import table_mod
  
class Feedback(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None): 
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        QtCore.QObject.connect(self.pb_sel, QtCore.SIGNAL('clicked()'), self.student)
        QtCore.QObject.connect(self.pb_sub, QtCore.SIGNAL('clicked()'), self.submit)
        self.name = ""
        self.id = ""
        
    def student(self):
        t = table_mod.Table()
        a = t.selectST()
        if(a == ""):
            return False
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("select Name from student where ID = "+str(a))
        li = cursor.fetchall()
        name = li[0][0]
        print(name)
        self.lbl.setText("Selected: "+name)
        self.name = name
        self.id = a
        conn.commit()
        #print("hi")
    def submit(self):
        if(self.name == ""):
            QtGui.QMessageBox.information(self,  "Invalid Selection!",  "Please select a student first!")
        else:
            r1 = self.sb_1.value()
            r4 = self.sb_2.value()
            r3 = self.sb_3.value()
            r2 = self.sb_4.value()
            print(r1,r2,r3,r4)
            conn = sqlite3.connect("data.db")
            cursor = conn.cursor()
            b = False
            try:
                cursor.execute("INSERT INTO feedback VALUES(?,?,?,?,?)",(self.id,r1,r2,r3,r4))
                b = True
                print("hi")
                self.sb_1.setValue(1)
                self.sb_2.setValue(1)
                self.sb_3.setValue(1) 
                self.sb_4.setValue(1)
                QtGui.QMessageBox.information(self,  "Thanks:)",  "Thanks for your feedback!")
            except sqlite3.Error as e:
                QtGui.QMessageBox.information(self,  "Invalid!",  "Feedback already given!")

            conn.commit()
            
         
if(__name__ == "__main__"): 
    app = QtGui.QApplication(sys.argv)
    myWindow = Feedback(None)
    myWindow.show()
    app.exec_() 
