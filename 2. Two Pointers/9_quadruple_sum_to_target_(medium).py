def twoSum(first, second, curr_nums, target, result):
    l = 0
    r = len(curr_nums) - 1

    while r > l:
        curr_sum = first + second + curr_nums[r] + curr_nums[l]
        if curr_sum > target:
            r -= 1
        elif curr_sum < target:
            l += 1
        else:
            result.add((first, second, curr_nums[l], curr_nums[r]))
            l += 1


def search_quadruplets(nums, target):
    if len(nums) < 4:
        return []

    custom_nums = sorted(list(nums))
    result = set()

    for start in range(len(custom_nums) - 3):
        for second in range(start + 1, len(custom_nums) - 2):
            twoSum(custom_nums[start], custom_nums[second], custom_nums[second + 1:], target, result)

    return [list(x) for x in result]


def main():
    print(search_quadruplets([4, 1, 2, -1, 1, -3], 1))
    print(search_quadruplets([2, 0, -1, 1, -2, 2], 2))


main()
