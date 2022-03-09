def twoSum(first, curr_num, target):
    l = 0
    r = len(curr_num) - 1
    result = 0

    while r > l:
        curr_sum = first + curr_num[r] + curr_num[l]
        if curr_sum < target:
            result += r - l
            l += 1
        else:
            r -= 1

    return result


def triplet_with_smaller_sum(nums, target):
    result = 0
    nums.sort()

    for i in range(len(nums) - 2):
        result += twoSum(nums[i], nums[i + 1:], target)

    return result


def main():
    print(triplet_with_smaller_sum([-1, 0, 2, 3], 3))
    print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))


main()
