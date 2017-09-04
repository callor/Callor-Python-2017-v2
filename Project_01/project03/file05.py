'''
Created on 2017. 9. 1.
@author: callor
'''
def grade(num1,num2,num3):
    sum01 = num1 + num2 + num3
    avg01 =sum01 / 3
    
    str = "%3d+%3d+%d3=%3d, %3d" % (num1, num2, num3, sum01, avg01)
    print(str)

    
if __name__ == "__main__" :    
    with open("data.txt","r",encoding="UTF-8") as f :
        lines = f.realines() # 파일을 모두 읽어서\n 단위로 나누어 list로 반환
        for line in lines :
            items = line.split(":")
            grade(int(items[0]), int(items[1]),int(items[2]))











