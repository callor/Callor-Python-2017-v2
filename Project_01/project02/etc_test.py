'''
Created on 2017. 8. 31.

@author: callor
'''

charlist = ['a','e','i','o','u']
s = 'a'

# list 목록중에 in 앞의 글자(문자, 문자열)
print("b" in charlist) # in 포함연산자
print( s in charlist)
print( s in "korea")  # 문자열이 내부적으로는 list 형태로 저장 될것이다

for i in charlist:
    print(i)
    
s = "korea"
l = list(s)
# 3번 위치부터 끝까지 문자열 slice
print(s[3:])
print(l[3:])