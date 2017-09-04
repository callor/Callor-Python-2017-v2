'''
Created on 2017. 9. 4.

@author: callor
'''
from datetime import *
from time import *

# 그레고리안 달력기준
curtime = time()
# 년월일
curdate = date.fromtimestamp(curtime)
print(curdate)
print(curdate.year) # 연도
print(curdate.month) # 월
print(curdate.day) # 일

# 년월일, 시각
curdatetime = datetime.fromtimestamp(curtime)
print(curdatetime.year)
print(curdatetime.month)
print(curdatetime.day)

print(type(curdatetime.year))

print(curdatetime.hour)
print(curdatetime.minute)
print(curdatetime.second)
print(datetime.fromtimestamp(curtime).year)

curyear = curdatetime.year
curmonth = curdatetime.month
curday = curdatetime.day

from calendar import *
cal = month(curyear, curmonth)
print(cal)







