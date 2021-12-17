# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 16:55:36 2021

@author: MinaJoh96

Guess the number 

"""

import random


#Introduction to game with name input
print("Welcome to Guess the number, what is your name?")
name = input()
print("Hello %s!" % name, "I'm thinking of a number between 1 and 10, care to guess?")

numb = random.randint(1,10)
for guesses in range(6):

    guess = input()
    guess = int(guess)
    
    if guess > numb: 
        guesses =+1
        print("To high!")
        
    if guess < numb:
        guesses =+1
        print("To low!")
        
    if guess == numb: 
        break 

if guess == numb:
    print("Nice job! The number was %i" % numb)
    
if guess != numb:
    print("Nope, the number I was thinking of was %i" % numb)
