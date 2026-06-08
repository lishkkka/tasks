n = int(input("Введите натуральное число: "))
for x in range(10):
    count = 0
    N = n
    while N > 0:
        if N % 10 == digit:
            count += 1
        N //= 10
    print(f"Цифра {x} встречается {count} раз(а)")