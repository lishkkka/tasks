while True:
    n = int(input("Введите целое число: "))

    if n > 0:
        print("positive")
    elif n < 0:
        print("negative")
    else:
        print("zero")
        break