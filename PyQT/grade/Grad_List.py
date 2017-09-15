'''
Created on 2017. 9. 15.

@author: callor
'''
from sys import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *

Grade_List = uic.loadUiType('./Grade_List.ui')[0]

class GradeList(QDialog,Grade_List):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()
        
    def initUi(self):
        
        rows = self.getNum()
        self.gradeTable = QTableWidget(self)
        
        # gradeTable : 표(table)의 데이터 list를 표현하는 위젯
        # 윈도우 크기와, table 크기를 같게
        self.gradeTable.setGeometry(self.geometry())
        self.gradeTable.setRowCount(rows)
        
        # nun, name, kor, eng, math, totla, avg
        self.gradeTable.setColumnCount(7)
        self.setTableHedaer()
        self.getGrade()
        
        self.show()
        
    # 파일을 읽어서 값을 표시
    def getGrade(self):
#         try:
            with open("./grade.txt",'r',encoding='UTF-8') as f1 :
                gradeLines = f1.readlines()
        
        
            for index,item in enumerate(gradeLines) :
                print(item) # 리스트를 프린터
                grades = item.split(":")
                print(index,grades)
                self.gradeTable.setItem(index,0,QTableWidgetItem(grades[0]))
                self.gradeTable.setItem(index,1,QTableWidgetItem(grades[1]))
                
                for i in range(2,5) :
                    item = QTableWidgetItem(grades[i])
                    item.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)
                    self.gradeTable.setItem(index,i,item)

                total1 = int(grades[2])
                total1 += int(grades[3])
                total1 += int(grades[4])
                
                avg1 = int(total1 / 3)
                
                print(total1,avg1)
                
                self.gradeTable.setItem(index,5,QTableWidgetItem(str(total1)))
                self.gradeTable.setItem(index,6,QTableWidgetItem(str(avg1)))
#         
#         except:
#             pass
            
        
        
    def setTableHedaer(self):
        column_header = ["학번","이름","국어","영어","수학","총점","평군"]
        self.gradeTable.setHorizontalHeaderLabels(column_header)
        
        
    def getNum(self):
        lines = 0
        
        try:
            with open('./grade.txt','r',encoding='UTF-8') as f2 :
                readLine = f2.readlines() # 파일 전체를 읽어서 라인단위로 잘라 list로 
                lines = len(readLine)
        except:
            lines = 0
            
        return lines
        
if __name__=="__main__" :

    app = QApplication(argv)
    gradeList = GradeList()
    gradeList.getGrade()
    exit(app.exec_())
