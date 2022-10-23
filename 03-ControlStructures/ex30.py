num_of_primes = int(input("Enter the amount of prime numbers: "))
num_is_prime = False
is_running = True

def isPrime(number):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                return False
        return True
    else:
        return False
            
def primeGenerator(size):
    num = 2
    print("Prime numbers: ", end="")
    while size:
        if isPrime(num):
            print(num, end=" ")
            size -=1
        num += 1

while is_running:
    if num_of_primes <= 0:
        print("Invalid input")
        num_of_primes = int(input("Enter the amount of prime numbers: "))
    else:
        primeGenerator(num_of_primes)
        is_running = False        