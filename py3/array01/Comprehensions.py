'''

Created on 2017. 9. 5.
@author: callor

Comprehentions
   Python의 독특한 기능
   array를 재 설정하는 기능

'''

a = [1,2,3,4,3,1,2,3,1,2,3]

for i in a:
    print(i)
    
# a list의 각 요소들에 + 3을 해서 새로운 List
b = []
for i in a:
    b.append(i + 3)
print(b)

b = [i+3 for i in a]
print(b)

# 고전적 언어방법
count = 0
for i in a :
    count +=1
    print(count, "번째 값:" , i)
    
# 파이썬 내장함수
for index,item in enumerate(a):
    print(str(index), "번 값:" , item)
    
    
    
    
    
    
    
    
    