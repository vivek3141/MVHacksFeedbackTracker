import sys
from enterst_auto import *
from PyQt4 import QtCore, QtGui, uic, QtSql
import sqlite3

 
class Enter(QtGui.QDialog):
    def __init__(self,parent=None): 
        QtGui.QWidget.__init__(self, parent) 
        self.ui = Ui_Dialog() 
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pushButton,QtCore.SIGNAL('clicked()'),self.submit)
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("data.db")
        db.open()
        self.ref()
    def submit(self):
        s1 = self.ui.li_1.text()
        s2 = self.ui.li_2.text()
        s3 = self.ui.li_3.text()
        s4 = self.ui.li_4.text()
        try:
            s2 = int(s2)
        except ValueError:
            QtGui.QMessageBox.information(self, "Invalid Input!",  "Grade should be a number!")
            return False
        if not(s2>0 and s2<13):
            QtGui.QMessageBox.information(self, "Invalid Input!",  "Grade should be between 1 and 12!")
            return False
        if(s3 != ""):
            try:
                s3 = int(s3)
            except ValueError:
                QtGui.QMessageBox.information(self, "Invalid Input!",  "Student ID should be a number!")
                return False
        if(s2 == "" or s4 == "" or s1 == ""):
            QtGui.QMessageBox.information(self, "Invalid Input!",  "Please fill the columns!")
            return False

        conn = sqlite3.connect("data.db")
        c = conn.cursor()
        c.execute("select ID from student")
        a = c.fetchall()
        id = a[-1][0] + 1
        c.execute("INSERT INTO student VALUES(?,?,?,?,?)",(id, str(s3),str(s1),str(s2),str(s4)))
        QtGui.QMessageBox.information(self, "Thanks:)",  "Thanks for your input!")
        self.ui.li_1.setText("")
        self.ui.li_2.setText("")
        self.ui.li_3.setText("") 
        self.ui.li_4.setText("")
        conn.commit()
        self.ref()
            

        
    def ref(self):
        self.model = QtSql.QSqlQueryModel(self)
        sql = "select Name, School from student;"
        self.model.setQuery(sql)
        self.ui.tableView.setModel(self.model)
         
if __name__=="__main__": 
    app=QtGui.QApplication(sys.argv) 
    myapp=Enter()
    myapp.show()
    sys.exit(app.exec_()) 
