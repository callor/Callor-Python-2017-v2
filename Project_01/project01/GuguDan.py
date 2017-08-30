'''
특정 숫자를 입력받아서
그 숫자에 해당하는 구구단을 출력
'''
def gugudan1(num1):
    print("=" * 15)
    print(num1,"단 구구단")
    print("-" * 15)
    for i in range(1,10):
        multi = num1 * i
        print(num1,"x",i,"=",multi)
    print("=" * 15)
    
while True:
    num1 = input("숫자를 입력하세요>>")
    print(type(num1))
    
    # 입력받은 숫자가 -1이면 종료
    if int(num1) == -1 :
        break
    
    gugudan1(int(num1))

print("종료되었습니다")













