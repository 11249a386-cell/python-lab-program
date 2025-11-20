def sum(x, y):
    s = 0
    for i in range(x, y + 1):
        s = s + i
    print('Sum of integers from', x, 'to', y, 'is', s)

sum(1, 25)
sum(50, 75)
sum(90, 100)
