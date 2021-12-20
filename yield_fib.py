# yield_fib


def fib_yield(n):
    a, b = 0, 1
    while n > 0:
        yield a
        n -= 1
        a, b = b, a + b

if __name__ == '__main__':
    n = int(input("N = "))
    fib = fib_yield(n)
    print(fib)
    for x in fib:
        print(x, end=' ')
    print("")
    