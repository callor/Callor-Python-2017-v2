'''

Created on 2017. 9. 7.
@author: callor

'''
class ExamClass():

    # python 전용툴에서는 매개변수가 없는 생성자를
    # 자동으로 작성해 주지만
    # eclipse에서는 가급적 명시해주는 것이 좋다.
    def __init__(self):
        pass
    
    def print_nation(self):
        print("Korea")

a = ExamClass()
a.print_nation()


# ExamClass를 상속
#    기존에 잘 디자인된 Class의 모든 기능을 그대로 수용하는 것
#    기존코드에 없는 새로운 기능을 추가해서
#        마치 기존 코드를 복사한후 새로운 코드를 생성한 것처럼 사용할수 있다
#  클래스 재사용 2번
class ExamClass01(ExamClass):

    # 상속한 경우는 SuperClass를 명시적으로 호출해 주어야 한다.
    def __init__(self):
        ExamClass.__init__(self)

    def print_name(self):
        print("홍길동")


b = ExamClass01()
b.print_nation()







