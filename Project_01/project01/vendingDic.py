'''
Created on 2017. 8. 30.
@author: callor
'''
prodDict = {
    "포도주스":800,
    "코카콜라":950,
    "코코팜":700,
    "비락식혜":650,
    "밀키스":88}

prodList = prodDict.items()
print(type(prodList))

def vending(cost,choice):
    
    count = 0 
    for p in prodList :
        count += 1
        if count >= choice:
            prodName = p[0]
            proPrice = p[1]
            if proPrice <= cost :
                print(prodName , "상품:",proPrice, "원에 판매")
                print(cost - proPrice, "원 거스름돈")
            break

print("=" * 30)
print("상품목록")
print("-" * 30)

# dict에서 key값 리스트만 추출하는 함수
num = 0
for p in prodDict.keys():
    price = prodDict[p] # key값으로 value를 추출
    num += 1
#     strMsg = "{0} : {1}\t = {2}".format(num,p,price)
    strMsg = " %d : %s\t  =  %3d" % (num,p,price)
    
#     print(num," : ",p," : ",price)    
    print(strMsg)

print("=" * 30)
choice = int(input("상품을 선택하세요>>"))
cost = int(input("금액을 투입하세요>>"))
vending(cost, choice)















