#!/usr/bin/env python3
# Created by: Anastasia Friedenstein Patino
# Created on: November. 5, 2023
# Program that calculates the total, subtotal and discount amount of a product.

price_per_unit_as_string = input("Enter a the price per unit: ")

# Try catch to make sure they enter a valid imput and if not it doesn't crash
try:
    price_per_unit_as_float = float(price_per_unit_as_string)
    amount_of_units_as_string = input("Enter a the amount of units: ")
    try:
        amount_of_units_as_int = int(amount_of_units_as_string)
        tax_as_string = input("Enter a the tax persentage (ex:15): ")
        try:
            tax_as_int = int(tax_as_string)
            subtotal = amount_of_units_as_int * price_per_unit_as_float
            if subtotal >= 1000:
                discount_amount = subtotal / 100 * 10
                total_before_tax = subtotal - discount_amount
                tax_amount = total_before_tax / 100 * tax_as_int
                total = tax_amount + total_before_tax
                print(f"Subtotal:{subtotal}")
                print(f"Discount amount: {discount_amount}")
                print(f"Total: {total}")
            else:
                print(f"Subtotal: {subtotal}")
                tax_amount = subtotal / 100 * tax_as_int
                total = tax_amount + subtotal
                print(f"Total: {total}")
        except ValueError:
            print("Please enter a valid tax")
    except ValueError:
        print("Please enter a valid amount")
except ValueError:
    print("Please enter a valid price")
