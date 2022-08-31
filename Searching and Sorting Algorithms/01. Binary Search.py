numbers = [int(x) for x in input().split()]
searched_number = int(input())


def binary_search(array, target):
    left_pointer = 0
    right_pointer = len(array) - 1

    while left_pointer <= right_pointer:
        mid_idx = (left_pointer + right_pointer) // 2
        mid_el = array[mid_idx]

        if mid_el == target:
            return mid_idx

        if target < mid_el:
            right_pointer = mid_idx - 1
        else:
            left_pointer = mid_idx + 1

    return -1


print(binary_search(numbers, searched_number))
