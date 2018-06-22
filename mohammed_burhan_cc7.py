# -*- coding: utf-8 -*-
"""
Created on Mon May 14 13:23:12 2018

@author: Lenovo
"""
str1="www.google.com"
def char_frequency(str1):
    dict={}
    for n in str1:
         keys = dict.keys()
         if n in keys:
             dict[n] += 1
         else:
             dict[n] = 1
    return dict
print (char_frequency(str1))
