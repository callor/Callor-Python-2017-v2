'''
Created on 2017. 9. 14.

@author: callor
'''
from sys import *
from PyQt5.QtWidgets import *
from PyQt5 import uic 

# ui 파일을 읽어서 화면(UI) 클래스로 생성
Myform = uic.loadUiType("./mywin.ui")[0]

class MyWindow(QMainWindow,Myform):
    def __init__(self):
        super().__init__()
        
    def initUi(self):
        self.btn_ok.clicked.connect(self.click_btn)
        
    def click_btn(self):
        name1 = self.txt_name.text()
        tel = self.txt_tel.text()
        age = self.txt_age.text()
        
#         self.txt_name.setText("안녕하세요")
        
        txt_sex = ""
        if self.select_man.isChecked() :
            txt_sex = "남자"
        else :
            txt_sex = "여자"
        
        QMessageBox.about(self,"신상정보",
            "이름:" + name1 + "\n"
            +"전화번호:" + tel + "\n"
            +"나이:" + age + "\n"
            +"성별:" + txt_sex)
        
if __name__ == "__main__" :
    app = QApplication(argv)
    myWin = MyWindow()
    myWin.setupUi(myWin) # Myform을 초기화 하는 method
    myWin.initUi()
    
    myWin.show()
    
    exit(app.exec_())
    
    
    
    
