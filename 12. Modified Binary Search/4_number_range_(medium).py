def binary_search(arr, x):
    lo, hi = 0, len(arr)
    while lo != hi:
        mid = (lo + hi) // 2
        if x <= arr[mid]:
            hi = mid
        else:
            lo = mid + 1
    return lo


def find_range(nums, target):
    start = binary_search(nums, target)
    end = binary_search(nums, target + 1) - 1

    if start < len(nums) and nums[start] == target:
        return [start, end]
    else:
        return [-1, -1]


def main():
    print(find_range([4, 6, 6, 6, 9], 6))
    print(find_range([1, 3, 8, 10, 15], 10))
    print(find_range([1, 3, 8, 10, 15], 12))


main()
