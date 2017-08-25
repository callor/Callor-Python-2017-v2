'''
Created on 2017. 8. 24.
Define Module

@author: callor
'''
# Define Module
#  함수들만의 묶음으로 되어 있는 모듈
#  필요하지 않으면 스크립트 변수를 선언하지 않는다.
#  스크립트 변수는 모두가 public 이기 때문에
def f1(num1, num2):
    return num1 + num2

def f2(num1, num2, num3):
    return num1 + num2 + num3


def paramF(num1, num2, list1):
    # 일반적인 방법
    num1 = 100
    num2 = 200
    
    # 파이썬코드 방식
    num1,num2 = 100,200

    list1.append("1")
    list1.append("2")
    list1.append("3")
    list1.append("4")
    list1.append("5")
    list1.append("E")



# 스크립트 상에 선언 변수
# 무조건 public
myname = "__main__"
# __name__ = "__main__"

# 시스템 변수, magic value
#     __ 로 시작되는 여러가지 변수들
# 함수선언부와 호출위치가 같은 모듈이면
#    __name__ = "__main__" 
print("__name__",__name__)

# 함수 자신을 호출하는 코드스크립트
# 다른 모듈에서 import 하는 순간 실행되지 않도록 하기 위한 코드
if __name__ == "__main__" : # true

    # f1과 f2를 테스트 하는 코드
    print(f1(10,20))
    print(f2(10,20,30))
    
    





