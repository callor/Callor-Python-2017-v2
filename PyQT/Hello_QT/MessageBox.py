'''
Created on 2017. 9. 12.

@author: callor
'''
from sys import *
from PyQt5.QtWidgets import *


class QtMsg(QWidget):
    
    def __init__(self):
        super().__init__()
        
    def initUit(self):
        
        
        self.setGeometry(300,300,250,250)
        self.setWindowTitle("Message")
        self.show()
        
        
    def closeEvent(self,event):
        re = QMessageBox.question(self, "Close", "현재창을 닫을까요?", 
            QMessageBox.No|QMessageBox.Yes,QMessageBox.No)
        
        if re == QMessageBox.Yes :
            event.accept()
        else :
            event.ignore()
            
if __name__ == "__main__" :
    app = QApplication(argv)
    qex = QtMsg()
    qex.initUit()
    
    exit(app.exec_())
    














