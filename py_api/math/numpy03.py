'''
Created on 2017. 9. 6.

@author: callor
'''
from numpy import *

a = array([1,2,3])
b = array([2,3,4])

# 배열의 4칙연산

# 덧셈
print(add(a,b))

# 뺄셈
print(subtract(a,b))

# 곱셈
print(multiply(a,b))

# 나눗셈
print(divide(a,b))

# product
list1 = [
    [1,2],
    [2,3]
    ]

list2 = [
    [4,5],
    [3,2]
]

# product 연산
c = dot( array(list1), array(list2) )
print(c)

# array 전체 항목의 덧셈
print(sum(array(list1)))
print(sum(array(list1),axis=0)) # Column 끼리만 
print(sum(array(list1),axis=1)) # row 끼리만

# array 전체 항목의 곱셈
print(prod(array(list1)))
print(prod(array(list1),axis=0)) # Column 끼리만
print(prod(array(list1),axis=1)) # row 끼리만

















