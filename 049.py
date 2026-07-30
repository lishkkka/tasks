n = input("Введите натуральное число: ")
x = True
for i in range(len(n) - 1):
    if n[i] >= n[i + 1]:
        x = False
        break
if x:
    print("Да")
else:
    print("Нет")
