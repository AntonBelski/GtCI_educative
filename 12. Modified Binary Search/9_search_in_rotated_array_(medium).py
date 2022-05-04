def search_rotated_array(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo != hi:
        mid = (lo + hi) // 2
        if nums[lo] < nums[hi] or nums[mid + 1] > nums[hi]:
            lo = mid + 1
        else:
            hi = mid
    min_ind = (lo + 1) % len(nums)

    lo, hi = 0, len(nums) - 1
    while lo != hi:
        mid = (lo + hi) // 2
        if target <= nums[(mid + min_ind) % len(nums)]:
            hi = mid
        else:
            lo = mid + 1

    real_lo = (lo + min_ind) % len(nums)
    if nums[real_lo] == target:
        return real_lo
    else:
        return -1


def main():
    print(search_rotated_array([10, 15, 1, 3, 8], 15))
    print(search_rotated_array([4, 5, 7, 9, 10, -1, 2], 10))


main()
