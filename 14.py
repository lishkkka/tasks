y = float(input("Угол часовой стрелки (градусы): "))
total = y * 2
hours = int(total // 60)
minutes = int(total % 60)
print(f"Часов: {hours}, минут: {minutes}")