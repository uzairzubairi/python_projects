#!/usr/bin/env python3
import string

#Get the user to input all three of the ages
age1=int(input("Enter the first age:\t"))
age2=int(input("Enter the second age:\t"))
age3=int(input("Enter the third age:\t"))

if age1 > age2 and age1 > age3:        #check if age1 is oldest
    print(f"Oldest is {age1}")
elif age2 > age1 and age2 > age3:       #check if age2 is oldest                                
    print(f"Oldest is {age2}")
elif age3 > age1 and age3 > age2:      #check if age3 is oldest                                 
    print(f"Oldest is {age3}")