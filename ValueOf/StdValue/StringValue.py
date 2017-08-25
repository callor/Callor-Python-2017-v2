'''
Created on 2017. 8. 21.
@author: callor
'''
s = "korea"
char1 = 'A' # 16진수 2자리 8bit, 1 Byte 공간에 1글자 할당
string1 = 'KOREA' # 5byte 저장공간을 예약 한 byte에 한글자씩 할당
string1 = "KOREA\0" # \0 None 값 , 포인터 개념

i = 1 # 변수 = class = object 
print(type(i)) # int Value,  int class

s = "KOREA"
print(type(s)) # String Class str class


i = 1 
i = 2 # 원래있던 1을 쫒아내고 2를 할당
i = 3 # 원래있던 2를 쫒아내고 3을 할당

# 재 할당을 하면 메모리 공간이 새로 예약되고 사용된다.
s = "K"
s = "O" # 원래있던 O를 쫒아내는게 아니고,
        # 다른 공간에 저장예약을 하고, s가 가리키는 곳을 변경
s = "R"

# 문자열 연속으로 여러줄 표현할때
# Raw String
s = '''우리나라
대한민국
Republic of Korea
'''
print(s)

# ESCAPE 문자 : 특수한 효과를 내기 위한 코드
# \n New Line 
s = "우리나라\n대한민구\nRepublic of Korea"
print(s)

# \t tab
s = "우리나라\t대한민국\tRepublic of Korea"
print(s)

path = "c:\test\test.txt" 
print(path)

# r 문자열내의 모든 ESC 문자를 무시하고 RawString 취급하라
path = r"c:\test\test.txt"
print(path)

s = ["c:","test","test.txt"]
print(",".join(s))

s = "KOREA"
s = ("k","O","R","E","A") # tuple
print(s)

# [a:b] a번째 부터 b-1번째까지
print(s[1:3])
























