N = int(input("Введите количество элементов: "))
a = list(map(int, input("Введите элементы списка: ").split()))
flag = 0
for i in range(1, N-1):
    if a[i-1] < a[i] and a[i] > a[i+1]:
        print(a[i])
        flag = 1
        break
if flag == 0:
    print("no")
