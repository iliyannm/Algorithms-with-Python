numbers = [int(x) for x in input().split()]


def bubble_sort(nums):
    for i in range(len(nums) - 1):
        for j in range(1, len(nums)):
            if nums[j - 1] > nums[j]:
                nums[j - 1], nums[j] = nums[j], nums[j - 1]

    return ' '.join(str(x) for x in nums)


print(bubble_sort(numbers))
