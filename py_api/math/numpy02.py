'''
Created on 2017. 9. 6.

@author: callor
'''
from numpy import *

# print(a,end='')

a1 = array(range(5))
b1 = array([False,True,False,True,False])

c1 = a1[b1]
print(c1)

a1 = array(range(100))
b1 = ( a1 % 2 == 0 ) # 짝수 골라내기

c1 = a1[b1] # 짝수만 골라내기
print(c1)

# a1 배열중에서 짝수만 보여주기
print(a1[ a1 % 2 == 0])