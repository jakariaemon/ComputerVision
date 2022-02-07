# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 19:45:40 2022

@author: Emon
"""
#list  #tupple # dictionary 
""" list is sequential data
can hold on to different data types
this is mutable. 
Mutable means changeable (update operation allow) 
use the square bracket to create a list """ 
l = [1,2, 'a', 'b']
print(l, type(l))
print(l[0])
print(l[-1])

for i in l:
    print(i)
    
for i in range(3):
    v = l[i]
    print(f'[{i}]: {v}') 
    
for i,v in enumerate(l):
     print(f'[{i}]: {v}')
     
l.append('c') # add at the end of the list, only one at a time
print(l)


l[-1] = 'emon'  # negative indexing
print(l)

# insert(desired location index, value)
l.insert(2, 'jakaria')
print(l) 

#insert does not overright the existing value 
#it shift 1 index and add

# remove by value (only one value remove) 
#it scan left to right and remove the first match
l.remove('a')
print(l)  

# remove using index
del l[3]
print(l)

