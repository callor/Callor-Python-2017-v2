'''
Created on 2017. 9. 7.
@author: callor

class : OOP
    고전적 프로그래밍 언어
        C 와 같은 언
        함수, 변수의 개념으로 프로그래밍
            함수 : 기능을 수행하는 묶음
            변수 : Data
        연결고리 : 매개변수, 리턴값
        유지보수 문제
            함수, 데이터의 관계가 불명확함에 따라 발생되는 문제
            상당히 크게 나

    Object Oriented Programming
        class : 함수(method) + 데이터(member, property)를 묶어서 처리
            property : class에 종속된 데이터이고, 외부에서 접근하려면
                가급적 method를 통해서 접근 하도록 제한
                
            method
              1. property에 접근하는 통로
              2. property를 이용해서 어떤 기능을 수행하는
              
        클래스
            Dog
                1. 형태, 특징(property) : 다리4, 털, 귀쫑긋 
                2. 동작(method) : rum, eat, bark
            
            책상
                1. 형태, 특징(property) : 나무, 사각형, 다리
                2. 동작(mthod) : 사람이 끌어야 움직인다.
                
    Function O P 
'''

# 함수선언
def myfunc():
    print("Korea")
    
# class 선언
#     User define Variable(사용자 정의형 자료형)
#     기본자료형 : 숫자, 문자, 컬렉션
class ExamClass() :

    # 생성자
    def __init__(self, name, age):
        self.name = name 
        self.age = age

# 객체(object)
# class를 object, instance 로 생성

s = ExamClass("철수",20) # 나만의 특별한 형태를 갖는 변수
print(type(s))


a = [1,2,3,4,5]
for i in a:
    print(i)


b = 0
# 오류 int 형은 for 반복문의 소스로 사용 불가
# for i in b:
#     print(i)
























