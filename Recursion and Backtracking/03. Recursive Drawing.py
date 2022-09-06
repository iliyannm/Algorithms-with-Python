def drawning(n):
    if n == 0:
        return

    print('*' * n)
    drawning(n - 1)
    print('#' * n)


drawning(int(input()))
