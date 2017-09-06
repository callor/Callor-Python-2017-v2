'''
Created on 2017. 9. 6.
@author: callor
상수(Const) != 변수
변수 : 저장되는 공간
상수 : 고정된 값


'''
from sympy import *

# 상수선언 
STR_NATION = 'KOREA'
strNation = "K"

a = STR_NATION
b = STR_NATION
c = STR_NATION

if a == b :
    print("맞다")

# sympy 상수

print(3+4j) # 일반파이썬에서 복소수 표현
print(3+4*I) # sympy 복소수 표현 I 허수 반드 *I

# 복소수는 크기 비교가 안된다
'''
if (3+4j) > (3+5j) :
    print("맞다")
'''
# evalf : 매크로(정상적인 코드가 아닌 문자열 형태의 코드) 실생
print(pi.evalf())

a = "3+4"
print(a)

# 문자열의 계산식을 코드로 변환시켜서 연산
# print(a.eval()) : 7

# 자연로그
print(E.evalf())

# 무한대 표현
print(oo.evalf())

# 음의 무한대
print(-oo.evalf()) # zoo










