def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)


print(factorial(int(input())))

# factorial(0) = 1
# factorial(1) = 1
# factorial(2) = 2
# factorial(3) = 6
# factorial(4) = 24
# factorial(5) = 120
