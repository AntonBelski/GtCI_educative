def binary_search(arr, key):
    is_ascending = arr[0] <= arr[len(arr) - 1]
    lo, hi = 0, len(arr)

    while lo != hi:
        mid = (lo + hi) // 2
        if not is_ascending:
            place = len(arr) - mid - 1
        else:
            place = mid
        if key <= arr[place]:
            hi = mid
        else:
            lo = mid + 1

    if not is_ascending:
        lo = len(arr) - lo - 1

    if 0 <= lo < len(arr) and arr[lo] == key:
        return lo
    else:
        return -1


def main():
    print(binary_search([4, 6, 10], 10))
    print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
    print(binary_search([10, 6, 4], 10))
    print(binary_search([10, 6, 4], 4))
    print(binary_search([10, 5], 100))
    print(binary_search([10, 5], 0))
    print(binary_search([10, 5], 5))
    print(binary_search([10, 5], 10))


main()
