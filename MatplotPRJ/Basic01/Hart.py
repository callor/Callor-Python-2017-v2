'''
Created on 2017. 9. 12.

@author: callor
'''
from matplotlib.pyplot import *
from pylab import *

x = linspace(-1.6,1.6,10000)
f = lambda x: (sqrt(cos(x)) * cos(200*x) + sqrt(abs(x))-0.7) * pow((4-x*x),0.01)
plot(x, list(map(f,x)))
show()