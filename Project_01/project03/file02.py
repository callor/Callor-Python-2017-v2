'''
Created on 2017. 9. 1.
@author: callor
# 
## 
'''
from random import *
f = open("data.txt","w",encoding="UTF-8")
for i in range(100):
    i1 = randint(50,100)
    i2 = randint(50,100)
    i3 = randint(50,100)
    
    str = "%d:%d:%d\n" % (i1,i2,i3)
    f.write(str)

f.close()
print("파일 저장 완료")    



