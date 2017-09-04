'''
Created on 2017. 9. 1.

@author: callor
'''
with open("year2017.png","wb" ) as target :
    with open("2017.png","rb") as source :
        target.write(source.read())
        
print("파일 복사 완료")