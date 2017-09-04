'''
Created on 2017. 9. 1.
@author: callor
'''
def grade(kor,eng,math):
    sum01 = kor + eng + math
    avg01 = sum01 / 3
    result = "%3d + %3d + %3d = %3d, %3d" % (kor,eng,math, sum01, avg01)
    print(result)

f = open("data.txt",'r',encoding="UTF-8") 

# txt = f.read() # 파일 전체를 통째로 읽어 들이기
# 30:40:50\n30:70:60

'''
**************** // 0번줄을 읽고, next() 함수가 실행
**************** // 1번줄을 읽게
***************** // 마지막줄을 일고 next()
그다음 readline() : -1 =>False로 변환시켜준다.
'''

while True:
    line = f.readline() # new line 단위로 읽기
    if not line :      # 읽어들인 값이 없으면 False 갖는다.
        break
    
    # 읽은 결과로 어떤 처리를 하려면 여기에서
    items = line.split(":") # 한줄의 읽은 값을 : 기준으로 나눈다
    grade(int(items[0]),int(items[1]),int(items[2]))









