#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 13:53:14 2020

@author: Okechukwu Egeruoh
"""
#The credit plan at TidBit Computer Store specifies a 10% down payment and an annual interest rate of 12%. 
#Monthly payments are 5% of the listed purchase price, minus the down payment. Write a program that takes the purchase 
#price as input. The program should display a table, with appropriate headers, of a payment schedule for the lifetime of the loan. 
#Each row of the table should contain the following items:

#the month number (beginning with 1)
#the current total balance owed
#the interest owed for that month
#the amount of principal owed for that month
#the payment for that month
#the balance remaining after payment.
#The amount of interest for a month is equal to balance * rate/12.
#The amount of principal for a month is equal to the monthly payment minus the interest owed

#Show annual interest, and monthly rate
MONTH_RATE = .12/12

ANN_INT = .12

Price = float(input(" purchasing price is ?: "))

#Display the down payment,payment, and original balance 
Payment = Price * .1

Balance = Price - Payment

payment = Balance * 0.05

#Display the Statement entered

print("Month", "Original Balance.", "Monthly Interest", "New Balance", "Principal", "Payment",)

# equation for month
month = 0
while Balance > payment:
  month += 1
  #Display interest, principal, the new balance
  interest = Balance * MONTH_RATE

  principal = payment - interest
  
  newBalance = Balance - principal

  print("%-1d%10.2f%12.2f%12.2f%7.2f%9.2f" % (month, Balance, interest, principal, payment, newBalance))

  Balance = newBalance  
  

payment=Balance
principal=payment
interest= 0
newBalance= 0
month = month + 1
newBalance= 0

print("%-1d%10.2f%12.2f%12.2f%7.2f%9.2f" % (month, Balance, interest, principal, payment, newBalance))



