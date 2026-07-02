N = int(input("Введите количество элементов: "))
a = list(map(int, input("Введите элементы списка: ").split()))
b = []
for i in range(N):
    d = 0
    for j in range(i + 1, N):
        if a[i] == a[j]:
            d = j - i
            break
    b.append(d)
print("Результат:", *b)