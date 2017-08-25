'''
Created on 2017. 8. 16.

@author: callor
'''

sum = 0

'''
range(n)
0 부터 n-1까지 반복실행
    0부터 10까지 덧셈
'''
for i in range(11) :
    sum += i 
    
print(sum)

mylist = ['A','B','C','D','E','F','G']
for s in mylist :
    print(s)

'''
mylist 항목중에서 C 가 있으면 찾았음 표시
'''
for s in mylist:
    if s == 'C' :
        print('찾았음')
        print(s)
        break

count = 0 
for s in mylist:
    count += 1
    if s == 'D' :
        print(count, "번째 위치")
        # print('%d 번째 위치' %(count))
        break # 최초의 찾은 위치만 표시할때
    

'''
0 부터 9까지
'''
for i in range(10) :
    print(i)

print('---------------------------')
'''
시작값과 종료값 지정
    10 부터 49까지 반복
'''
for i in range(10,50) :
    print(i)
    
print('--------------------------')
'''
시작값과 종료값 및 step을 지정
    1부터 10까지 2씩증가
''' 
for i in range(1,11,2):
    print(i)
           
for i in range(0,11,2):
    print(i)
   
    

    