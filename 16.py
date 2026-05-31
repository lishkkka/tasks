x1, y1 = map(float, input("Введите координаты левого нижнего угла первого прямоугольника (x y): ").split())
w1, h1 = map(float, input("Введите ширину и высоту первого прямоугольника: ").split())
x2, y2 = map(float, input("Введите координаты левого нижнего угла второго прямоугольника (x y): ").split())
w2, h2 = map(float, input("Введите ширину и высоту второго прямоугольника: ").split())

x1_right, y1_top = x1 + w1, y1 + h1
x2_right, y2_top = x2 + w2, y2 + h2

first_in_second = (x2 <= x1 and y2 <= y1 and x1_right <= x2_right and y1_top <= y2_top)

second_in_first = (x1 <= x2 and y1 <= y2 and x2_right <= x1_right and y2_top <= y1_top)
one_in_another = first_in_second or second_in_first

not_intersect = (x1_right <= x2) or (x2_right <= x1) or (y1_top <= y2) or (y2_top <= y1)
intersect = not not_intersect

print(f"а) Все точки первого прямоугольника принадлежат второму: {first_in_second}")
print(f"б) Все точки одного из прямоугольников принадлежат другому: {one_in_another}")
print(f"в) Прямоугольники пересекаются: {intersect}")