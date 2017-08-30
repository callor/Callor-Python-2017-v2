'''
Created on 2017. 8. 30.
@author: callor
솟수 : 1과 자신 이외로 나누어지 않는 수
'''
def is_prime(x):
    if x < 2: # prime 수는 2 미만의 수는 의미가 없다
        return False 
    
    if x == 2:
        return True

    else:
        for i in range(2,x):
            if x % i == 0 :
                return False
        return True
num1 = 101
if is_prime(num1): # == True는 생략할 수 있다
    print(num1,"은 소수입니다")
else :
    print(num1,"은 소수가 아닙니다")
    
    
def is_primeEach(x):
    result = True
    if x < 2 :
        result = False
        
    for i in range(2,x):
        if x % i == 0:
            result = False
            break
    return result

# 1 부터 100까지 숫자중에서 prime수가 무엇인가 출력
for i in range(101) :
    if is_primeEach(i) :
        print(i,"는 솟수입니다")

# 1부터 250까지의 수중 솟수들의 합을 구하시오
sum = 0 
for i in range(251):
    if is_primeEach(i) :
        sum += i

print("합계",sum)






