#user input
amount = float(input("Enter the amount in PLN: "))

#vat calculation
vat = round(0.23 * amount, 2)

print(f"Amount  : {amount}")
print(f"VAT 23% : {vat}")