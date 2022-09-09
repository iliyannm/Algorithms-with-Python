numbers = [int(x) for x in input().split()]
target_number = int(input())


def binary_search(nums, target):
    left_pointer = 0
    right_pointer = len(nums) - 1

    while left_pointer <= right_pointer:
        mid_idx = (left_pointer + right_pointer) // 2

        if nums[mid_idx] == target:
            return mid_idx

        if target < nums[mid_idx]:
            right_pointer = mid_idx - 1
        else:
            left_pointer = mid_idx + 1

    return -1


print(binary_search(numbers, target_number))
