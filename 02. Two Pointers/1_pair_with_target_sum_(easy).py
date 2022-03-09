def pair_with_targetsum(nums, target):
    left = 0
    right = len(nums) - 1

    while nums[left] + nums[right] != target:
        if nums[left] + nums[right] > target:
            right -= 1
        if nums[left] + nums[right] < target:
            left += 1

    return [left, right]


def main():
    print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
    print(pair_with_targetsum([2, 5, 9, 11], 11))


main()
