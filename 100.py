N = int(input("Введите количество элементов: "))
a = list(map(int, input("Введите элементы списка: ").split()))


def stable(arr):
    if len(arr) <= 2:
        return True
    for i in range(1, len(arr) - 1):
        if not (min(arr[i - 1], arr[i + 1]) <= arr[i] <= max(arr[i - 1], arr[i + 1])):
            return False
    return True

if stable(a):
    print("Да")
else:
    f = 0
    for i in range(N):
        new_arr = a[:i] + a[i + 1:]
        if stable(new_arr):
            f= 1
            break

    if f == 1:
        print("Да")
    else:
        print("Нет")