N = list(map(int, input("Введите элементы списка: ").split()))
count = 0
for i in range(len(N)):
    if N[i] % 2 == 0:
        count += 1
print(count)