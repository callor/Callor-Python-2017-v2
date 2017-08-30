'''
모듈
   1. 단순 호출용
   2. 값을 주고 일만 시키는 용도
   3. 값을 주고 일을 시키고 결과를 받는 용도
   4. 값은 주지 않고 단순 호출을 하고, 결과를 받는 용도
'''
# 단순 호출용
def inputF():

    # prompt 사용자의 입력을 대기하는 상태
    # blocking, 프로그램의 흐림이 멈춘상태
    num = input("숫자를 입력하세요>> ")
    print(num)
    
# inputF()
# 값을 주고 일만 시키는 용도
def inputF1(num):
    print(num)
    
# 값을 주고 일을 시키고 결과를 받는용도
def inputF2(num1, num2):
    return num1 + num2

#  값을 주지 않고 일을 시키고 결과를 받는 용도
def inputF3():
    return "우리나라만세"

'''
숫자를 문자열로 강제 형변환
'''
a = 3
b = "KOREA" 
c = b + str(3) #숫자를 문자열로 강제 형변환
print(c) # 결과를 KOREA3

a = "3"
b = 4
c = int(a) + b # 숫자를 강제 형변환 시켜야한다
print(c)# 3+4인 7이라는 결과를 얻고

a = "4"
b = 5
c = a * int(b) # 문자열과 숫자를 곱셈 오류
print(c)

# c = a / b

# Dict 를 list 변환시켰을때 어떤 결과 나오는지 확인
prodDict = {
    "포도주스":800,
    "코카콜라":950,
    "코코팜":700,
    "비락식혜":650,
    "밀키스":88}

# (key,value) => tuple
prodList = prodDict.items()
print(prodList)
print(type(prodList))

for i in prodList:
    print(type(i))
    print(i[0]) # key
    
for i in prodList:
    print(i[1]) # value
















