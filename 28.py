N = int(input("Введите количество пар чисел: "))

for i in range(N):
    a = int(input(f"Введите первое число пары {i + 1}: "))
    b = int(input(f"Введите второе число пары {i + 1}: "))

    if a > b:
        print(f"Большее: {a}")
    elif b > a:
        print(f"Большее: {b}")
    else:
        print("Равны")