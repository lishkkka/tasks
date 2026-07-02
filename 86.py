N = int(input("Введите количество элементов: "))
a = list(map(int, input("Введите элементы списка: ").split()))
count = 0
for i in range(N):
    for j in range(i + 1, N):
        if a[i] > a[j]:
            count += 1
print(f"Количество инверсий: {count}")