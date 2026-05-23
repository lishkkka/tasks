a, b, c = map(float, input("Размеры кирпича (a b c): ").split())
x, y = map(float, input("Размеры отверстия (x y): ").split())

def fits(w, h):
    return (w <= x and h <= y) or (w <= y and h <= x)

if fits(a, b) or fits(a, c) or fits(b, c):
    print("Кирпич пройдёт")
else:
    print("Не пройдёт")