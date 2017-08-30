'''
Created on 2017. 8. 30.
@author: callor
'''
'''
자판기 구현
  1. 돈을 투입하고,
  2. 상품 선택
     상품은 1-5까지 상품
     각 상품은 고유의 금액이 정해짐
  3. 투입된 금액과 상품의 금액 비교해서
  4. 투입된 금액 > 상품금액
     상품을 지급, 잔액표시
     not : 잔액이 부족메시지
'''

prodName =  ["포도주스","코카콜라","코코팜","비락식혜","밀키스"]
prodPrice = [800,950,700,650,880]

def vending(cost, prodChoice):
    
    # 투입한 금액보다 선택한 상품가격이 작거나 같으면
    if prodPrice[prodChoice-1] <= cost :
        print(prodName[prodChoice-1],"상품:",prodPrice[prodChoice-1],"원에 구입" )
        print("잔액:",cost - prodPrice[prodChoice-1])
    
while True:
    cost = int(input("금액을 입력하세요>>"))
    prodChoice = int(input("상품을 선택하세요>>"))
    if cost == 0 :
        break
    vending(cost,prodChoice)

print("판매가 종료되었습니다")


def vent(cost,choice):
    if choice == 1 :
        if 800 < cost :
            print("포도주수 판매")
    elif choice == 2:
        if 950 < cost :
            print("코카콜라 판매")
    elif choice == 3:
        if 700 < cost :
            print("코코팜 판매")
    elif choice == 4:
        if 650 < cost :
            print("비락식혜 판매")
    elif choice == 6:
        if 880 < cost :
            print("밀키스 판매")







