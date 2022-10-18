#!/usr/bin/env python3
import string

print ("Change Calculator")
print ()

continueProgram="y"

while continueProgram == "y" or continueProgram=="Y":

    price=int(input("Enter number of cents:\t\t"))            #the user inputs the number of cents
    print()
    quarters=0
    dimes=0
    nickels=0
    pennies=0
    if price >= 25:                                         #calculate the nubmer of quarters
        for i in range(25, price+1, 25):
            
            quarters+=1
            price-=25
    
    if price >= 10:                                         #calculate the number of dimes from the remaining amount
        for i in range(10, price+1, 10):

            dimes+=1
            price-=10
   
    if price >= 5:                                          #calculate the number of nickels from the remaining amount
        for i in range(5, price+1, 5):
            
            nickels+=1
            price-=5
   
    if price >= 1:                                          #calculate the number of pennies from the remaining amount
        for i in range(1, price+1):
            
            pennies+=1
            price-=1

    print(f"Quarters:\t\t{quarters}")
    print(f"Dimes:\t\t\t{dimes}")
    print(f"Nickels:\t\t{nickels}")
    print(f"pennies:\t\t{pennies}")

    continueProgram=input("Continue? (y/n):\t\t")           #ask user if he wants to continue or not
    print()
 