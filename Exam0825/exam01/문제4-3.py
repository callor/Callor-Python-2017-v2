'''
Created on 2017. 8. 25.
@author: callor
'''


def bmi_test(height, weight):
    height = height / 100
    bmi = weight / (height ** 2)
    
    if bmi < 18.5 :
        print(bmi, "마른체형")
    elif bmi >= 18.5 and bmi < 25.0 :
        print(bmi,"표준")
    elif bmi >= 25.0 and bmi < 30.0 :
        print(bmi,"비만")
    elif bmi >= 30.0 :
        print(bmi,"고도 비만")
        
height = 169
weight = 70

bmi_test(height, weight)


def bmi_test1(height, weight):
    height = height / 100
    bmi = weight / (height ** 2)
    
    if bmi < 18.5 :
        print(bmi, "마른체형")
    elif bmi < 25.0 :
        print(bmi,"표준")
    elif bmi < 30.0 :
        print(bmi,"비만")
    elif bmi >= 30.0 :
        print(bmi,"고도 비만")
        
bmi_test1(169, 70)
        
        
        
        
        
        
        