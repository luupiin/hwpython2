def fibonacci(n):
    n1, n2 = 1, 1
    print(n1, n2, end=" " )
    for i in range(n + 1):
        yield n1+n2
        n1, n2 = n2, n1+n2

print(*fibonacci(10))