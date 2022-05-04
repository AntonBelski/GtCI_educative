def search_ceiling_of_a_number(arr, k):
    lo, hi = 0, len(arr)

    while lo != hi:
        mid = (lo + hi) // 2
        if k <= arr[mid]:
            hi = mid
        else:
            lo = mid + 1

    if lo == len(arr):
        lo = -1

    return lo


def main():
    print(search_ceiling_of_a_number([4, 6, 10], 6))
    print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
    print(search_ceiling_of_a_number([4, 6, 10], 17))
    print(search_ceiling_of_a_number([4, 6, 10], -1))


main()
