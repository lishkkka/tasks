N = int(input("Введите количество элементов первого списка: "))
a = list(map(int, input("Введите элементы первого списка: ").split()))
M = int(input("Введите количество элементов второго списка: "))
b = list(map(int, input("Введите элементы второго списка: ").split()))
c = []
i = 0
j = 0
while i < N and j < M:
    if a[i] == b[j]:
        c.append(a[i])
        i += 1
        j += 1
    elif a[i] < b[j]:
        i += 1
    else:
        j += 1
print(f"Общие элементы: {c}")
