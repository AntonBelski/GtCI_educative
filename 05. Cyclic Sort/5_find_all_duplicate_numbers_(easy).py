def find_all_duplicates(nums):
    n = len(nums)
    results = []

    for i in range(n):
        while nums[i] != nums[nums[i] - 1]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

    for i in range(n):
        if i + 1 != nums[i]:
            results.append(nums[i])

    return results


def main():
    print(find_all_duplicates([3, 4, 4, 5, 5]))
    print(find_all_duplicates([5, 4, 7, 2, 3, 5, 3]))


main()
