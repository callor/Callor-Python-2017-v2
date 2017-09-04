'''
Created on 2017. 9. 1.
@author: callor
'''
from random import *

# 쓰기모드 open
# 기존에 파일이 있으면 뒤에 연결해서( append )
with open("data1.txt","a",encoding="UTF-8") as f:
    for i in range(10) :
        data = randint(1,10)
        str = "%02d번째 줄 : %d\n" % (i,data)
        f.write(str)
print("파일 입력을 마칩니다")








