N = int(input("Введите количество элементов: "))
a = list(map(int, input("Введите элементы списка: ").split()))
count = 1
m = 1
for i in range(1, N):
    if a[i-1] > a[i]:
        count += 1
    else:
        count = 1
    if count > m:
        m = count
print(m)