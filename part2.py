#!/usr/bin/env python3

import string


print ("Pay Check Calculator")
print ()

#collects info about hours and payrate
hours_worked=float(input("Hours worked:\t\t"))
hourly_payrate=float(input("Hourly PayRate:\t\t"))

#calculates taxes and gross pay and take home pay
tax_rate=0.18
gross_pay=hours_worked*hourly_payrate
tax_amount=tax_rate*gross_pay
take_home_pay=gross_pay-tax_amount

#print all the calculated info
print()
print(f"Gross pay:\t\t{gross_pay}")
print("Tax rate:\t\t18%")
print(f"Tax amount:\t\t{tax_amount}")
print(f"Take home pay:\t\t{take_home_pay}")
