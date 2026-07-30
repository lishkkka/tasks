N = int(input("Введите число N: "))
for n in range(2, N + 1):
    p = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            p = False
            break
    if p:
        print(n, end=" ")
