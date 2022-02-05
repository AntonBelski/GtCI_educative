def triplet_sum_close_to_target(nums, target):
    nums.sort()
    closest = float('inf')

    for i in range(len(nums) - 2):
        curr_closest = twoSum(nums[i], nums[i + 1:], target)
        if abs(target - curr_closest) < abs(target - closest):
            closest = curr_closest

    return closest


def twoSum(first, curr_nums, target):
    l = 0
    r = len(curr_nums) - 1
    curr_closest = float('inf')

    while r > l:
        curr_sum = first + curr_nums[l] + curr_nums[r]
        if abs(target - curr_sum) < abs(target - curr_closest):
            curr_closest = curr_sum

        if curr_sum > target:
            r -= 1
        else:
            l += 1

    return curr_closest


def main():
    print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
    print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
    print(triplet_sum_close_to_target([1, 0, 1, 1], 100))


main()
