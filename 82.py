N = int(input("Введите количество элементов: "))
a = list(map(int, input("Введите элементы списка: ").split()))
s = 0
for i in range(N):
    s += a[i]
flag = 0
if s % 3 == 0:
    x = s // 3
    left = 0
    count = 0
    for i in range(N):
        left += a[i]
        if left == x:
            count += 1
            left = 0
    if count == 3:
        flag = 1
if flag == 1:
    print("Да")
else:
    print("Нет")