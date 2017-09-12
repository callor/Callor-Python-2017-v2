'''
Created on 2017. 9. 12.

@author: callor

Bar 그래프 그리
'''
# numpy array 생성
from numpy import *
x = array([0,1,2,3,4,5,6,7,8,9])
y = array([9,8,7,8,7,6,6,5,5,4])

from matplotlib.pyplot import *
figure() # pyplot 를 이용해서 그래프를 시작하겠다 선언
bar(x,y) # x, y array를 이용해서 그래프를 그려라
show()  # 그래프를 화면에 보여라