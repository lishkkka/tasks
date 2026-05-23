print("Введите координаты вершин A, B, C, D по порядку:")
x1, y1 = map(float, input("A (x y): ").split())
x2, y2 = map(float, input("B (x y): ").split())
x3, y3 = map(float, input("C (x y): ").split())
x4, y4 = map(float, input("D (x y): ").split())

area = abs((x1*y2 + x2*y3 + x3*y4 + x4*y1) - (y1*x2 + y2*x3 + y3*x4 + y4*x1)) / 2
print(f"Площадь четырехугольника =", area)