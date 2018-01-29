# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#==============================================================================
# #
# varA = 'abcd'
# varB = "ab"
# if (type(varA)==str or type(varB)==str):
#     print("string involved")
# elif varA > varB:
#     print("bigger")
# elif varA == varB:
#     print("equal")
# elif varA < varB:
#     print("smaller")
# 
iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 



