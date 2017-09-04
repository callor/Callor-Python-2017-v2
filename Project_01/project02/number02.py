'''
Created on 2017. 8. 31.

@author: callor
'''
from random import *

# 리스트 생성할때
alist = list()
alist = []

for i in range(10) :
    rnd = randint(1,100)
    alist.append(rnd)
    
print("=" * 30)
print("난수 List")
print(alist)

# 정렬(sort) : ASC DES

print("-" * 30)
print("역순만들기")
alist.reverse() # 역순만들기
print(alist)

print("-" * 30)
print("오름차순 정렬")
alist.sort() # ASC 정렬, 오름차순 정렬
print(alist)

print("-" * 30)
print("내림차순 정렬")
alist.sort( reverse = True ) # ASC 정렬, 오름차순 정렬
print(alist)








