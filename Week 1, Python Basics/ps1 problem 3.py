# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 18:01:52 2017

@author: Fuad g Abdella
"""
#This program prints the longest substring of s in which the letters occur
#in alphabetical order. In case of ties, print the first substring
#If there are no letters in alphabetical order, print the first letter
#

s = 'lrqesdjilaazqxaqzlmgbsfp' # example
maxx = 0
temp = ''             #temporary string to contain the substrings
for index in range(len(s)-2):
    i = index
    while s[i] <= s[i+1]:
        temp += s[i]
        temp += s[i+1]
        i+=1
        if i > (len(s)-2):
            break
    if len(temp) > maxx:
        ending_index = i+1
        starting_index = index 
        maxx = len(temp)
    temp = ''    
if maxx == 0:
    print("Longest substring in alphabetical order is:",s[0:1])
else:    
    print("Longest substring in alphabetical order is:",s[starting_index:ending_index])
