N = int(input("Введите количество элементов: "))
a = list(map(int, input("Введите элементы списка: ").split()))
b = []
for i in range(N):
    flag = 0
    for j in range(len(b)):
        if a[i] == b[j]:
            flag = 1
    if flag == 0:
        b.append(a[i])
for i in range(len(b)):
    print(b[i])