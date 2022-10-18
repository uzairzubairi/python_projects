#!/usr/bin/env python3
import string

print ("=============================================================")
print ("Shipping Calculator")
print ("=============================================================")

continueProgram="y"

while continueProgram == "y" or continueProgram=="Y":
    itemCost=round(float(input("Cost of items ordered:\t\t")),2)        #user inputs cost of items

    while itemCost<=0:                                                  #check to make sure its a positive value. if not, ask input again
        print("You must enter a positive number. Please try again.")
        itemCost=round(float(input("Cost of items ordered:\t\t")),2)

    shippingCost=round(float(input("Shipping Cost:\t\t\t")),2)          #ask user for shipping cost
    totalCost=round(itemCost+shippingCost,2)                               #calculate total cost

    print(f"Total cost:\t\t\t{totalCost}")                      #print total cost

    continueProgram=input("Continue? (y/n):\t\t")           #ask user if he wants to continue or not
    print ("=============================================================")
 