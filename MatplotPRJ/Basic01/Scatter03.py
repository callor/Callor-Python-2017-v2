'''
Created on 2017. 9. 12.

@author: callor
'''
from numpy import *

t = array([0,1,2,3,4,5,6,7,8,9])
y = array([9,8,7,8,7,6,7,6,5,4])


from matplotlib.pyplot import *
colormap = t

figure()
scatter(t,y,s=50,c=colormap,marker="<")
show()