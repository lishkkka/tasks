N = int(input("Введите количество элементов: "))
a = list(map(int, input("Введите элементы списка: ").split()))
flag = 0
for i in range(N):
    for j in range(i + 1, N):
        b = a.copy()
        b[i], b[j] = b[j], b[i]
        check = 1
        for k in range(N - 1):
            if b[k] >= b[k + 1]:
                check = 0
        if check == 1:
            flag = 1
if flag == 1:
    print("Да")
else:
    print("Нет")
