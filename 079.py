N = int(input("Введите количество элементов: "))
a = list(map(int, input("Введите элементы списка: ").split()))
s = 0
flag = 0
for i in range(N):
    if a[i] == s:
        flag = 1
    s += a[i]
if flag == 1:
    print("Да")
else:
    print("Нет")
