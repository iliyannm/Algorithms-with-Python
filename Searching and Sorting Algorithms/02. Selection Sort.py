numbers = [int(x) for x in input().split()]

for idx in range(len(numbers)):
    min_idx = idx
    for nxt_idx in range(idx + 1, len(numbers)):
        if numbers[nxt_idx] < numbers[idx]:
            min_idx = nxt_idx
            numbers[idx], numbers[min_idx] = numbers[min_idx], numbers[idx]

print(*numbers, sep=' ')
