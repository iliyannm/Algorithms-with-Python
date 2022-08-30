def find_combo(idx, combination, number):
    if idx >= len(combination):
        print(*combination, sep=' ')
        return

    for num in range(1, number + 1):
        combination[idx] = num
        find_combo(idx + 1, combination, number)


n = int(input())
sequence = [1] * n
find_combo(0, sequence, n)
