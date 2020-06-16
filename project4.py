# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 13:18:01 2020

@author: Okechukwu Egeruoh
"""
#In this project, you are asked to write a program that, given a seven-digit number, 
#generates every possible seven-letter word combination corresponding to that number. 
#There are 2,187 such combinations. Avoid phone numbers with the digits 0 and 1 9to which no
# letters correspond). See if your phone number corresponds to a meaningful word.

letters = ['','','','ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'QPRS', 'TUV', 'WXYZ']
digits = []
phone = input ('Enter a 7 digit phone number:\n')

for i in range (7):
    digits.insert(i, int(phone[i]))
    
for i in range(7):
    print(letters[digits[i]])