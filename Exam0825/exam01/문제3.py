'''
Created on 2017. 8. 25.

@author: callor
'''
naver_end_price = [474500, 461500, 501000, 500500, 488500]

max = 0
min = 1000000
for i in naver_end_price :
    if max < i :
        max = i 
    if min > i :
        min = i 

print("최대값:" , max)
print("최소값:", min)

print(max - min)