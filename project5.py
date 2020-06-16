#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 14:26:45 2020

@author: okechukwu egeruoh
"""

#Write the encrypted text of each of the following words using a Caesar cipher with a distance value of 3:
#python
#hacker
#wow







Text = input(" encrypt message here:")
distance = int (input("distance is ?:"))
code = ""
for ch in Text:
  ordValue = ord(ch)
  cipherValue = ordValue + distance
  if cipherValue > ord('z'):
    cipherValue = ord('a') + distance - (ord('z') - ordValue + 1)
    code = code + chr(cipherValue)
  print(code)

code = input ("Enter the coded text:")
distance = int(input("Enter the distance value:"))
Text =""
for ch in code:
  ordValue = ord(ch)
  cipherValue = ordValue - distance
  if cipherValue < ord('a'):
      cipherValue = ord('z') - \
        (distance − (ord('a') − ordValue − 1))
      Text += chr(cipherValue)
print(Text)



