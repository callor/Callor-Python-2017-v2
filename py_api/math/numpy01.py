'''
Created on 2017. 9. 6.

@author: callor
'''
from numpy import *

a = [1,2,3,4,5]

# 2 Dimension Array
# 빌딩구조
# 행렬분석

# rank : 차원
# shape : 요소
a1 = [ [1,2],[2,3],[3,4] ]

list = [1,2,3,4]

# numpy.array()
arr = array(list) # 리스트를 배열로 변환
print(type(arr))
print(arr.shape) # 결과값이 tuple로 반환, arr.shape
# print(arr.rank) # arr.rank
 
# 겹침 리스트를 2차원 Array로 변환
b1 = array([ [1,2,3,4],[2,2,2,2],[3,4,5,6] ])
print(b1.shape)

print(b1[0,1]) # 결과 : 2

# 배열 생성 구조를 tuple로 넣어 준다.
z1 = zeros( (2,3) ) # 2,3 배열을 만들되 값을 모두 0으로
print(z1)

o1 = ones( (3,3) )
print(o1)


f1 = full( (2,3), 5)
print(f1)

e1 = eye(5)
print(e1)

# range() : 리스트를 만드는 함수
# range(10) : 0 부터 9까지 연속된 값을 갖는 리스트
a1 = array(range(20)) # 20개의 배열을 만들고
print(a1)

# 20개의 배열을 재 배열
print(a1.reshape( ( 4,5) )) # x*y 의 값은 전체와 같게
a2 = array(range(20)).reshape( ( 5,4) )
print(a2)
# print(a2.reshape( (2,3) ))
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]
 [16 17 18 19]]
'''
# a = b[0:3]
a3 = a2[0:3,0:2] # slice
print(a3)

















    