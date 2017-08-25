'''
Created on 2017. 8. 21.
@author: callor
'''

s = """
우리나라
대한민국
"""
print(s)

s = "우리나라\n대한민국"
print(s)

s1 = ["가나","나다","라마"]
j1 = "" . join(s1) # 문자열을 연결
print(j1)

j1 = ",".join(s1)
print(j1)


s1 = j1.split(",") # 컴마를 기준으로 분리
                # 결과물은 List
                
print(s1)

s1 = "Republic-Korea"
d1,_,d3 = s1.partition("-")

# 별도 라인에 표시
print(d1)
print(d3)

# 한줄에 표시
print(d1,d3)

# %s : String %d : DEC
p = "이름 : %s 나이 %d"  # % ("홍길동",20)

print("이름:", "홍길동", "나이:" ,20)
print(p % ("홍길동",20))

p = "나이 : %3d"
print(p % 2)
print(p % 5)
print(p % 20)
print(p % 100)

p = "나이 : %03d"
print(p % 2)
print(p % 5)
print(p % 20)
print(p % 100)

p = "나이 : %-3d"
print(p % 2)
print(p % 5)
print(p % 20)
print(p % 100)

p = "X = %0.3f, Y = %10.2f"
print(p % (3.141562, 3.141592))

s = "이름:{0} 나이:{1}"
print(s.format("홍길동",20))

s ="이름:{name} 나이:{age}"
print(s.format(name="홍길동",age=20))











