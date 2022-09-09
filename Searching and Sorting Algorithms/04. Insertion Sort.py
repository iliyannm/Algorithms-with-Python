numbers = [int(x) for x in input().split()]


def insertion_sort(nums):
    for i in range(1, len(nums)):
        for j in range(i, 0, -1):
            if nums[j] < nums[j - 1]:
                nums[j - 1], nums[j] = nums[j], nums[j - 1]

    return ' '.join(str(x) for x in nums)


print(insertion_sort(numbers))
