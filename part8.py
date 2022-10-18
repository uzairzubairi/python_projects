#!/usr/bin/env python3
import string

print ("Tip Calculator")
print ()
price=float(input("Cost of meal:\t\t"))           #user inputs the cost of the meal
print()

for i in range(15,30,5):                            #run a loop to calculate and print the 3 tip options
    tip=round(float(i/100),2)
    tipCost=round(float(price*tip),2)               #calculate the tip in dollars
    totalPrice=round(float(price+tipCost),2)        #calculate the total price including the tip
    print(f"{i}%")                                  #print all the info, in the next 4 lines
    print(f"Tip Amount:\t\t{tipCost}")
    print(f"Total amount:\t\t{totalPrice}")
    print()