def sum(n):
    sum_amount = 0
    for i in range(1, n+1):
        sum_amount += i
    return sum_amount

sums = sum(10)
print(sums)