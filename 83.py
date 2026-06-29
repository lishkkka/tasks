N = int(input("Введите количество элементов: "))
a = list(map(int, input("Введите элементы списка: ").split()))
m = N + 1
for i in range(N):
    s = 0
    for j in range(i, N):
        s += a[j]
        if s > 0:
            if j - i + 1 < m:
                m = j - i + 1
if m == N + 1:
    print("no")
else:
    print(f"Минимальная длина: {m}")