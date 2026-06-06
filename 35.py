N = int(input("Введите натуральное число N: "))
print(f"Делители числа {N}:")
for i in range(1, N + 1):
    if N % i == 0:
        print(i, end=" ")