N = int(input("Введите количество элементов: "))
a = list(map(int, input("Введите элементы списка: ").split()))
m = 0
for i in range(N):
    b = []
    count = 0
    for j in range(i, N):
        flag = 0
        for x in range(len(b)):
            if a[j] == b[x]:
                flag = 1
        if flag == 1:
            break
        b.append(a[j])
        count += 1
    if count > m:
        m = count
print(f"Максимальная длина: {m}")
