N = int(input("Введите количество элементов первого списка: "))
a = list(map(int, input("Введите элементы первого списка: ").split()))
M = int(input("Введите количество элементов второго списка: "))
b = list(map(int, input("Введите элементы второго списка: ").split()))
c = []
i = 0
j = 0
while i < N and j < M:
    if a[i] < b[j]:
        if len(c) == 0 or c[len(c) - 1] != a[i]:
            c.append(a[i])
        i += 1
    elif a[i] > b[j]:
        if len(c) == 0 or c[len(c) - 1] != b[j]:
            c.append(b[j])
        j += 1
    else:
        if len(c) == 0 or c[len(c) - 1] != a[i]:
            c.append(a[i])
        i += 1
        j += 1
while i < N:
    if len(c) == 0 or c[len(c) - 1] != a[i]:
        c.append(a[i])
    i += 1
while j < M:
    if len(c) == 0 or c[len(c) - 1] != b[j]:
        c.append(b[j])
    j += 1
print(f"Результат: {c}")
