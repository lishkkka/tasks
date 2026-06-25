N = list(map(int, input("Введите элементы списка: ").split()))
m = N[0]
index = 0
for i in range(len(N)):
    if N[i] > m:
        m = N[i]
        index = i
print(index)