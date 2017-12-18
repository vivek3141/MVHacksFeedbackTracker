import sys
sys.path.append("./Files")
from PyQt4 import QtCore, QtGui, uic 
import feedback_mod
from main_auto import *
import entrest_mod
import table_mod
import feed_mod
import ratings_mod  
class Main(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None): 
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        QtCore.QObject.connect(self.actionGive_Feedback,QtCore.SIGNAL('triggered()'),self.showFeedback)
        QtCore.QObject.connect(self.actionAdd_Student,QtCore.SIGNAL('triggered()'),self.showStudent)
        QtCore.QObject.connect(self.actionV,QtCore.SIGNAL('triggered()'),self.showvStudent)
        QtCore.QObject.connect(self.actionView_Feedback,QtCore.SIGNAL('triggered()'),self.showFeed)
        QtCore.QObject.connect(self.actionFull_Report,QtCore.SIGNAL('triggered()'),self.showReport)
    def showFeedback(self):
        feed = feedback_mod.Feedback(self)
        feed.setFixedSize(feed.size())
        feed.show()
    def showStudent(self):
        st = entrest_mod.Enter()
        st.setFixedSize(st.size())
        st.show()
        st.exec_()
    def showvStudent(self):
        t = table_mod.Table()
        t.setFixedSize(t.size())
        t.show()
        t.exec_()
    def showFeed(self):
        f = feed_mod.Table()
        f.setFixedSize(f.size())
        f.show()
        f.exec_()
    def showReport(self):
        r = ratings_mod.Rate()
        r.setFixedSize(r.size())
        r.show()
        r.exec_()
     	     
         
 
app = QtGui.QApplication(sys.argv)
myWindow = Main(None)
myWindow.show()
app.exec_() 
