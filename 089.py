N = int(input("Введите количество элементов: "))
a = list(map(int, input("Введите элементы списка: ").split()))
b = []
for i in range(N - 2):
    x = a[i]
    y = a[i + 1]
    z = a[i + 2]
    if (x >= y and x <= z) or (x >= z and x <= y):
        t = x
    elif (y >= x and y <= z) or (y >= z and y <= x):
        t = y
    else:
        t = z
    flag = 0
    for j in range(len(b)):
        if b[j] == t:
            flag = 1
    if flag == 0:
        b.append(t)
print(f"Количество различных значений: {len(b)}")
