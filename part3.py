#!/usr/bin/env python3

import string


print ("Price Comparison")
print ()

#collects info about price for 64oz and 32oz
price_64oz=float(input("Price for 64oz size:\t\t"))
price_32oz=float(input("Price for 32oz size:\t\t"))

#calculates unit price
unit_price_64oz=round(price_64oz/64,2)
unit_price_32oz=round(price_32oz/32,2)


#print all the calculated info
print()
print(f"Price per oz (64oz):\t\t{unit_price_64oz}")
print(f"Price per oz (32oz):\t\t{unit_price_32oz}")
