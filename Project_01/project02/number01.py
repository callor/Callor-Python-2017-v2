'''
Created on 2017. 8. 31.
@author: callor
'''

'''
random() 함수 :
    임의 범위에서 난수를 발생시키는 함수
'''
from random import *

numlist = list() # 공백 리스트 생성

# 1부터 100까지 임의 숫자를 발생시켜서 list로 만들기
# 유사난수 : 난수의 빈도가 일정한 값에 치우친다.
for i in range(100) :
    rnd = randint(1,100)
    numlist.append(rnd)

for i in numlist :
    print(i)

# 위에서 만든 list 중에 내가 키보드로 입력한 숫자가 몇개 있는가
#     발견되는가 찾기
def numSearch(num1):
    
    numlist = list()
    for i in range(100) :
        rnd = randint(1,100)
        numlist.append(rnd)

    count = 0
    for i in numlist:
        if i == num1 :
            count += 1
    print(num1,"은",count,"개 있음")

        
num1 = int(input("1부터 100까지 중 숫자 입력 >> "))    
numSearch(num1)


# 1부터 10까지 임의 난수를 100개 만들고
# LIST에 담은 후
# 키보드에서 1부터 10까지 값을 입력 받은 후
# 난수 LIST를 검색하여
# 개수와 합계를 구하시오

numlist = list()
for i in range(100):
    rnd = randint(1,10)
    numlist.append(rnd)
    
def searchNum(num):
    count = 0
    sum = 0
    for i in numlist :
        if num == i :
           count += 1
           sum += i
           
    print("개수:",count)
    print("합계:",sum)
    
    
num1 = int(input("1부터 10까지 숫자 1개 입력>>"))
searchNum(num1) 









        
        
        
        
        
        
        
        