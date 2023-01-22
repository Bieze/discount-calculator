#!/usr/bin/python3


price = input("Put in your original price (will automatically add $): ")
disc = input("Put in the discount (plain number): ")


discount = int(disc) / 100
cut = discount * round(float(price))
newPrice = round(float(price)) - int(float(cut))
print(f"What you pay: ${newPrice}")
print(f"How much you saved: ${cut}")