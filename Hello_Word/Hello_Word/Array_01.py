'''
Array : 다수의 값들을 관리하는 방법
    py:Collection
    1. set
    2. dic
    3. list
    4. tuple
'''

'''
set의 정의
    값들이 중복 될수 없다.
    
'''
myset = {1,2,3,4,5,6}
print(myset)

myset.add(8);
print(myset) # 1개만 추가할때

myset.update({9,8,7}) # 8은 기존값이 있어서 추가 되지 않는다.
print(myset)

myset.remove(3) # 3을 제거
myset.clear() # 전체 삭제


'''
dict
   key:value 가 쌍으로 있는 값들의 집합
   json(javascript object notation)
   map 형태
'''
mydic = {"이름" : "홍길동", "나이" : 20, "주소" : "광주시"}
print(mydic)

print(mydic["이름"]) # mydic의 key값이 이름인 항목을 보여라
mydic["나이"] = 30 # 항목의 내용을 변경

age = mydic['나이'] # 나이의 value를 age 라는 변수에 할당(복사)
print(age) # age에 복사된 값을 출력
keys = mydic.keys() # 객체 메서드(일반 함수와 분리해서 사용하는 개념)
print(keys)

del mydic['주소'] # 주소항목을 삭제

keys = mydic.keys() # mydic 에서 key들을 배열로 추출
print(keys)

values = mydic.values() # value(값)들을 배열로 추출
print(values)

items = mydic.items() # dic를 list 로 변환
print(items)

age = mydic.get("나이") # py 2.x 에서 사용하던 method
age = mydic['나이'] # 3.x에서 사용하는 방법

mydic.clear() # 모두 삭제
print(mydic)

'''
List 
자유롭게 어떤 데이터라도 취급가능한 배열
'''
mylist = [] # list 생성
mylist = ['AB',1,'대한민국',True, False] #
print(mylist) 
print(mylist[0]) # 맨처음 list
print(mylist[3]) # 4번째 항목
print(mylist[4]) # 존재하지 않는 부분의 값을 요구

mylist.append("Korea") # 추가
del mylist[3] # 4번째 항목 삭제
 
mylist.append(1)
mylist.append(2)
mylist.append(3)
mylist.append(4)
mylist.append(5)

print(mylist)

# 기존 list에서 중복값을 제외한 배열을 얻기 위한 방법
mylist = [1,2,3,4,5,6,3,4,5]
myset = set(mylist) # list값을 set으로 변환
print(myset) # 중복된 값을 제와한 결과만 list로 변환


'''
slice
   list의 특정 부분을 잘라내기
'''
# 3번 위치부터 6-1까지
mylist1 = mylist[3:6]
print(mylist1)

# 0부터 6-1번째까지
mylist1 = mylist[:6]
print(mylist1)

# 3번부터 끝까지
mylist1 = mylist[3:]
print(mylist1)

'''
tuple
    만든 후 추가, 삭제가 불가능한 자료형
    다양한 형태의 자료 중복 가능
'''

mytuple = ("AB",1,False)
print(mytuple)

myNotuple = (123) # 이것은 tuple 아니다, 정수형 변수
mytuple = (123,) # 값이 1개일때는 끝에 컴마(,)를 넣어야 tuple이 된다.















