'''
Created on 2017. 8. 22.

@author: callor
'''

'''
산술연산자
   사칙연산자 : + - * / 
   제곱연산자 : **
   나머지 연산자 : % 
   나누기에서 소수점 이하를 버리는 연산자 : //

'''
print(3//2) # 몫을 구하는데 편리하게 사용
print(3%2) # 나머지 연산자

'''
비교 연산자 = 관계연산자
    값들의 크기 비교
    ==, > < , <= >=
    같지 않음 : !=

'''
s = 3
if s != 3 :
    print("같지 않다")
else :
    print("같다")
    
if s == 3 :
    print("같다")
else :
    print("같지 않다")
    
    
 
'''
할당연산자
  변수에 어떤값을 할당하기 위해 사용
'''
s = 3 # = 할당 연산자
s = s * 2 # 원래 s 값에 2를 곱해서 다시 s 에 할당
s *= 2 # 축약형 할당연산자

s = 0
s += 1 # 1을 증가 하라
#s++  python은 해당 없음

'''
논리연산자
  결과를 True False 판단하는 연산자
  
  합성연산자
      and or not
'''
x = True
y = False
'''
x        y        x and y         x or y
-------------------------------------
                     *               +
True     True         True         True
True     False        False        True
False    True         False        True
False    False        False        False
-----------------------------------------
'''
if x and y :
    print("YES")
else :
    print("NO")

# 결과 : NO

'''
Bit
  어떤 값을 2진수로 변환해서 각각의 자리 값을 비교

3 : 0011
4 : 0100

3 or 4 : 0111  3 | 4
3 and 4 : 0000 3 & 4
'''
    
'''
맴버십 연산자
    포함연산자
    a 에 어떤 값이 포함되어 있는가 판단
    컬렉션을 대상으로 사용하는 연산자
'''

a = [1,2,3,4,5,6,7]
for i in a :
    if i == 3 :
        print("있다")
        
if 3 in a  :
    print("있다")
else :
    print("없다")


if 3 not in a :
    print("없다")
else :
    print("있다")

'''
indentity 연산자
'''
s = "KOREA"
print(type(s))

i = 1
print(type(i))

if s is i : # s와 i 의 object type 이 같은가
    print("같다")
else :
    print("다르다")
    
if s is not i :
    print("다르다")
else :
    print("같다")



 
    
    
    
    
    
    
    