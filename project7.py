#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 15:25:45 2020

@author: Okechukwu Egeruoh
"""

#part 1 - Writing data.text file
f = open 
f.write ('If this happens, then that happens that is not good')
f.close()

#Part 2 - Reading data.txt
f = open('data.txt', 'r')
text=f.read()
print("This is what is read from data.txt\n\n", text)
f.close()

#part3 - Split each word in data.txt
wordList = text.split()
print(wordList)

#part4 sorting items 
wordList.sort()
print("Sorted List looks like this:\n\n", wordList)

#Part5 removing redundant words in the list 

#function to get unique items
def unique(list1):
    uniqueWordList=[]
    
#Traverse for all words in the wordlist
    for item in list1:
        if item not in uniqueWordList:
            uniqueWordList.append(item)
        print("Here is the unique words in the list:\n\n", uniqueWordList)
unique(wordList)


