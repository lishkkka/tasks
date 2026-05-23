total = 20
floors = 5
per_floor = total // floors
number = int(input("Введите номер квартиры: "))
if number < 1 or number > total:
    print(f"Квартиры №{number} нет в этом подъезде.")
else:
    floor = (number - 1) // per_floor + 1
    number2 = (number - 1) % per_floor + 1
    print(f"Этаж: {floor}, по счету {number2}-ая")