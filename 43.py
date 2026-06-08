n = int(input("Введите натуральное число: "))
max1 = -1
max2 = -1
while n > 0:
    x = n % 10
    if x > max1:
        max2 = max1
        max1 = x
    elif x > max2 and x != max1:
        max2 = x
    n //= 10
if max2 == -1:
    print("нет")
else:
    print(max2)