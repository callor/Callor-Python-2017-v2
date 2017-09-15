'''
Created on 2017. 9. 15.
@author: callor
'''
from sys import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

# 폴더이름.파일명
from grade.Grad_List import *

Grade_Form = uic.loadUiType('./grade_form.ui')[0]

class GradeInput(QMainWindow,Grade_Form):
    
    def __init__(self):
        super().__init__() # QMainWindow 상속 초기화
        self.setupUi(self) # Grade_Form 상속 초기화

    def initUi(self):
        self.initTextBox()
        self.btn_save.clicked.connect(self.gradeWrite)
        self.btn_list.clicked.connect(self.gradeList)
        self.show()
        
    def gradeWrite(self):
        
        num1 = self.txt_num.text()
        name1 = self.txt_name.text()
        kor = self.txt_kor.text()
        eng = self.txt_eng.text()
        math = self.txt_math.text()
        
        # nun:name:kor:eng:math
        # 클릭할때마다 새로 파일이 오픈되므로
        # 파일을 열때 write 가 아닌 append mode로 열어야 한다.
        with open('./grade.txt','a',encoding='UTF-8') as f1 :
    
            saveformat = "{0}:{1}:{2}:{3}:{4}\n"
            saveText = saveformat.format(num1,name1,kor,eng,math)
            print(saveText)
            
            f1.write(saveText)
            
        self.initTextBox()
            
    def initTextBox(self):
        curCount = self.getNum()
        intCount = int(curCount) + 1
        self.txt_num.setText( str(intCount) )
        self.txt_name.setText("")
        self.txt_kor.setText("")
        self.txt_eng.setText("")
        self.txt_math.setText("") 
        
    def getNum(self):
        lines = 0
        
        try:
            with open('./grade.txt','r',encoding='UTF-8') as f2 :
                readLine = f2.readlines() # 파일 전체를 읽어서 라인단위로 잘라 list로 
                lines = len(readLine)
        except:
            lines = 0
            
        return lines
        
    def gradeList(self):
        gradeList = GradeList()
        gradeList.exec_()
        
if __name__ == "__main__" :
    app = QApplication(argv)
    gradeInput = GradeInput()
    gradeInput.initUi()
    
    exit(app.exec_()) # app.exe_()
    
    
    
    
    
    
    
    
    
    
    