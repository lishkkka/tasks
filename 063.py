N = int(input("Введите количество элементов: "))
a = list(map(int, input("Введите элементы списка: ").split()))
m = 0
x = a[0]
for i in range(N):
    count = 0
    for j in range(N):
        if a[i] == a[j]:
            count += 1
    if count > m:
        m = count
        x = a[i]
print(x)
