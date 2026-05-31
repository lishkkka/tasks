a, b, c = map(float, input("Стороны a b c: ").split())
exists = a + b > c and a + c > b and b + c > a
print("Треугольник существует" if exists else "Не существует")