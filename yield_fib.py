# yield_fib

cube = lambda x: x**3

def fibonacci_yield(n):
    if n == 0:
        return

    yield 0
    if n > 1:
        yield 1
    a, b, m = 0, 1, 2
    while m < n:
        m += 1
        a, b = b, a + b
        yield b
    
def fibonacci(n):
    A = [0, 1]
    for x in range(2, n): A.append(A[x-1] + A[x-2])
    return A[:n]

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
    