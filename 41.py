n = int(input("Введите натуральное число: "))
m = 0
while n > 0:
    c = n % 10
    if c > m:
        m = c
    n //= 10
print(f"Наибольшая цифра:", m)