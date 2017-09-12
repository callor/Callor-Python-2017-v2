'''
Created on 2017. 9. 12.

@author: callor
'''
from sys import *
from PyQt5.QtWidgets import *

# argv sys.argv 의 변수
# 명령줄에서 입력한 인수를 담는 변수
#     python Qt_01.py a b c
# 
print(argv)
print(argv[0])
# QT 시작하기 위한 초기화 함수
#     현재 파일이름을 매개변수로 받야 한다.
# QApplication(['C:\\bitWork\\bit201708LeeSJ\\PyQT\\Hello_QT\\Qt_01.py'])
app = QApplication(argv) # 현재파일이름을 QApp..에게 넘겨주어서 초기화
w = QWidget()
w.resize(250,250)
w.setWindowTitle("QT 연습")
w.show()

# 현재 창을 띄우고 기다려라
exit(app.exec_())