m = int(input("Введите номер масти (1-4): "))
k = int(input("Введите номер достоинства (6-14): "))

if m == 1:
    suit = "пик"
elif m == 2:
    suit = "треф"
elif m == 3:
    suit = "бубен"
else:
    suit = "черв"

if k == 6:
    rank = "Шестерка"
elif k == 7:
    rank = "Семерка"
elif k == 8:
    rank = "Восьмерка"
elif k == 9:
    rank = "Девятка"
elif k == 10:
    rank = "Десятка"
elif k == 11:
    rank = "Валет"
elif k == 12:
    rank = "Дама"
elif k == 13:
    rank = "Король"
else:
    rank = "Туз"

print(f"{rank} {suit}")