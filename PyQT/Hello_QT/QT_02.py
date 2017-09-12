'''
Created on 2017. 9. 12.

@author: callor
'''
from sys import *
from PyQt5.QtWidgets import *


class QtExam(QWidget):
    
    def __init__(self):
        super().__init__() # QWidget의 함수, 변수를 이어받아서 사용하겠다
        
        
    def initUi(self):
        
        self.resize(250,250)
        self.center()
        
        self.setWindowTitle("QT 연습")
        self.show()
        
    # 창을 현재 모니터 중앙에 위치하도록 하는 사용자 함수
    def center(self):
        r = self.frameGeometry()
        c = QDesktopWidget().availableGeometry().center()
        r.moveCenter(c)
        self.move(r.topLeft())
        
        
if __name__ == "__main__" :
    app = QApplication(argv)
    qex = QtExam() # 클래스로 객체를 선언
    qex.initUi() # 객체 내의 initUi Method를 실행
    exit(app.exec_())