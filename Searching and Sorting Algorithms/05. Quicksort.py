numbers = [int(x) for x in input().split()]


def quick_sort(nums, start, end):
    if start >= end:
        return

    pivot, left_pointer, right_pointer = start, start + 1, end

    while left_pointer <= right_pointer:
        if nums[left_pointer] > nums[pivot] > nums[right_pointer]:
            nums[left_pointer], nums[right_pointer] = nums[right_pointer], nums[left_pointer]

        if nums[left_pointer] <= nums[pivot]:
            left_pointer += 1

        if nums[right_pointer] >= nums[pivot]:
            right_pointer -= 1

    quick_sort(nums, start, right_pointer - 1)
    quick_sort(nums, left_pointer, end)

