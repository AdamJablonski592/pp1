hours = float(input("Enter Hours: "))
rate = float(input("Enter rate: "))

complete_payment = 40 * rate
if hours > 40:
    amount = hours - 40
    new_pay_rate = amount * 1.5 * rate
    complete_payment += new_pay_rate
    
print(f"Pay: {complete_payment}")