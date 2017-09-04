'''
Created on 2017. 9. 4.
@author: callor
'''
from time import *

# 현재 날짜와 시간을 표시
# RTC 장치로 부터 읽기
curtime = asctime() # 문자열 시각
print(curtime)
print(type(curtime))

curtime = time() # float
print(curtime)
print(type(curtime))

curtime = localtime(time())
print(curtime)
print(type(curtime))
print(curtime)

