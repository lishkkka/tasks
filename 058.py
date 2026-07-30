N = int(input("Введите количество элементов: "))
a = list(map(int, input("Введите элементы списка: ").split()))
index = -1
for i in range(1, N-1):
    if a[i-1] > a[i] and a[i] < a[i+1]:
        index = i
if index == -1:
    print("no")
else:
    print(index)
