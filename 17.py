a, b = map(int, input("Позиция фигуры (a b): ").split())
c, d = map(int, input("Позиция цели (c d): ").split())

print("Ладья угрожает:", a == c or b == d)
print("Слон угрожает:", abs(a - c) == abs(b - d))
print("Король может попасть:", max(abs(a - c), abs(b - d)) == 1)
print("Ферзь угрожает:", a == c or b == d or abs(a - c) == abs(b - d))

normal = (c == a and d == b + 1)
double = (b == 2 and c == a and d == 4)
print("Пешка (обычный ход):", normal or double)

print("Пешка (бьёт):", abs(a - c) == 1 and d == b + 1)