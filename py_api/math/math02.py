'''
Created on 2017. 9. 4.
@author: callor
'''
from math import *

# math.pi 내장 상수
print(pi)

# math.e 자연로그  내장 상수
print(e)

# n >= 3.14인 가장 적은 자연수를 반환(올림연산)
n = ceil(3.14)
print(type(n))
print(ceil(3.14))
print(ceil(3.52))
print(ceil(-3.52))

# m <= 3.14인 가장 큰 정수(내림연산)
print(floor(3.14))

# 버림연산
print(trunc(3.14))

# 뒷수에서 부호만 복사해서 앞에 부착
print(copysign(6.5,-0.0))
print(6.5 * (-1))

# float 절대값
print(fabs(-6.5))

# 5! 계산
print(factorial(5))

# mod 함수 결과가 실수
print(fmod(3,2))
print(3%2) # 정수
print(3.2 % 2)      # 1.2000000000000002

# % 의 정밀도를 높이기 위해 
print(fmod(3.2,2))  # 1.2000000000000002
print(fsum([1,2,3])) 

print(modf(3.14))





