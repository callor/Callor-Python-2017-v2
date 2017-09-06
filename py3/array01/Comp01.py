'''
Created on 2017. 9. 5.

@author: callor
'''
from os import *

print(getcwd()) # 현재 디렉토리(폴더)보여주는 os 함수
# OS에 관계없이 구분문자로 / 사용할 수 있다.
# \n 
# chdir("C:/bitWork/bit201708LeeSJ")
print(getcwd())


from glob import glob
# 현재 디렉토리의 파일 목록을 리스트로 만들어주는 함수
print(glob("*.*")) # 와일드 카드

# 파일의 와일드 카드
# * : 모든 것
#    *.* : 모든 파일
#    *.py : 확장자가 py인 모든 파일
#    *test*.py : 파일이름에 test가 있는 py 파일들

# ? : 영,숫자 1개와 대치
#    ??test.py : test 앞에 임의의 영,숫자 2개가 있는 파일들

a = glob("*.py")
print(type(a))
print(a)

from time import localtime
for i in a:
    metadata = stat(i)
    makeTime = metadata.st_mtime
    ltime = localtime(makeTime)
    print(i, ltime.tm_year,ltime.tm_mon,ltime.tm_mday)

    
    
    
    
    
    
    