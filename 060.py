N = int(input("Введите количество элементов: "))
a = list(map(int, input("Введите элементы списка: ").split()))
flag = 1
for i in range(N):
    if a[i] != a[N-i-1]:
        flag = 0
if flag == 1:
    print("Список является палиндромом")
else:
    print("Список не является палиндромом")
