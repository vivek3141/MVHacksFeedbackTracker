import sys
from PyQt4 import QtCore, QtGui, uic, QtSql 
import sqlite3
from table_auto import * 
  
class Table(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None): 
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
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
        self.tableView.setModel(self.model)
    def selectST(self):
        dialog = Table()
        dialog.show()
        result = dialog.exec_()
        if result == 1:
            index = dialog.ui.tableView.currentIndex()
            id_us = dialog.ui.tableView.model().data(index)
            if str(id_us).isdigit():
                return id_us
            else:
                QtGui.QMessageBox.information(self,  "Invalid Selection!",  "Please select the ID and not the name!")
                return ""
        else:
            return ""
 	     
         
if(__name__ == "__main__"): 
    app = QtGui.QApplication(sys.argv)
    myWindow = Table(None)
    myWindow.show()
    app.exec_() 
