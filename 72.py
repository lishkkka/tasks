N = int(input("Введите длину списков: "))
a = list(map(int, input("Введите первый список: ").split()))
b = list(map(int, input("Введите второй список: ").split()))
flag = 0
for x in range(N):
    check = 1
    for i in range(N):
        if a[(i + x) % N] != b[i]:
            check = 0
    if check == 1:
        flag = 1
if flag == 1:
    print("Да")
else:
    print("Нет")