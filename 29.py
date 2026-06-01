N = int(input("Введите натуральное число: "))
n = 0
for i in range(1, N + 1):
    n += i
print(f"Сумма чисел от 1 до {N} = {n}")