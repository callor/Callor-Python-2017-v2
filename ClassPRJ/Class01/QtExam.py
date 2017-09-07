'''
Created on 2017. 9. 7.
@author: callor
'''

from sys import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


'''
Widget
    모든 도구
        창, 버튼, 입력상자
    창 : 창도 포함할수 있다
        포함되는 창 Frame
        Layout Frame
'''

class ExamWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()
    
    # ui 를 디자인 하는 method     
    def initUi(self):
        
       # 화면의 크기를 설정
       self.setGeometry(300,300,300,300)
       self.setWindowTitle("QT Window 연습")
       self.show() 
       
if __name__ == "__main__" :
    app = QApplication(argv) # sys.argv
    mywin = ExamWin()
    
#     mywin.initUi()
    exit(app.exec_())












