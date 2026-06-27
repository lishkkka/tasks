N = int(input("Введите количество элементов: "))
a = list(map(int, input("Введите элементы списка: ").split()))
flag = 0
for i in range(N):
    s = 0
    for j in range(i, N):
        s += a[j]
        if s == 0 and j - i + 1 >= 2:
            flag = 1
if flag == 1:
    print("Да")
else:
    print("Нет")