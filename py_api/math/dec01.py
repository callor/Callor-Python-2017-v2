'''
Created on 2017. 9. 4.
@author: callor
'''
from decimal import *

# 파이썬에서 실수 저장하는 방법
# 32 bit 공간에 실수저장
#     왼쪽 1비트 : 부호비트
#       0 : 양수, 1 :음수
#    1 - 8 : 지수부
#    23 : 가수

print(0.1) # 0.1000000000001
print(1/3)

print((1234.567 + 45.678) + 0.004)
print(1234.567 + (45.678 + 0.004))
print(Decimal(3))

# int('1.1') 문자열입력으로 인한 오류
print(Decimal('1.1') + Decimal(3))

# 부호값, (숫자값), 소수점
c = ( 0, (3,1,4),4)
print(Decimal( c ))








