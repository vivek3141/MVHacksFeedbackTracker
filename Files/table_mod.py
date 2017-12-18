import sys
from table_auto import *
from PyQt4 import QtCore, QtGui, uic, QtSql
 
class Table(QtGui.QDialog):
    def __init__(self,parent=None): 
        QtGui.QWidget.__init__(self, parent) 
        self.ui = Ui_Dialog() 
        self.ui.setupUi(self)
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("data.db")
        db.open()
        self.ret()
        #print(self.tableView)
        
        
        
    def ret(self):
        """conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("select * from student")
        a = cursor.fetchall()
        print(a)
        conn.commit()"""
        self.model = QtSql.QSqlQueryModel(self)
        sql = "select ID, Name, School from student;"
        self.model.setQuery(sql)
        self.ui.tableView.setModel(self.model)
    def selectST(self):
        #print("hi")
        dialog = Table()
        dialog.show()
        result = dialog.exec_()
        index = dialog.ui.tableView.currentIndex()
        print(index)
        id_us = dialog.ui.tableView.model().data(index)
        if str(id_us).isdigit():
            return id_us
        else:
            QtGui.QMessageBox.information(self,  "Invalid Selection!",  "Please select the ID and not the name!")
            return ""
 
        #this is where we will bind the event handlers 
         
#This is where we will insert the functions (defs) 
         
if __name__=="__main__": 
    app=QtGui.QApplication(sys.argv) 
    myapp=Table()
    myapp.show()
    sys.exit(app.exec_()) 
