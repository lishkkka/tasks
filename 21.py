a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

if a <= b and a <= c:
    min1 = a
    if b <= c:
        min2 = b
    else:
        min2 = c
elif b <= a and b <= c:
    min1 = b
    if a <= c:
        min2 = a
    else:
        min2 = c
else:
    min1 = c
    if a <= b:
        min2 = a
    else:
        min2 = b

result = min1 * min2

print(f"Произведение двух наименьших чисел: {result}")