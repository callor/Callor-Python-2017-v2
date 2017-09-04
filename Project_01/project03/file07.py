'''
Created on 2017. 9. 1.

@author: callor
'''
# text 파일 복사
with open("data2.txt","w",encoding="UTF-8") as target:
    with open("data.txt","r",encoding='UTF-8') as source :
        target.write(source.read())

print("파일을 복사 했습니다.")


