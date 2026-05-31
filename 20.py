weight = float(input("Вес боксёра (кг): "))
if weight < 60:
    print("Лёгкий вес")
elif weight < 64:
    print("Первый полусредний вес")
elif weight < 69:
    print("Полусредний вес")
else:
    print("Выше категорий")