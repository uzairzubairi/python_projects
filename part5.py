#!/usr/bin/env python3
import string

print ("Letter grade converter")
print ()

willContinue="y"
#use a while loop to check if the user wants to continue putting in more grades, the loop runs as long as user enters y
while willContinue.lower()=="y":
    enteredGrade=int(input("Enter numerical grade:\t")) # user enters the first grade
    if enteredGrade > 88 and enteredGrade < 100:        # "if" checks if its between 88 and 100, if it is, A grade is shown
        print("Letter grade: A")
        willContinue=input("Continue? (y/n):\t")        #user is asked if he wants to continue, if user enters y, loop will run again
    elif enteredGrade > 80 and enteredGrade < 87:
        print("Letter grade: B")
        willContinue=input("Continue? (y/n):\t")
    elif enteredGrade > 67 and enteredGrade < 79:
        print("Letter grade: C")
        willContinue=input("Continue? (y/n):\t")
    elif enteredGrade > 60 and enteredGrade < 66:
        print("Letter grade: D")
        willContinue=input("Continue? (y/n):\t")
    elif enteredGrade < 60:
        print("Letter grade: F")
        willContinue=input("Continue? (y/n):\t")
print("Bye!")

