'''
Created on 2017. 9. 12.
@author: callor
'''
from numpy import *
a = array([1,2,3,4,5])

from matplotlib.pyplot import *
figure()
plot(a)
show() # python blocking

# matplot 내부에서 list를 numpy array 변경하여 처리
plot([1,2,3,4,5,6,7,8,9])
show()

