N = int(input("Введите количество элементов: "))
a = list(map(int, input("Введите элементы списка: ").split()))
m = N
for i in range(N):
    for j in range(i, N):
        b = []
        for k in range(N):
            if k < i or k > j:
                b.append(a[k])
        flag = 1
        for k in range(len(b) - 1):
            if b[k] > b[k + 1]:
                flag = 0
        if flag == 1:
            if j - i + 1 < m:
                m = j - i + 1
print(f"Минимальная длина: {m}")
