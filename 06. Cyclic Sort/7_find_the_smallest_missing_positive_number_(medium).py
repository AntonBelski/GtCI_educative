def find_first_smallest_missing_positive(nums):
    n = len(nums)

    for i in range(n):
        while 0 < nums[i] < n + 1 and nums[i] != nums[nums[i] - 1]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

    for i in range(n):
        if i + 1 != nums[i]:
            return i + 1

    return n + 1


def main():
    print(find_first_smallest_missing_positive([-3, 1, 5, 4, 2]))
    print(find_first_smallest_missing_positive([3, -2, 0, 1, 2]))
    print(find_first_smallest_missing_positive([3, 2, 5, 1]))


main()
