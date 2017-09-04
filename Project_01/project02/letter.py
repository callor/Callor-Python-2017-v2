'''
Created on 2017. 8. 31.
@author: callor
'''

s = "Republic of Korea"
slist = list(s) # 문자열을 list로 변환
sreverse = ""
for i in range(len(slist)) :
    sreverse += slist[ (-1)-i ]

print(s)
print(sreverse)

sreverse = ""
for i in range(len(s)) :
    sreverse += s[(-1)-i]
    
print(s)
print(sreverse)



# list는 revers()함수를 이용해서 거꾸로 뒤집을 수 있다
print(slist)
slist.reverse() # slist자체를 뒤집기
print(slist)
# 출력 : ['a', 'e', 'r', 'o', 'K', ' ', 'f', 'o', ' ', 'c', 'i', 'l

# list를 문자열로 변환시키는 
srevers = ""
for i in slist :
    srevers += i
print(srevers)
# 출력 : aeroK fo cilbupeR
