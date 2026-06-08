n = int(input("Введите натуральное число: "))
r = -1
for i in range(10):
    count = 0
    N=n
    while N > 0:
        if N % 10 == i:
            count += 1
        N //= 10
    if count == 1:
        r = i
        break
if r == -1:
    print("нет")
else:
    print(r)