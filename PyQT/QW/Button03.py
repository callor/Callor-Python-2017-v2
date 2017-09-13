'''
Created on 2017. 9. 13.
@author: callor
'''
from sys import *
from PyQt5.QtWidgets import *

class BuExam(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
    def initUi(self):
        
        self.setGeometry(300,300,300,300)
        
        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)
        
        # static label 선언
        label1 = QLabel("값1",self)
        label1.move(20,20)
        
        
        # 입력박스
        self.lineEdit = QLineEdit("",self)
        self.lineEdit.move(80,20)
#         self.lineEdit.textChanged.connect(self.lineEditChage)
#         self.lineEdit.returnPressed.connect(self.keydown)
        
        # Button
        self.btn1 = QPushButton("확인",self)
        self.btn1.move(80,80)
        self.btn1.clicked.connect(self.lineEditChage)

        self.show()
        
    def lineEditChage(self):
        self.statusBar.showMessage(self.lineEdit.text())
        


        
if __name__=="__main__" :
    
    app = QApplication(argv)
    buEx = BuExam()
    buEx.initUi()
    
    # 
    exit(app.exec_())
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        