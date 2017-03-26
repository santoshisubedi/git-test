n, sum = 0, 0

while n < 5:
    value = input('Enter Number %s: ' % (n + 1))
    sum = sum + float(value)
    n += 1

print('Sum = %.2f' % sum)