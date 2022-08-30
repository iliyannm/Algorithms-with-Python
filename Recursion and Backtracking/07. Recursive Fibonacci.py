def find_fibonacci(n):
    result = 0
    fib_1 = 1
    fib_2 = 1

    for i in range(n - 1):
        result = fib_1 + fib_2
        fib_1, fib_2 = fib_2, result

    return result


print(find_fibonacci(int(input())))
