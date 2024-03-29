'''
Created on 2017. 8. 21.

@author: callor
'''
from sympy.core.tests.test_args import test_sympy__physics__quantum__cg__Wigner3j
'''
숫자관련 
   정수
   실수
저장공간 : 변수
  int v : 공간만 예약 어떤값이  
  float v
'''
s = 0 # 최초에는 값을 0으로 초기화
s = 100 # 정수형 변수가 되고, 값을 100으로 할당
s = 0 # 100이 쫒겨나고 0으로 다시 할당

s1 = None # 아무것도 아닌값 내부적으로 code 0 
s1 = ""  # None, Nothing, null 
s1 = " " # 공백

f1 = 3.2 # 실수
b1 = False # boolean


f1 = 1.6
print(int(f1)) # int 함수는 실수=>정수 바꾸는

i1 = 30 
print(float(i1)) # 정수를 실수로 바꾸는

print(int("3")) # 문자열로 표현된 숫자를 정수로

print("3" + "4") # 문자열을 연결

# 통신과정에서 주고 받는값 코드 단위 = 문자
# 숫자 = 문자열로 되어 서로 교환
print(int("3") + int("4")) 
print(float("3.5")) # 문자열을 실로 바꾸는

print(bool("False")) # 문자열을 boolean
print(bool("false"))

# bool 함수는 값이 숫자 0일때만 False 무조건 나머지는 True
print(bool(0))
print(bool("0"))

s1 = None
print(s1 is None) # s1이 None 인가 묻는 => True

# 파이썬은 복소수를 직접 지원하는 언어
v = 2 + 3j
print(v.real) # 실수부만 추출하는 member, 속성
print(v.imag) # 허수부만 추출하는 member, 속성

i = 1
j = 2
k = 3

i, j, k = 1,2,3 # 앞에서부터 순서대로 i = 1, j = 2, k = 3
print(i, j, k)


# 정수형, 저수준 숫자
hex1 = 0xFF # 16진수 255
oct1 = 0o70 # 8진수
bin1 = 0b001 # 이진수

# Raw Data 16진수 2자리의 연속된 값으로 표현하는 모든 Data 
# FF 99 00 F1

'''
16진수 : 2진수와 아주 친한 문자

    이진수    10진수
    0000         0        0
    0001
    0010
    0011
    0100
    1001         9        9
    1010        10        A
                          B
 
    1111         15       F
'''
# 지수형식 표현
print(3e5) # 3 * 10의 5승




























