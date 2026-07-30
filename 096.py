N = int(input("Введите количество элементов: "))
a = list(map(int, input("Введите элементы списка: ").split()))
u = []
for i in range(N):
    f = 0
    for j in range(len(u)):
        if a[i] == u[j]:
            flag = 1
    if f == 0:
        u.append(a[i])
m = N
for i in range(N):
    b = []
    for j in range(i, N):
        f = 0
        for k in range(len(b)):
            if a[j] == b[k]:
                f = 1
        if f == 0:
            b.append(a[j])
        if len(b) == len(u):
            if j - i + 1 < m:
                m = j - i + 1
            break
print(f"Минимальная длина: {m}")
