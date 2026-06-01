N = int(input("Введите количество чисел: "))

for i in range(N):
    n = int(input(f"Введите целое число {i + 1}: "))

    if n % 2 == 0:
        print(f"{n} - четное")
    else:
        print(f"{n} - нечетное")