def reverse_array(idx, array):
    mid_idx = len(array) // 2

    if idx >= mid_idx:
        return

    array[idx], array[len(array) - 1 - idx] = array[len(array) - 1 - idx], array[idx]
    reverse_array(idx + 1, array)


array = [int(x) for x in input().split()]

reverse_array(0, array)

print(' '.join(str(x) for x in array))