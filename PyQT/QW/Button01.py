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
        
        btn1 = QPushButton("Bt1",self)
        btn1.move(30,30)
        
        # buttonClicked 는 clicked Event가 메인 윈도우에서 전달되었을때
        # 호출해서 실행할 method이며 이를 event handling
        #   python slot 이라고 호칭
        btn1.clicked.connect(self.buttonClicked)
        
        btn2 = QPushButton("Bt2",self)
        btn2.move(150,30)
        btn2.clicked.connect(self.buttonClicked)
        
        self.statusBar()
        
        self.setWindowTitle("Button 연습")
        self.show()
        
 
    # event handler : slot 이벤트를 처리할 method
    # 임의의 이름으로 설정
    def buttonClicked(self):
        # 이 메서드를 호출하도록 만든 대상
        senderBtn = self.sender()
        self.statusBar().showMessage(senderBtn.text() + " Clicked ")
 
 
        
if __name__ == "__main__" :
    app = QApplication(argv)
    bEx = BuExam()
    bEx.initUi()
    exit(app.exec_())
    
    
    
    
    
    
    
    
    
    
        
        
    
