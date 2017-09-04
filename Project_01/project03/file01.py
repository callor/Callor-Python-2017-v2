'''
Created on 2017. 9. 1.
@author: callor

파일의 입출력(Read, Write)은 OS하고 파이썬하고 통신

1. 연결 : open(읽기용, 쓰기용)
    OS -> 파일 핸들(handle, ID값)
2. 읽고 쓰기
3. 닫기
'''
# 파일을 쓰기위해서 여는 방식
# f : 파일 핸들값, ID 값이 있다
# 파일을 열때 배타적, 공유방식
f = open("text.txt","w",encoding="UTF-8")

# 직접 파일에 기록하는 상태 아니고
# 파일에 저장하전 buffer에 보관하는 상태
for i in range(10):
    str = "%02d번째 줄입니다\n" % (i+1)
    f.write(str) 
    
# 읽기용으로 열면 close()하지 않아도 문제발생확률이 낮으나
# 쓰기용으로 열면 반드시 close() 해야 합니다.
#   쓰기한 내용이 파일에 기록되지 않을 수 있습니다
# buffer에 있는 내용을 파일에 기록하고 파일 핸들을 반납

f.close() # flush 역할


# print(dir())
    

# 쓰기위해 열린 파일을 읽기위해 다시 연다.
f1 = open("text.txt","r",encoding="UTF-8")
data = f1.read()
print(data)












