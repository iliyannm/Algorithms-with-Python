nums = [int(x) for x in input().split()]


def quick_sort(start, end, nums):
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

    nums[pivot], nums[right_pointer] = nums[right_pointer], nums[pivot]

    quick_sort(start, right_pointer - 1, nums)
    quick_sort(left_pointer, end, nums)


quick_sort(0, len(nums) - 1, nums)

print(*nums, sep=' ')
