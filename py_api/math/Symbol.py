'''
Created on 2017. 9. 5.
@author: callor

방정식
   미지수 존재
   미지수가 있는 연산
   0 = x * 3 + 2
   0 = x ** 2 + x + a
'''
from sympy import * 

# 미지수로 선언
x = Symbol('x') # 1개 미지수 선언
print( x + x + 3 )

# 다항식
x, y = symbols('x,y') # 2개 이상의 미지수 선언
print(x * y + x * y + x * y)

# 전개식
a = expand((x+1) * (x+2))
print(a)
print(type(a))

# 인수분해
b = factor(x**2 + 3*x+2)
print(b)

pprint(expand((x+1)*(x+2)))
p = 2 + 3*x + x**2

print('polynomial',end='')
pprint(p)

# 다항식 풀이
p = x **2 + 2 * x * y + y**2
print(p.subs({x:2, y:1}))

# 1차 방정식 풀이
e = 2 * x - 6 # 2 * x - 6 = 0
print(solve(2 * x - 6))

# 2차 방정식 풀이
e = x ** 2 + 3 * x + 2
print(solve(e)) # 리스트 형식으로 출력
print(solve(e,dict=True)) # 근을 dict 로 출력

# 허근 계산
e = x ** 2 + x + 1
print(solve(e,dict=True))

a,b,c = symbols("a,b,c")
e = a * x ** 2 + b * x + c

# a,b,c 는 상수,x에대한 방정식임을 명료하게 표현
print(solve(e,x,dict=True))
pprint(solve(e,x,dict=True))

# 연립방정식 풀이
e1 = x + 2 * y - 3
e2 = 3 * x - y + 2
print(solve((e1,e2),dict=True))













