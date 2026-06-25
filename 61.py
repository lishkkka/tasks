N = int(input("Введите количество элементов: "))
a = list(map(int, input("Введите элементы списка: ").split()))
flag = 0
for x in range(N):
    b = a[:x] + a[x + 1:]
    check = 1
    for i in range(len(b)):
        if b[i] != b[len(b) - i - 1]:
            check = 0
    if check == 1:
        flag = 1
if flag == 1:
    print("Можно получить палиндром")
else:
    print("Нельзя получить палиндром")