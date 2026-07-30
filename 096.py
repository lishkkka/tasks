N = int(input("Введите количество элементов: "))
a = list(map(int, input("Введите элементы списка: ").split()))
u = []
for i in range(N):
    flag = 0
    for j in range(len(u)):
        if a[i] == u[j]:
            flag = 1
    if flag == 0:
        u.append(a[i])
m = N
for i in range(N):
    b = []
    for j in range(i, N):
        flag = 0
        for k in range(len(b)):
            if a[j] == b[k]:
                flag = 1
        if flag == 0:
            b.append(a[j])
        if len(b) == len(u):
            if j - i + 1 < m:
                m = j - i + 1
            break
print(f"Минимальная длина: {m}")
