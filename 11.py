N = int(input("Школьников: "))
k = int(input("Яблок: "))
e = k // N
r = k % N
print(f"Каждому: {e}, осталось: {r}")