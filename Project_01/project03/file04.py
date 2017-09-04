'''
Created on 2017. 9. 1.
@author: callor
'''
from random import *

f = open("data.txt","r",encoding="UTF-8")
f.close()


# 파일의 활동범위를 제한하는 with .. as 구문
with open("data.txt","w",encoding= "UTF-8") as f :
    for i in range(100) :
        i1 = randint(50,100)
        i2 = randint(50,100)
        i3 = randint(50,100)
        
        str = "%d:%d:%d\n" % (i1,i2,i3)
        f.write(str)
    
with open("data.txt","r",encoding="UTF-8") as f :
    while True:
        line = f.readline()
        if not line : break
        items = line.split(":")
        print(items)









    
    
    
    