N = int(input("Введите количество элементов: "))
a = list(map(int, input("Введите элементы списка: ").split()))
m = a[0]
l = 0
r = 0
for i in range(N):
    s = 0
    for j in range(i, N):
        s += a[j]
        if s > m:
            m = s
            l = i
            r = j
print(f"Начальный индекс: {l}")
print(f"Конечный индекс: {r}")