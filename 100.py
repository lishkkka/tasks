N = int(input("Введите количество элементов: "))
a = list(map(int, input("Введите элементы списка: ").split()))
flag = 0
for x in range(-1, N):
    b = []
    for i in range(N):
        if i != x:
            b.append(a[i])
    check = 1
    for i in range(1, len(b) - 1):
        if b[i] < b[i - 1] and b[i] < b[i + 1]:
            check = 0
        if b[i] > b[i - 1] and b[i] > b[i + 1]:
            check = 0
    if check == 1:
        flag = 1
if flag == 1:
    print("Да")
else:
    print("Нет")