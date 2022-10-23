n = 0
CORRECT_PIN = 5162

while n <3:
    pin = int(input("Enter the PIN code: "))
    
    if pin != CORRECT_PIN:
        print("Incorrect...")
        n += 1
    else:
        print("Correct PIN")
        break
        
if n == 3:
    print("Sorry your payment card has been blocked")
