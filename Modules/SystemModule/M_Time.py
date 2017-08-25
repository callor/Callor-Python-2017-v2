'''
Created on 2017. 8. 24.
@author: callor
'''
import time

# 1970년 1월 1일 00시 00분 00초 부터 흐른 밀리세컨트
print(time.time())
print(time.ctime())

curtime = time.ctime()
print(curtime)

from time import * 
print(time())
# 시간함수
print(ctime())

curtime = ctime()
print(curtime)