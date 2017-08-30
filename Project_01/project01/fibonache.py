'''
Created on 2017. 8. 30.
@author: callor
'''
'''
1+2 로 시작되는 피보나치 수열 표현
'''
first = 1
second = 2
print(first,second)
for i in range(10) :
    nextNum = first + second
    print(nextNum)
    first = second
    second = nextNum