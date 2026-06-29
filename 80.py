N = int(input("Введите количество элементов: "))
a = list(map(int, input("Введите элементы списка: ").split()))
count = 0
for i in range(N-1):
    if (a[i] + a[i+1]) % 2 == 0:
        count += 1
print(f"Количество подотрезков: {count}")