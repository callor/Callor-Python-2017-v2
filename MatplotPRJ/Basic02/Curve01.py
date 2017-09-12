'''
Created on 2017. 9. 12.
@author: callor
'''
from numpy import *
from matplotlib.pyplot import *

# 
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname ="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family =font_name)

l = [1,2,3,4,5,6,7,8,9,0,1,2]
x = arange(0,12,0.01) # numpy(시작, 종료, step)
y = sin(x)

x1 = arange(1,12,0.01)
c = cos(x)

figure(figsize=(6,4)) 
# line width =3 
plot(x,y,'y',lw=3,label="sin") # 범례 label

# line 색상을 red
plot(x,c,"r", label="cos") # 범례 label
legend() # 범례 표시


# 그리드 포함
grid()

# 각축에 label 붙이기.
xlabel("시간")
ylabel("전압")
title("사인 그래프")


show()

















