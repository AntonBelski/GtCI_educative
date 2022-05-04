def count_rotations(nums):
    lo, hi = 0, len(nums) - 1
    while lo != hi:
        mid = (lo + hi) // 2
        if nums[lo] < nums[hi] or nums[lo] > nums[mid]:
            hi = mid
        else:
            lo = mid + 1
    return lo


def main():
    print(count_rotations([10, 15, 1, 3, 8]))
    print(count_rotations([4, 5, 7, 9, 10, -1, 2]))
    print(count_rotations([1, 3, 8, 10]))


main()
