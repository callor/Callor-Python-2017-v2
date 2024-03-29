'''
Created on 2017. 8. 22.
@author: callor
'''

'''
For 구문 : 순서, 개수에 따라서 반복
While 구문 : 조건(비교, 관계, 논리)에 따라 반복
'''

'''
조건을 명시하고,
그 조건이 거짓될 수 있도록 어떤 연산을 해 주어야 한다.
    그렇지 않으면 무한 반복
'''
i = 1
while i <= 10 : # 비교 연산결과가 참인동안 반복
    print(i) # i 값이 무한이 출력
    i = i + 1 #  i > 10이 되도록 연산을 해서 while을 끝낼 수 있도록


s = 0     
while True :
    print(s)

    # 내부에서 연산을 진행하고,
    # 별도로 조건을 검사해서
    # 강제로 중단    
    s += 1
    if s > 10 : break
    
s = 0     
while True :
    if s > 10 :
        print(s)
        break
        # continue # 무조건 다시 처음으로 돌아가라
    elif s > 5 :
        print(s)
        # continue
        
#     else :
    s += 1
    

    
'''
For는 처음부터 실행될 횟수를 지정하고 시작
'''
for i in range(10) : # 대표적인 for 반복 구문    
    print(i)
    
# range(start, end-1, step )
for i in range(0,10,1) :
    print(i)
    
list = ["This","is", "a", "book"]
for s in list : # 컬렉션의 개수만큼 반복
    print(s)
    
    
for s in list :
    print(s)
    if s == "is" : break # 조건에 따라 강제 중단
# 출력 : This, is
    
for s in list :
    if s == "is" :
        print(s)
        break
# 출력 : is
    

# 0부터 99까지 1씩 증가된 값을 갖는 Array
# for 와 같은 반복문을 처리하기 위한 Array
numbers = range(0,100,1) # 같은 범위의 range를 여러번 사용할때
print(type(numbers))

for i in numbers :
    print(i)

for a in numbers :
    print(i)    
    
    
    
    
    
    
    
    
    
    
    
    