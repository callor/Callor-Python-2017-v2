'''
Created on 2017. 9. 5.

@author: callor
'''

a = [1,3,1,3,14]

# a list의 각 요소를 2제곱하여 새로운 리스트 생성
b = [ x**2 for x in a ]
print(type(b))
print(b)

# 셋으로 변경하면 중복된 값이 삭제 된다.
c = { x ** 2 for x in a}
print(type(c))
print(c)

from os import *
from glob import glob
# 모든 파일에 대한 목록을 g list로 생성
g = glob("*.*")

# 
# 파일의 사이즈가 1000  byte보다 큰 파일만 리스트 재 생성
f = [x for x in g if stat(x).st_size > 100] 
print(f)
# print([x for x in glob("*.*")])

# 
# 사전 구조 key : value 묶인 구조
d = {x:stat(x).st_size for x in g}
print(type(d))
print(d)
print(d['Comp01.py'])

# 사전에서 key와 value를 바꿀때 사용하는 트릭
print({value:key for key,value in d.items()})

for i in range(10):
    print(i)
else: # 정상적으로 모두 순회했을때
    print("x")











