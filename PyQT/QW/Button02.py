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
        
        # static label
        textLabel = QLabel("Message:",self)
        textLabel.move(20,20)
        
        # dynamic label
        self.label = QLabel("",self)
        self.label.move(80,20)
        self.label.resize(150,30)
        
        btn1 = QPushButton("확인",self)
        btn1.move(20,60)
        btn1.clicked.connect(self.btn_click)
        
        self.show()
        
    
    def btn_click(self):
        self.label.setText("안녕하세요")
        
    
if __name__ == "__main__" :
    app = QApplication(argv)
    buEx = BuExam()
    buEx.initUi()
    exit(app.exec_())  
    
    
    
    
    