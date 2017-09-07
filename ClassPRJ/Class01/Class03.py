'''
Created on 2017. 9. 7.

@author: callor
'''
sum01 = 0
def addF(a):
    global sum01 # 값을 유지시키도록, public 변수
    sum01 += a
    print(sum01)
    
sum02 = 0
def addF2(a):
    global sum02 # 값을 유지시키도록, public 변수
    sum02 += a
    print(sum02)

def myF1():
    addF(3) # 3
    addF(5) # 8
    addF(6) # 14

def myF2():
    addF2(3) # 3
    addF2(5) # 8
    addF2(6) # 14



myF1()
myF2()

class MyClass() :
    sum01 = 0

    def __init__(self,a):
        self.sum01 = a

    def add01(self,a):
        self.sum01 += a
        
    def print_sum(self):
        print(self.sum01)
    
'''
객체 a와 객체 b는 같은 MyClass를 이용해서 생성되었지만
내부에서 작동될때는 전혀 다른 객체가 된다.

객체의 재사용 1번방법
    이미 만들어진 Class로 부터 각각의 instance를 생성하여
    사용하는 방법
        코드의 중복 작성을 막는 방법
'''
a = MyClass(3) # 객체 a
a.add01(3)
a.add01(5)
a.add01(6)
a.print_sum()

b = MyClass(3) # 객체 b
b.add01(3)
b.add01(5)
b.add01(6)   
b.print_sum() 
    
    
    
    
    

