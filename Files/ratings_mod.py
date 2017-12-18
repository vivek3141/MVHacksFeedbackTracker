import sys
from ratings_auto import * 
import sqlite3
class Rate(QtGui.QDialog):
    def __init__(self,parent=None): 
        QtGui.QWidget.__init__(self, parent) 
        self.ui = Ui_Dialog() 
        self.ui.setupUi(self)
        self.setValues()
    def setValues(self): 
        conn = sqlite3.connect("data.db")
        c = conn.cursor()
        c.execute("select Q1,Q2,Q3,Q4 from feedback")
        li = c.fetchall()
        conn.commit()
        print(li)
        tot = len(li)*4
        tot3 = len(li)*2
        a = [0,0,0,0]
        k = 0
        for i in li:
            k = 0
            for l in i:
                a[k] = a[k] + (l-1)
                k = k + 1
        print(a)
        self.ui.p_1.setValue((a[0]/tot)*100)
        self.ui.p_2.setValue((a[1]/tot)*100)
        self.ui.p_3.setValue((a[2]/tot3)*100)
        self.ui.p_4.setValue((a[3]/tot)*100)
if __name__=="__main__": 
    app=QtGui.QApplication(sys.argv) 
    myapp=Rate()
    myapp.show()
    sys.exit(app.exec_()) 
