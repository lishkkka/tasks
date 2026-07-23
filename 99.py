N = int(input("Введите количество элементов: "))
a = list(map(int, input("Введите элементы списка: ").split()))
m = 1
count = 1
for i in range(1, N):
    if abs(a[i] - a[i - 1]) == 1:
        count += 1
        if count > m:
            m = count
    else:
        count = 1
print(f"Максимальная длина: {m}")