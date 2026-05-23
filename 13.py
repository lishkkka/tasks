h = int(input("Часы: "))
m = int(input("Минуты: "))
s = int(input("Секунды: "))
total = h * 3600 + m * 60 + s
angle = total * 360 / 43200
print(f"Угол часовой стрелки: {angle}")