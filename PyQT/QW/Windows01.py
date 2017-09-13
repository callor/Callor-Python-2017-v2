'''
Created on 2017. 9. 13.

@author: callor
'''
from sys import *
from PyQt5.QtWidgets import *

# Status Bar
# 화면의 하단에 메시지 표시하는 영역
class StatusExam(QMainWindow):
    
    # 정해진 키워드 __init__
    # 생성자, 클래스를 이용해서 객체를 생성할때 제일먼저
    #    호출되는 method
    def __init__(self):
        super().__init__()
#         self.initUi()
        
    # 임의로 만드는 method
    #    class 내부에 있는 함수는 method 호칭
    #    화면 구성을 하기 위해 만드는 사용자 정의 함수
    def initUi(self):
        # this 상수는 현재 클래스 자신, 
        #    (상속받을경우) 부모 클래스까지 포함해서
        self.statusBar().showMessage("Ready")

        menubar = self.menuBar() # 메뉴 생성
        filemenu = menubar.addMenu("File")
        filemenu.addMenu("New")
        filemenu.addMenu('open')
        filemenu.addMenu("save")
        filemenu.addMenu("-------")
        filemenu.addMenu("exit")
        
        editmenu = menubar.addMenu("Edit",self)
        
        
        
        #
        # 좌측상단 꼭지점 좌표(x : left로부터,y : top으로 부터)
        # width, height
        #                 x   y  width height   
        self.setGeometry(300,300,250,250)
        self.setWindowTitle("StatusBar 연습")
        self.show()

        
# 현재 모듈(class, def)을 self test 하는 부분
if __name__ == "__main__" :
    app = QApplication(argv)
    stExam = StatusExam() # 클래스를 객체로 생성하는 구문
                          # JAVA: StatusExam stEzam = new StatusExam();
                          #     new : __init__(self) 부분에 해당
                          
    stExam.initUi()
    exit(app.exec_())
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    