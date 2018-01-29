# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 17:23:59 2017

@author: fuadg
"""
s = 'azcbobobegghakl'
count = 0
for char in s:
    if char == 'a' or char == 'e' or char == 'i' \
    or char == 'o'or char == 'u':
            count += 1
print("Number of vowels: " + str(count))