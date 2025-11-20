num = int(input("Please enter the number: "))
sum = 0
x = num

while num > 0:
    d = num % 10
    num = num // 10
    sum = sum + (d * d * d)

if x == sum:
    print("The number", x, "is an Armstrong Number")
else:
    print("The number", x, "is not an Armstrong Number")
