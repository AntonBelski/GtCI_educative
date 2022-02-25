def find_missing_number(nums):
    i, n = 0, len(nums)
    while i < n:
        if nums[i] < n and i != nums[i]:
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        else:
            i += 1

    for i in range(n):
        if nums[i] != i:
            return i

    return len(nums)


def main():
    print(find_missing_number([4, 0, 3, 1]))
    print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))


main()
