# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 19:21:58 2022

@author: Emon
"""
a = 5            # Variable Declaration and initialization 
b = 10.0000 
c = 2
print(a)        # print variable
print(type(a))  # see data type 
print(type(b))
print(a-c)
print(a+c) 
print(a**2)   # power 
print(b//2)   # return only integer value 

t = True 
f = False
print (t and f) #logical and  
print (t or f)  # logical or
print (not f)   #negation 
print (t != f)  # xor 

print("Emon")
print('Jakaria')  # print string

print(""" Jakaria 
      Islam 
      Emon""")  # can formate the string 
      
print('a = {}'.format(a))
print('a = ' + str(a))
print('a = %d' % a)
print(f'a = {a}') 

if a>0 :
    print('positive')
elif a<0: 
    print('Negative')
else:
    print("Zero")
    
for i in range(1,10):   # range(start, stop, inc/dec)  default start value 0, inc/dec value 1 
    print(i, end = " ") # stop is exclusive (n-1), start is inclusive.     

# for i in range(10, 0): crete a infinite loop
# beacuse inc/dec has a default value of +1 . we need to explicitelty mention dec

for i in range (10,0, -1):
    print(i, end = " ")
    