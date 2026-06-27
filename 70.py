N = int(input("Введите количество элементов: "))
a = list(map(int, input("Введите элементы списка: ").split()))
s = 0
for i in range(N):
    s += a[i]
left = 0
flag = 0
for i in range(N-1):
    left += a[i]
    if left == s - left:
        flag = 1
if flag == 1:
    print("Да")
else:
    print("Нет")