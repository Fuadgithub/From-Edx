# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 21:58:24 2017

@author: fuadg
"""
low = 0;
high = 100;
guess = int((low+high)/2);
print("Please think of a number between 0 and 100!")
print("Is your secret number",str(guess) + "?")
response = input("Enter 'h' to indicate the guess is too high. \
Enter 'l' to indicate the guess is too low. \
Enter 'c' to indicate I guessed correctly. ")

while not(response == 'h' or response == 'l'or response == 'c'):
    print("Sorry, I did not understand your input.")
    print("Is your secret number",str(guess) + "?")
    response = input("Enter 'h' to indicate the guess is too high. \
Enter 'l' to indicate the guess is too low. \
Enter 'c' to indicate I guessed correctly. ")

if response == 'c':
    print("Game over. Your secret number was: ",guess)

while response != 'c':
    if response == 'h':
        high = guess
        guess = int((low+high)/2)
        print("Is your secret number",str(guess) + "?")
        response = input("Enter 'h' to indicate the guess is too high. \
Enter 'l' to indicate the guess is too low. \
Enter 'c' to indicate I guessed correctly. ")
        
        while not(response == 'h' or response == 'l'or response == 'c'):
            print("Sorry, I did not understand your input.")
            print("Is your secret number",str(guess) + "?")
            response = input("Enter 'h' to indicate the guess is too high. \
Enter 'l' to indicate the guess is too low. \
Enter 'c' to indicate I guessed correctly.")
        if response == 'c':
            print("Game over. Your secret number was: ",guess)
            break
    else:
        low = guess
        guess = int((low+high)/2)
        print("Is your secret number",str(guess) + "?")
        response = input("Enter 'h' to indicate the guess is too high. \
Enter 'l' to indicate the guess is too low. \
Enter 'c' to indicate I guessed correctly. ")
        
        while not(response == 'h' or response == 'l'or response == 'c'):
            print("Sorry, I did not understand your input.")
            print("Is your secret number",str(guess) + "?")
            response = input("Enter 'h' to indicate the guess is too high. \
Enter 'l' to indicate the guess is too low. \
Enter 'c' to indicate I guessed correctly. ")
        if response == 'c':
            print("Game over. Your secret number was: ",guess)
            break
        
