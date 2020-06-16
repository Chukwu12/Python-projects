# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 18:38:57 2020

@author: Okechukwu
"""
#Project Description: SPY is a stock symbol that represents the famous S&P 500 used for benchmarking the stock market. 
#In this project, you are asked to write a program to do the following:to read historical data of SPY from the
#attached file called, "SPY.csv." to create a dictionary called SPY with the key using the date, associated with open price, 
#high price, low price, close price, and volume traded;to create a list called, "PriceChange," that contains the price changes 
#from the previous closing prices of the "SPY.csv"

SPY ={}
i=0 #rowa number of records
PriceChange=[]
#Read SPY.csv from downloads folder

f = open('C:/Users/HP/Desktop/cis 425 python/SPY.csv', 'r')  

for lines in f:
	SpyList=line.split(',')
	SPY[i]={}
	SPY[i]["date"]=SpyList[0]
	SPY[i]["open"]=SpyList[1]
	SPY[i]["high"]=SpyList[2]
	SPY[i]["low"]=SpyList[3]
	SPY[i]["close"]=SpyList[4]
	SPY[i]["volume"]=SpyList[6]

	if i > 0:
		closeDiff=float(SPY[i]['close'])-float(SPY[i-1]['close'])
		PriceChange.append(closeDiff)

		i+=1 #i=i+1


