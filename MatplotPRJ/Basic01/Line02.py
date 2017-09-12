'''
Created on 2017. 9. 12.

@author: callor
'''

# x 과 y 좌표 값을 설정해서 그래프 그리기
year = [1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009]
pop = [100,300,200,500,450,550,600,700,900,1000,1100]

from matplotlib.pyplot import *

# pythond IDE 생략해도 되나 
figure()

# list를 내부적으로 numpy array 변경해서 처리
plot(year,pop)
show()
