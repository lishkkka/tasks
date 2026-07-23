N = int(input("Введите количество элементов: "))
a = list(map(int, input("Введите элементы списка: ").split()))
b = []
for i in range(N):
    m = a[0]
    for j in range(N):
        if j != i:
            if a[j] > m or j == 0:
                m = a[j]
    flag = 0
    for j in range(len(b)):
        if b[j] == m:
            flag = 1
    if flag == 0:
        b.append(m)
for i in range(len(b)):
    for j in range(i + 1, len(b)):
        if b[i] > b[j]:
            b[i], b[j] = b[j], b[i]
print(f"Результат: {b}")

