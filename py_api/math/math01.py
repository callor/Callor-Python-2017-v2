'''
Created on 2017. 9. 4.
@author: callor
'''
from math import *

a = [1,2,3,4,5,6,7,8,9]
# iterable 자료의 총합을 구하는 내장함수
print(sum(a))

sum1 = 1+2+3
a = sum1
print(a)

# 6 + 1 + 2 + 3  + 4
print(sum([1,2,3,4],6))

# -5 + 1 + 2 + 3 + 4
print(sum([1,2,3,4],-5))

# -5 + 1
# 5/2 + 1 + -5
print(sum([1,-5],5/2))
print(sum([1,5/2],-5))

a = [4,12,31,231]
print(max(a))
print(min(a))

# 절대값
print(abs(-1))

# 제곱수 계산
# 2 ** 10
print(pow(2,10)) # float
print(2**10) # int

# 2 ** 10 % 2
print(pow(2,10))

# 반올림 , 2자리 이하에서 반올림
print(round(3.415,2))
print(round(3.424,0))
print(type(round(3.424))) # 정수형
print(type(round(3.424,0))) # 실수형

print(divmod(10,7)) # 몫과 나머지를 튜플로













