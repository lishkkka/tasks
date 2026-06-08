a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
x, y = a, b
while b != 0:
    a, b = b, a % b
print(f"НОД({x}, {y}) = {a}")