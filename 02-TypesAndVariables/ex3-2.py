input1 = input("Enter Hours: ")
input2 = input("Enter rate: ")

try:
    hours = float(input1)
    rate = float(input2)
    complete_payment = 40 * rate
    if hours > 40:
        amount = hours - 40
        new_pay_rate = amount * 1.5 * rate
        complete_payment += new_pay_rate
        
    print(f"Pay: {complete_payment}")
except:
    print("Error. Enter a numeric value")
    
