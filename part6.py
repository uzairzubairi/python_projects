#!/usr/bin/env python3
import string

#Get the user to input all three of the sides
side1=int(input("Enter the first side:\t"))
side2=int(input("Enter the second side:\t"))
side3=int(input("Enter the third side:\t"))

if side1 == side2 and side2 == side3:        #check if the sides are equal. If they are, print that they are.
    print("The triangle is equilateral")
else:                                        #otherwise, print not equilateral
    print("The triangle is not equilateral")