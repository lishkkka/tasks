N = int(input("Введите количество элементов: "))
a = list(map(int, input("Введите элементы списка: ").split()))
m = a[0]
l = 0
r = 0
for i in range(N):
    if a[i] > m:
        m = a[i]
for i in range(N):
    if a[i] == m:
        l = i
        break
for i in range(N - 1, -1, -1):
    if a[i] == m:
        r = i
        break
count = 0
for i in range(l + 1, r):
    flag = 0
    for j in range(l + 1, i):
        if a[i] == a[j]:
            flag = 1
    if flag == 0:
        count += 1
print(f"Количество различных элементов: {count}")
