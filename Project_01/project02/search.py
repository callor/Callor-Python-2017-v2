'''
Created on 2017. 8. 31.
@author: callor
키보드로 입력받은 
문자열에서 자음 또는 모음만 걸러내는 방법
'''
vowellist = ['a','e','o','u','i','A','E','O','U','I']
vowelString = "aeouiAEOUI"

# text 중에 모음의 개수
# 문자열을 list로 변환한 다음에 찾기
def vowel0(text):
    count = 0
    textlist = list(text) # 문자열을 list 자료형으로 바꾸기
    for i in range(len(textlist)) : # len 문자열의 길이
        if textlist[i] in vowellist :
             count += 1
    print("모음의 개수:",count)

# text 중에 모음의 개수
def vowel1(text):
    count = 0
    for i in range(len(text)) : # len 문자열의 길이
        if text[i] in vowellist : # list에서 찾기
             count += 1
    print("모음의 개수:",count)

def vowel2(text):
    count = 0
    for i in range(len(text)) :
        if text[i] in vowelString : # 문자열에서 찾기
            count += 1
    print("모음의 개수:",count)

# txext 중에 자음의 개수
def consonant(text):
    count = 0
    for i in range(len(text)) : # len 문자열의 길이
        if text[i] not in vowellist :
             count += 1
    print("자음의 개수:",count)
    
    
    
    
strInput = input("영문 문자열을 입력하세요>>")
vowel1(strInput)
consonant(strInput)














