N = int(input("Введите количество элементов: "))
a = list(map(int, input("Введите элементы списка: ").split()))
s = 0
left = 0
count = 0
for i in range(N):
    s += a[i]
for i in range(N-1):
    left += a[i]
    if left == s - left:
        count += 1
print(f"Количество способов: {count}")
