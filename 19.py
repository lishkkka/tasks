a, b, c = map(float, input("Три числа: ").split())
for x in (a, b, c):
    if 1.6 <= x <= 3.8:
        print(x)