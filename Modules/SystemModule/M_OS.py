'''
Created on 2017. 8. 24.

@author: callor
'''
import os

# 물리적인 파일의 폴더 위치값
print(os.getcwd())
mydir = os.getcwd()

# 현재 폴더에 있는 파일들의 목록
print(os.listdir())

fileList = os.listdir()
for f in fileList:
    if f == "M_OS.py" :
        print("현재 디렉토리에 M_OS.py이 있음")

        
from os import *
print(getcwd())
mydir = os.getcwd()

print(os.listdir())

fileList = os.listdir()
for f in fileList :
    if f == "M_OS.py" :
        print("현재 디렉토리에 M_OS.py이 있음")

# 파일 path 는
#     윈도우에서는 C:\temp
#     리눅스 등에서는 C:/temp
fileList = os.listdir("C:/test")
fileList = os.listdir("C:\\test")
print(fileList)

# fileList class에 포함된 변수와 method 목록
print(dir(fileList))

korea = 100
use = 200

usa = 300
usa += 200

print(korea + usa)



        
