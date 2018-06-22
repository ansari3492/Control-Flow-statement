# -*- coding: utf-8 -*-
"""
Created on Mon May 14 19:00:53 2018

@author: Lenovo
"""
nums=input("entere the number: ").split(',')

list1 = [int(x) for x in nums]
minValue = min(list1)
maxValue = max(list1)

list1.remove(minValue)
list1.remove(maxValue)

print (sum(list1))

print (sum(list1)/len(list1))