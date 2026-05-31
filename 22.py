month = int(input("Введите номер месяца (1-12): "))

if month == 2:
    days = 28
elif month in (4, 6, 9, 11):
    days = 30
else:
    days = 31

print(f"Дней в этом месяце: {days} ")