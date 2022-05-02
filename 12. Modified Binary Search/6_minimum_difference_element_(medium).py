def search_min_diff_element(arr, x):
    lo, hi = 0, len(arr) - 1
    while lo != hi:
        mid = (lo + hi) // 2
        if x <= arr[mid]:
            hi = mid
        else:
            lo = mid + 1

    if lo > 0 and abs(arr[lo - 1] - x) <= abs(arr[lo] - x):
        lo -= 1

    return arr[lo]


def main():
    print(search_min_diff_element([4, 6, 10], 7))
    print(search_min_diff_element([4, 6, 10], 4))
    print(search_min_diff_element([1, 3, 8, 10, 15], 12))
    print(search_min_diff_element([4, 6, 10], 17))


main()
