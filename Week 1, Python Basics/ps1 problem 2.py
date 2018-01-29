# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 17:31:31 2017

@author: fuadg
"""
#Given a string s of lower case characters
#find the number of times the string 'bob' occurs in s
s = 'azcbobobegghakl';
index = 0
counter = 0
for char in s:
    index += 1
    if char == 'b':
        if (index+1) < len(s):
            if s[index] == 'o' and s[index+1] == 'b':
                counter += 1
print("Number of times bob occurs is: "+ str(counter))