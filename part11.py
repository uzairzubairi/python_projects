#!/usr/bin/env python3
import string

 
print ("Table of powers")
print()

startNum=int(input("Enter start number:\t\t"))              #user inputs start number
endNum=int(input("Enter end number:\t\t"))                  #user inputs end number

while startNum>endNum:                                          #check if the start number is smaller than end number or not
    print("Start number must be smaller than the end number! Try again please.")
    startNum=int(input("Enter start number:\t\t"))
    endNum=int(input("Enter end number:\t\t"))

print("Number\t\tSquared\t\tCubed")
print("=======\t\t======\t\t======")
for i in range(startNum,endNum):                            #calculate the square and cube of all the numbers and print it
    squared=i**2
    cubed=i**3
    print(f"{i}\t\t{squared}\t\t{cubed}")
 

 