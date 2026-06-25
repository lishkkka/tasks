N = int(input("Введите количество элементов: "))
a = list(map(int, input("Введите элементы списка: ").split()))
count = 0
for i in range(1, N-1):
    if a[i] > a[i-1] and a[i] > a[i+1]:
        count += 1
print(count)