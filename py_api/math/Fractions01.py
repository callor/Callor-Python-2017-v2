'''
Created on 2017. 9. 4.
@author: callor
'''

from fractions import *

# 분수를 만드는 함수
# 앞:분자, 뒤:분모
f = Fraction(3,4)
print(f)
print(type(f))
f1 = Fraction(2,5)
print(f + f1)

# 분모는 0이 올수 없다.
f2 = Fraction(3,1)
