for n in range(10, 100):
    a = n // 10
    b = n % 10
    if (a + b) ** 2 == n:
        print(n)
