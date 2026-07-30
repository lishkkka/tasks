n = input("Введите натуральное число: ")
l = c = 1
for i in range(1, len(n)):
    if n[i] == n[i - 1]:
        c += 1
        if c > l:
            l = c
    else:
        c = 1
print(l)