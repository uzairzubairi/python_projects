#!/usr/bin/env python3

import string


print ("Travel Time Calculator")
print ()

#collects info about miles and miles per hour
miles=int(input("Enter miles:\t\t"))
miles_perhour=int(input("Enter miles per hour:\t\t"))

#calculates travel time
travel_time_hours=round(miles/miles_perhour)
travel_time_mins=miles%miles_perhour

#print all the calculated info
print()
print("Estimated Travel Time")
print(f"Hours:\t\t{travel_time_hours}")
print(f"Minutes:\t\t{travel_time_mins}")
