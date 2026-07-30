N = int(input("Введите количество элементов: "))
a = list(map(int, input("Введите элементы списка: ").split()))
flag = 0
for i in range(N):
    for j in range(i + 1, N):
        if a[i] == a[j]:
            check = 1
            for k in range(i + 1, j):
                for l in range(k + 1, j):
                    if a[k] == a[l]:
                        check = 0
            if check == 1:
                flag = 1
if flag == 1:
    print("Да")
else:
    print("Нет")
