#!/usr/bin/env python3
import string

#Quiz 2 Python - Uzair Zubairi
def display_menu():
    print ("=========================================================================")
    print ("\t\t\t\tBaseball Team Manager")
    print ("MENU OPTIONS")
    print("1 - Calculate batting average")
    print("2 - Exit program")
    print ("=========================================================================")

    menu_opt=int(input("Menu option: "))                                          #ask user to choose a menu option
    return menu_opt

def calc_average():
    print("Calculate batting average...")
    at_bat=int(input("Official number of at bats: "))
    hits=int(input("Number of hits: "))
    while hits>at_bat:
        print("Hits can not be more than at bats. Please try again.")
        at_bat=int(input("Official number of at bats: "))
        hits=int(input("Number of hits: "))
    bat_avg=hits/at_bat 
    return bat_avg

def main():
    menu_option=display_menu()
    while menu_option!=1 and menu_option!=2:                                       #check if the choice is valid
        print("Error! Invalid menu option selected. Try again.")
        menu_option=display_menu()

    while menu_option==1:                                                       #if option 1 is selected, call function to calculate average
        
        batting_avg=calc_average()                                       
        
        print(f"Batting average: {batting_avg}")
        print()
        menu_option=display_menu()                                      #ask again to choose a menu option
        while menu_option!=1 and menu_option!=2:
            print("Error! Incorrect menu option selected. Try again.")
            menu_option=display_menu()
        
    print("Bye!")                                                           #if option 2 is selected, exit program

if __name__ == "__main__":
    main()
