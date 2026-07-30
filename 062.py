N = int(input("Введите количество элементов: "))
a = list(map(int, input("Введите элементы списка: ").split()))
flag = 0
for i in range(N):
    count = 0
    for j in range(N):
        if a[i] == a[j]:
            count += 1
    if count == 1:
        print(a[i])
        flag = 1
if flag == 0:
    print("no")
