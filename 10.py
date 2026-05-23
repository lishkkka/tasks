total = 15
floors = 5
per_floor = total // floors
number = int(input("Введите номер квартиры: "))
if number < 1 or number > total:
    print(f"Квартиры №{number} нет в этом подъезде.")
else:
    floor = (number - 1) // per_floor + 1
    print(f"Квартира №{number} находится на {floor}-м этаже.")