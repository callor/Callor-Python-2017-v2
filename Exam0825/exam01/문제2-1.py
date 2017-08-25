'''
Created on 2017. 8. 25.

@author: callor
'''
a = "Hello World"
a = "hi " + a[6:]
print(a)

b = "Hello World"
print(type(b))

b = "Hi " + b[6:]
print(b)

a = "abcdef"
a = a[1:] + a[0]
print(a)
