'''
Created on 2017. 8. 31.
@author: callor
'''
vowellist = ['a','e','o','u','i','A','E','O','U','I']
vowelString = "aeouiAEOUI"

# 입력받은 문자열 중에서 모음만, 자음만 추출해서 보여주기
def getVowel0(text):
    textlist = list(text)
    vowel_letter = ""
    for i in range(len(textlist)) :
        if textlist[i] in vowellist :
            vowel_letter += textlist[i]

    print("모음들:",vowel_letter)


def getVowel(text):
    vowel_letter = ""
    for i in range(len(text)) :
        if text[i] in vowellist :
            vowel_letter += text[i]

    print("모음들:",vowel_letter)
    

def getVowel2(text):
    vowel_letter = ""
    for x in text :
        if x in vowelString :
            vowel_letter += x
    print("모음들:",vowel_letter)
    

def getLetter(text):
    vowel_letter = ""
    conson_letter = ""

    for i in text :
        if i in vowelString :
            vowel_letter += i

    for i in text :
        if i not in vowelString :
            conson_letter += i


def getLetter1(text):
    vowel_letter = ""
    conson_letter = ""

    for i in text :
        if i in vowelString :
            vowel_letter += i
        if i not in vowelString :
            conson_letter += i


def getLetterEach(text):
    vowel_letter = ""
    conson_letter = ""

    for i in text :
        if i in vowelString :
            vowel_letter += i
        elif i != " " :
            conson_letter += i

    print("모음들:", vowel_letter)
    print("자음들:", conson_letter)

    
s = "Republic of Korea"
getVowel(s)
getVowel2(s)
getLetterEach(s)









