N = int(input("Введите количество элементов: "))
a = list(map(int, input("Введите элементы списка: ").split()))
count = 0
flag = 1
for i in range(N):
    c = 0
    for j in range(N):
        if a[i] == a[j]:
            c += 1
    if c == 2:
        count += 1
    elif c > 2:
        flag = 0
if flag == 1 and count == 2:
    print("Да")
else:
    print("Нет")