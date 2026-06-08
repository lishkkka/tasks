n = int(input("Введите натуральное число: "))
N=n
r = 0
while n > 0:
    r = r * 10 + (n % 10)
    n //= 10
if N == r:
    print("Да")
else:
    print("Нет")