'''
Created on 2017. 9. 12.

@author: callor
'''
a = [10,20,20,30,40,50,60,70]
label = ["Blue","Green","Red","Cyan","Magenta","Yello","Black","White"]

from matplotlib.pyplot import *
figure()
pie(a,labels=label)
# b,g,r,c,m,y,k,w
show()