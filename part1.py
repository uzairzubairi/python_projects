#!/usr/bin/env python3

import string


print ("Registration Form")
print ()

first_name=input("First name:\t\t")
last_name=input("Last name:\t\t")
birth_year=input("Birth year:\t\t")


print(f"Welcome {first_name} {last_name}!")
print("Your registration is complete.")
print (f"Your temporary password is: {first_name}*{birth_year}")