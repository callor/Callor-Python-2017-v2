'''
Created on 2017. 9. 7.
@author: callor
'''
class ExamClass():
    
    # property 클래스 내부에 선언된 변수, member 변수
    old = -1
    name = ""
    
    # 셍성자 Contruct
    def __init__(self,name,old):
        self.name = name
        self.old = old
        
    # User Define Method
    def print_name(self):
        print(self.name)
        
    def print_age(self):
        print(self.old)



# 객체(Object) 생성
s = ExamClass("홍길동",20)
s.print_name()

def exFunc(aa):
    print













