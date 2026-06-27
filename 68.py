N = int(input("Введите количество элементов: "))
a = list(map(int, input("Введите элементы списка: ").split()))
m = a[0]
for i in range(N):
    s = 0
    for j in range(i, N):
        s += a[j]
        if s > max:
            m = s
print(f"Максимальная сумма: {m}")