'''
Created on 2017. 9. 6.

@author: callor
'''
from sympy import *
x = Symbol('x')

# 대수 방정식 표현
print(solve( x**2-2 ))

# 미분
print(diff(exp(x) *  sin(x)))

# 적분
print(integrate(exp(x)*sin(x)+exp(x)*cos(x)))

# 극한
print(limit(sin(x)/x,x,0))



