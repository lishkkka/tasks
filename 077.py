N = int(input("Введите количество элементов: "))
a = list(map(int, input("Введите элементы списка: ").split()))
m = 0
count = 0
for i in range(N):
    if a[i] % 2 == 0:
        count += 1
        if count > m:
            m = count
    else:
        count = 0
print(f"Максимальная длина: {m}")
